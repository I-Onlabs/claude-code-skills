---
name: git-helper
description: Version control made simple for vibecoders. Use when user asks about git, commits, branches, pushing, pulling, undoing changes, merge conflicts, or says things like "save my work", "go back to before", "I messed up git", "how do I undo", or needs to collaborate on code.
---

# Git Helper

Git commands translated for vibecoders.

## The Only Commands You Really Need

### Save Your Work
```bash
git add .
git commit -m "describe what you changed"
```

### Upload to GitHub/Remote
```bash
git push
```

### Download Latest Changes
```bash
git pull
```

## Common Tasks

### "I want to save a checkpoint before trying something risky"
```bash
git add .
git commit -m "checkpoint before trying X"
```

### "I want to undo what I just did"

**Undo last commit but keep the changes:**
```bash
git reset --soft HEAD~1
```

**Throw away all uncommitted changes:**
```bash
git checkout .
```

**Undo changes to a specific file:**
```bash
git checkout -- path/to/file.js
```

**Go back to how it was on GitHub:**
```bash
git fetch origin
git reset --hard origin/main
```

### "I want to see what changed"
```bash
git status              # what files changed
git diff                # what lines changed (unstaged)
git diff --staged       # what lines changed (staged)
git log --oneline -10   # last 10 commits
git show HEAD           # see last commit details
```

### "I want to work on something separate"
```bash
git checkout -b my-new-feature    # create branch
# ... do your work ...
git add .
git commit -m "my changes"
git push -u origin my-new-feature # upload branch
```

### "I want to get someone else's branch"
```bash
git fetch origin
git checkout their-branch-name
```

### "I want to merge my branch into main"
```bash
git checkout main
git pull
git merge my-new-feature
git push
```

## Fixing Mistakes

### "I committed to the wrong branch"
```bash
git reset --soft HEAD~1           # undo commit, keep changes
git stash                          # save changes temporarily
git checkout correct-branch        # switch branches
git stash pop                      # bring changes back
git add .
git commit -m "your message"
```

### "I need to change my last commit message"
```bash
git commit --amend -m "new message"
```

### "I want to add something to my last commit"
```bash
git add .
git commit --amend --no-edit
```

### "Git says I have merge conflicts"
1. Open the file with conflicts
2. Look for lines with `<<<<<<<`, `=======`, `>>>>>>>`
3. Keep the code you want, delete the markers
4. Save the file
5. `git add .` then `git commit -m "resolved conflicts"`

### "Git won't let me pull"
```bash
# Option 1: Save your changes first
git stash
git pull
git stash pop

# Option 2: Commit first
git add .
git commit -m "my changes"
git pull
```

### "I'm in 'detached HEAD' state"
Don't panic. Just:
```bash
git checkout main
```
If you have changes you want to keep:
```bash
git checkout -b save-my-work
```

### "I want to completely start over"
```bash
git fetch origin
git reset --hard origin/main
```
⚠️ This throws away ALL local changes

### "I accidentally deleted a file"
```bash
git checkout HEAD -- path/to/deleted/file.js
```

### "I need to grab just one commit from another branch"
```bash
git cherry-pick <commit-hash>
```

## Working with Stash

**Save changes for later (named):**
```bash
git stash push -m "work in progress on feature X"
```

**See all stashes:**
```bash
git stash list
```

**Restore a specific stash:**
```bash
git stash pop stash@{0}   # most recent
git stash pop stash@{1}   # second most recent
```

**Delete a stash:**
```bash
git stash drop stash@{0}
```

## Daily Workflow

**Start of day:**
```bash
git pull
```

**While working (save often):**
```bash
git add .
git commit -m "what I did"
```

**End of day:**
```bash
git push
```

## Branch Cleanup

**Delete local branch:**
```bash
git branch -d branch-name      # safe delete
git branch -D branch-name      # force delete
```

**Delete remote branch:**
```bash
git push origin --delete branch-name
```

**See all branches:**
```bash
git branch -a
```

## Quick Reference

| I want to... | Command |
|--------------|---------|
| Save work | `git add . && git commit -m "msg"` |
| Upload | `git push` |
| Download | `git pull` |
| Undo last commit | `git reset --soft HEAD~1` |
| Throw away changes | `git checkout .` |
| New branch | `git checkout -b branch-name` |
| Switch branch | `git checkout branch-name` |
| See status | `git status` |
| See history | `git log --oneline` |
| Save for later | `git stash` |
| Get saved work back | `git stash pop` |
| See what changed | `git diff` |
| Abort merge | `git merge --abort` |

## GitHub-Specific

**Clone a repo:**
```bash
git clone https://github.com/user/repo.git
```

**Add a remote:**
```bash
git remote add origin https://github.com/user/repo.git
```

**See remotes:**
```bash
git remote -v
```

**Create repo from existing folder:**
1. Create empty repo on GitHub (no README)
2. Then:
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/user/repo.git
git push -u origin main
```
