---
name: error-fixer
description: Interpret error messages and fix common coding issues without technical knowledge. Use when user shares error messages, stack traces, console errors, build failures, or says things like "I got an error", "it's not working", "what does this mean", or pastes red text from their terminal or browser.
---

# Error Fixer

Translate scary error messages into plain English and actionable fixes.

## How to Use This Skill

When user shares an error:
1. Identify the error type (see patterns below)
2. Explain in one sentence what's wrong
3. Provide the fix command or action
4. Explain what the fix does (briefly)

## Common Error Patterns

### Module/Import Errors

**"Cannot find module 'X'" or "Module not found"**
- Meaning: A package isn't installed
- Fix: `npm install X` (replace X with the package name)

**"Cannot find module './components/Thing'"**
- Meaning: File path is wrong or file doesn't exist
- Fix: Check spelling, check if file exists, check capitalization

**"Module parse failed" or "You may need a loader"**
- Meaning: Trying to import a file type the bundler doesn't understand
- Fix: Install appropriate loader (e.g., css-loader, file-loader)

### Syntax Errors

**"Unexpected token" or "Parsing error"**
- Meaning: Typo in code — missing bracket, comma, quote
- Fix: Look at the line number mentioned, check for typos

**"X is not defined"**
- Meaning: Using a variable/function that doesn't exist
- Fix: Import it, define it, or check spelling

**"Unexpected end of input"**
- Meaning: Missing closing bracket, brace, or quote
- Fix: Check for unclosed `{`, `[`, `(`, or quotes

### React Errors

**"Invalid hook call"**
- Meaning: Hook used outside a component or in wrong order
- Fix: Move hooks to top of component, don't use in loops/conditions

**"Each child should have a unique key prop"**
- Meaning: List items need key attributes
- Fix: Add `key={uniqueId}` to each mapped element

**"Cannot read property 'X' of undefined"**
- Meaning: Trying to access something that doesn't exist yet
- Fix: Add optional chaining `?.` or check if data exists first

**"Too many re-renders"**
- Meaning: Component is updating itself in an infinite loop
- Fix: Check useEffect dependencies, don't call setState during render

**"Rendered more/fewer hooks than expected"**
- Meaning: Hooks are being called conditionally
- Fix: Move all hooks before any return statements or conditions

**"Hydration failed" or "Text content mismatch"**
- Meaning: Server HTML doesn't match client HTML (Next.js/SSR)
- Fix: Use `suppressHydrationWarning`, or check for browser-only code

### Next.js Errors

**"'next/router' should not be imported in app directory"**
- Meaning: Using old router in App Router
- Fix: Use `import { useRouter } from 'next/navigation'` instead

**"You're importing a component that needs useState..."**
- Meaning: Server component using client-only features
- Fix: Add `'use client'` at top of file

**"Dynamic server usage" or "cookies/headers"**
- Meaning: Using dynamic features in static context
- Fix: Add `export const dynamic = 'force-dynamic'` to page

### Tailwind Errors

**Styles not applying**
- Meaning: Class names not being detected
- Fix: Check `content` paths in tailwind.config.js include your files

**"Unknown at rule @tailwind"**
- Meaning: Editor doesn't recognize Tailwind
- Fix: Install Tailwind CSS IntelliSense extension, or ignore the warning

### Build/Compile Errors

**"ENOENT: no such file or directory"**
- Meaning: A file or folder is missing
- Fix: Check path, run `npm install` if it's in node_modules

**"EACCES: permission denied"**
- Meaning: No permission to access file/folder
- Fix: `sudo chown -R $USER ~/.npm` or use sudo

**"ENOMEM" or "JavaScript heap out of memory"**
- Meaning: Node ran out of memory
- Fix: Add `NODE_OPTIONS=--max-old-space-size=4096` before command

**"ERESOLVE unable to resolve dependency tree"**
- Meaning: Package version conflicts
- Fix: `npm install --legacy-peer-deps` or update conflicting packages

### Git Errors

**"fatal: not a git repository"**
- Meaning: Not in a git project folder
- Fix: `cd` to your project folder, or run `git init`

**"Your branch is behind"**
- Meaning: Others pushed changes you don't have
- Fix: `git pull`

**"Merge conflict"**
- Meaning: Same lines changed by two people
- Fix: Open the file, look for `<<<<<<<`, choose which version to keep

**"Permission denied (publickey)"**
- Meaning: SSH key not set up
- Fix: Add SSH key to GitHub, or use HTTPS URL instead

### Network/API Errors

**"CORS error" or "blocked by CORS policy"**
- Meaning: Server doesn't allow requests from your site
- Fix: Backend issue — add CORS headers, or use a proxy

**"401 Unauthorized"**
- Meaning: Bad or missing API key
- Fix: Check your .env file, verify API key is correct

**"403 Forbidden"**
- Meaning: Valid credentials but not allowed
- Fix: Check API permissions, rate limits, or subscription tier

**"404 Not Found"**
- Meaning: URL or endpoint doesn't exist
- Fix: Check the API URL, check spelling

**"429 Too Many Requests"**
- Meaning: Rate limited
- Fix: Wait and retry, add delays between requests

**"500 Internal Server Error"**
- Meaning: Server crashed — not your fault
- Fix: Check server logs, or wait and retry

**"ERR_CONNECTION_REFUSED"**
- Meaning: Server not running or wrong port
- Fix: Start the server, check the port number

### TypeScript Errors

**"Type 'X' is not assignable to type 'Y'"**
- Meaning: Wrong data type
- Fix: Cast it, fix the type, or use `as` assertion

**"Property 'X' does not exist on type 'Y'"**
- Meaning: Accessing something TypeScript doesn't know about
- Fix: Define the type, or use `(obj as any).X`

**"Object is possibly 'undefined'"**
- Meaning: Value might not exist
- Fix: Add `?.` or `!` (if you're sure it exists)

**"Cannot find name 'X'"**
- Meaning: TypeScript doesn't know about this global
- Fix: `npm install @types/X` or declare it

### Python Errors

**"ModuleNotFoundError: No module named 'X'"**
- Meaning: Package not installed
- Fix: `pip install X`

**"IndentationError"**
- Meaning: Inconsistent spaces/tabs
- Fix: Use consistent indentation (4 spaces recommended)

**"SyntaxError: invalid syntax"**
- Meaning: Typo — missing colon, bracket, or quote
- Fix: Check the line mentioned and the line before it

**"TypeError: 'NoneType' object is not subscriptable"**
- Meaning: Trying to access something that's None
- Fix: Check if variable has a value before accessing

## Quick Fixes Table

| Error Contains | Likely Fix |
|----------------|------------|
| "module not found" | `npm install <package>` |
| "ENOENT" | Check file path exists |
| "unexpected token" | Syntax error — check brackets/quotes |
| "is not defined" | Import or define the variable |
| "CORS" | Backend needs CORS headers |
| "401" | Check API key in .env |
| "port already in use" | `kill -9 $(lsof -t -i:3000)` |
| "cannot read property of undefined" | Add `?.` or null check |
| "heap out of memory" | Add `NODE_OPTIONS=--max-old-space-size=4096` |
| "hydration" | Add `'use client'` or `suppressHydrationWarning` |
| "too many re-renders" | Check useEffect deps, don't setState in render |

## When Error is Unclear

1. Copy the FIRST line of the error (usually the actual problem)
2. Look for a file path and line number
3. Google the exact error message in quotes
4. Or paste to AI with the relevant code file
5. Check if it's a known issue: search GitHub Issues
