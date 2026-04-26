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

function verifySignature(req, body) {
  const sig = req.headers['x-hub-signature-256'];
  const expected = 'sha256=' + crypto.createHmac('sha256', SECRET).update(body).digest('hex');
  return sig && crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expected));
}

function isValidPrNumber(n) {
  return Number.isInteger(n) && n > 0 && n < 1_000_000;
}

createServer((req, res) => {
  if (req.url !== '/github-webhook') { res.writeHead(404); return res.end(); }

  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', () => {
    if (!verifySignature(req, body)) { res.writeHead(401); return res.end(); }

    const event = JSON.parse(body);
    const prNum = event.pull_request?.number ?? event.issue?.number;
    if (!isValidPrNumber(prNum)) { res.writeHead(400); return res.end(); }

    if (event.action === 'opened' && event.pull_request) {
      execFile('npx', ['ruv-swarm', 'github', 'pr-init', String(prNum)]);
    }

    if (event.comment && event.comment.body.startsWith('/swarm')) {
      // Forward as a single argv element; the consumer must parse and re-validate
      execFile('npx', ['ruv-swarm', 'github', 'handle-comment',
                       '--pr', String(prNum),
                       '--command', event.comment.body]);
    }

    res.writeHead(200);
    res.end('OK');
  });
}).listen(3000);
```
