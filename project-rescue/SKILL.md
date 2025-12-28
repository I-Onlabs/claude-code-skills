---
name: project-rescue
description: Emergency recovery patterns for when vibecoding goes wrong. Use when user mentions things like "everything broke", "nothing works", "it was working before", "I messed something up", "how do I undo", "project won't start", "dependencies broken", "git is messed up", errors after updates, blank screens, infinite loops, or any situation where a project that was working is now broken.
---

# Project Rescue

Recovery playbook for vibecoders. When in doubt, start from Level 1 and escalate.

## Quick Diagnosis

Ask: "What was the last thing you (or an AI) changed?" — this usually points to the problem.

## Recovery Levels

### Level 1: Soft Reset (Try First)

**App won't start or shows errors after changes:**
```bash
# Kill everything and restart
pkill -f node
npm run dev
```

**Weird behavior, stale state:**
```bash
# Clear caches
rm -rf .next .turbo .cache dist build .parcel-cache
npm run dev
```

**"Module not found" or import errors:**
```bash
rm -rf node_modules package-lock.json
npm install
```

### Level 2: Undo Recent Changes

**Undo last commit (keep changes as uncommitted):**
```bash
git reset --soft HEAD~1
```

**Discard ALL uncommitted changes (nuclear for files):**
```bash
git checkout .
git clean -fd
```

**See what changed recently:**
```bash
git log --oneline -10
git diff HEAD~1
```

### Level 3: Dependency Hell

**Lock file conflicts or weird version issues:**
```bash
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

**Python equivalent:**
```bash
rm -rf venv __pycache__ .pytest_cache
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Bun projects:**
```bash
rm -rf node_modules bun.lockb
bun install
```

**"But it works on the AI's machine":**
Check Node/Python version. Ask AI what version it assumed.

### Level 4: Git Is Messed Up

**Stuck in merge/rebase hell:**
```bash
git merge --abort
# or
git rebase --abort
```

**Detached HEAD (scary message, usually harmless):**
```bash
git checkout main  # or master
```

**Need to go back in time:**
```bash
git log --oneline -20           # find the good commit hash
git checkout <hash>             # look around
git checkout -b rescue-branch   # save it if good
```

**Complete git reset to remote (loses local changes):**
```bash
git fetch origin
git reset --hard origin/main
```

### Level 5: Nuclear Options

**Start fresh but keep your code:**
```bash
# Save your work
cp -r my-project my-project-backup

# Fresh clone
git clone <repo-url> my-project-fresh
cd my-project-fresh
npm install
```

**Port already in use:**
```bash
# macOS: Find what's using port 3000
lsof -i :3000
# Kill it
kill -9 <PID>

# Or kill all node processes
pkill -f node
```

**Firebase/Supabase acting weird:**
- Check the web console for the actual error
- Verify environment variables are set
- Check if you hit free tier limits

## IDE-Specific Recovery

### Cursor / Windsurf / VSCode
**AI made a mess of files:**
- Use Timeline (right-click file → Open Timeline) to restore previous versions
- Or: `git diff HEAD` to see changes, then `git checkout <file>` to restore specific files

**Extensions causing issues:**
- Disable all extensions, test, re-enable one by one

### Replit
**Project won't run:**
1. Click "Shell" tab
2. Run `kill 1` to restart the container
3. Or: `npm install` then `npm run dev`

**Out of resources:**
- Delete `node_modules`, `.next`, or other large folders
- Check storage usage in the Files pane

## Common Vibecoding Disasters

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Blank white screen | JS error, check console | Browser DevTools → Console |
| "Cannot find module" | Missing dependency | `npm install` |
| Infinite loop/freeze | useEffect or while loop bug | Undo last change |
| "EACCES permission" | npm permission issue | `sudo chown -R $USER ~/.npm` |
| API returns 401/403 | Bad/expired API key | Check .env file |
| Works locally, fails deployed | Missing env vars on host | Check Vercel/Netlify settings |
| Git says "diverged" | Local and remote differ | `git pull --rebase origin main` |
| TypeScript red everywhere | Types out of sync | `npm run build` or restart TS server |
| Tailwind styles not applying | Config or purge issue | Check tailwind.config.js content paths |
| Hot reload stopped | Dev server stuck | Kill and restart dev server |

## macOS Specific

**Clear system caches:**
```bash
# Homebrew
brew cleanup

# npm global
npm cache clean --force

# Xcode (if iOS dev)
rm -rf ~/Library/Developer/Xcode/DerivedData
```

**Node version issues:**
```bash
# Check version
node -v

# Switch with nvm
nvm use 18   # or whatever version
```

## Prevention Tips

1. **Commit before big changes** — `git add . && git commit -m "checkpoint before X"`
2. **One change at a time** — easier to undo
3. **Read error messages** — paste them to your AI, the answer is usually there
4. **Check the browser console** — right-click → Inspect → Console
5. **Save working states** — tag releases: `git tag working-v1`

## When All Else Fails

1. Copy your important files (src/, components/, etc.) somewhere safe
2. Start a fresh project with the same stack
3. Move your files back piece by piece
4. Each piece that breaks tells you where the bug is
