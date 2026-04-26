# Swarm Management

How to spin up the review swarm from a PR and route agents.

## Create Swarm from PR

```bash
# From PR description
gh pr view 123 --json body,title,labels,files | npx ruv-swarm swarm create-from-pr

# Auto-spawn agents based on labels
gh pr view 123 --json labels | npx ruv-swarm swarm auto-spawn

# With full PR context
gh pr view 123 --json body,labels,author,assignees | \
  npx ruv-swarm swarm init --from-pr-data
```

## Label → Agent Mapping

```json
{
  "label-mapping": {
    "bug":         ["debugger", "tester"],
    "feature":     ["architect", "coder", "tester"],
    "refactor":    ["analyst", "coder"],
    "docs":        ["researcher", "writer"],
    "performance": ["analyst", "optimizer"],
    "security":    ["security", "authentication", "audit"]
  }
}
```

## Topology Selection by PR Size

```bash
npx ruv-swarm github pr-topology --pr 123
```

Heuristics:

| PR size | Topology |
|---|---|
| < 100 lines | ring |
| 100–500 lines | mesh |
| > 500 lines | hierarchical |

## PR Comment Commands

Trigger swarm actions directly from PR comments:

```markdown
/swarm init mesh 6
/swarm spawn coder "Implement authentication"
/swarm spawn tester "Write unit tests"
/swarm status
/swarm review --agents security,performance
```

## Webhook Handler

> **Security:** PR comment bodies and issue numbers are attacker-controlled. Never interpolate them into a shell command. Use `execFile` with an argv array, validate the PR number is numeric, and parse the command instead of forwarding the raw string.

```javascript
// webhook-handler.js
const { createServer } = require('http');
const { execFile } = require('child_process');
const crypto = require('crypto');

const SECRET = process.env.GITHUB_WEBHOOK_SECRET;
const MAX_BODY_BYTES = 25 * 1024 * 1024;   // GitHub caps at 25MB; reject anything larger

// Replay-protection cache: GitHub re-sends the same X-GitHub-Delivery on retry.
// In production, back this with Redis or a small DB so it survives restarts.
const seenDeliveries = new Set();

function verifySignature(req, body) {
  const sig = req.headers['x-hub-signature-256'];
  if (!sig) return false;
  const expected = 'sha256=' + crypto.createHmac('sha256', SECRET).update(body).digest('hex');
  const a = Buffer.from(sig);
  const b = Buffer.from(expected);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

function isValidPrNumber(n) {
  return Number.isInteger(n) && n > 0 && n < 1_000_000;
}

createServer((req, res) => {
  if (req.method !== 'POST')                  { res.writeHead(405); return res.end(); }
  if (req.url !== '/github-webhook')          { res.writeHead(404); return res.end(); }

  const delivery = req.headers['x-github-delivery'];
  if (!delivery)                              { res.writeHead(400); return res.end('missing X-GitHub-Delivery'); }
  if (seenDeliveries.has(delivery))           { res.writeHead(200); return res.end('duplicate'); }

  let body = '';
  let aborted = false;
  req.on('data', chunk => {
    body += chunk;
    if (body.length > MAX_BODY_BYTES) { aborted = true; req.destroy(); }
  });
  req.on('end', () => {
    if (aborted) { res.writeHead(413); return res.end(); }
    if (!verifySignature(req, body)) { res.writeHead(401); return res.end(); }

    seenDeliveries.add(delivery);   // mark only after signature verified

    const event = JSON.parse(body);
    const prNum = event.pull_request?.number ?? event.issue?.number;
    if (!isValidPrNumber(prNum)) { res.writeHead(400); return res.end(); }

    // Acknowledge within GitHub's 10-second budget; do real work async.
    res.writeHead(200);
    res.end('OK');

    if (event.action === 'opened' && event.pull_request) {
      execFile('npx', ['ruv-swarm', 'github', 'pr-init', String(prNum)]);
    }
    if (event.comment && event.comment.body.startsWith('/swarm')) {
      // Forward as a single argv element; the consumer must parse and re-validate.
      execFile('npx', ['ruv-swarm', 'github', 'handle-comment',
                       '--pr', String(prNum),
                       '--command', event.comment.body]);
    }
  });
}).listen(3000);
```

The handler addresses GitHub's documented webhook requirements: HMAC-SHA256 signature with timing-safe comparison, `X-GitHub-Delivery` for replay protection, 25 MB payload cap, POST-only, and a 200 response inside the 10-second budget (real work is dispatched after the response). For production, also enable IP allowlisting against [GitHub's published webhook IP ranges](https://api.github.com/meta) and back `seenDeliveries` with persistent storage.
