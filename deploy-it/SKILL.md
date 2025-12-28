---
name: deploy-it
description: Deployment patterns for Vercel, Netlify, Replit, Firebase Hosting, Railway, Render, and Cloudflare. Use when user wants to deploy, publish, go live, host a website, or mentions these platforms. Also use when troubleshooting deployment issues like "works locally but not deployed" or environment variable problems.
---

# Deploy It

Get your app live without the headache.

## Quick Comparison

| Platform | Best For | Free Tier | Deploy Command |
|----------|----------|-----------|----------------|
| **Vercel** | Next.js, React | Generous | `npx vercel` |
| **Netlify** | Static sites, JAMstack | Generous | `npx netlify deploy --prod` |
| **Railway** | Full-stack, databases | $5/month credit | `railway up` |
| **Render** | APIs, Docker, databases | Limited | Git push |
| **Cloudflare Pages** | Static, edge functions | Very generous | Git push |
| **Firebase** | Firebase projects | Limited | `firebase deploy` |
| **Replit** | Quick prototypes | Limited | Click Deploy |

## Vercel (Best for Next.js)

### First Time Setup
```bash
npm i -g vercel
vercel login
vercel
```

### Deploy Updates
```bash
vercel --prod
```

### Environment Variables
1. Go to vercel.com → Your project → Settings → Environment Variables
2. Add your variables
3. Redeploy (important!)

### Custom Domain
1. Settings → Domains → Add
2. Update DNS at your registrar

### vercel.json (optional config)
```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/" }],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "no-store" }]
    }
  ]
}
```

## Netlify

### First Time Setup
```bash
npm i -g netlify-cli
netlify login
netlify init
```

### Deploy
```bash
netlify deploy --prod
```

### Build Settings (netlify.toml)
```toml
[build]
  command = "npm run build"
  publish = "dist"  # or "build" or ".next" or "out"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Environment Variables
Site Settings → Build & deploy → Environment

## Railway (Full-Stack + Databases)

### First Time Setup
```bash
npm i -g @railway/cli
railway login
railway init
```

### Deploy
```bash
railway up
```

### Add Database
1. Dashboard → New → Database (Postgres, MySQL, Redis, MongoDB)
2. Variables are auto-added to your app

### Environment Variables
Dashboard → Variables → Add

## Render

### Deploy via GitHub
1. Connect GitHub repo
2. Choose Web Service or Static Site
3. Set build command: `npm run build`
4. Set start command: `npm start`

### Environment Variables
Dashboard → Environment → Add

### render.yaml (optional)
```yaml
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
```

## Cloudflare Pages (Fast + Free)

### Deploy via GitHub
1. Connect GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `dist` or `build` or `out`

### Environment Variables
Settings → Environment variables

### _redirects (for SPA)
```
/*    /index.html   200
```

## Firebase Hosting

### Setup
```bash
npm i -g firebase-tools
firebase login
firebase init hosting
```

### Deploy
```bash
npm run build
firebase deploy --only hosting
```

### firebase.json (SPA config)
```json
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      { "source": "**", "destination": "/index.html" }
    ]
  }
}
```

## Replit

1. Hit the **Deploy** button in your Replit
2. Choose deployment type (Static/Web Service)
3. Done

### Keeping it Running
For backends, you may need Replit's paid tier to keep it always-on.

## Common Deployment Problems

### "Works locally, broken on deploy"

**Check environment variables:**
- They must be set in the platform's dashboard
- Next.js: `NEXT_PUBLIC_` prefix for client-side vars
- Redeploy after adding env vars

**Check build output:**
- Make sure `npm run build` works locally first
- Check the build logs on the platform

### "404 on page refresh"

**SPA routing issue.** Add redirect rules:

Vercel (`vercel.json`):
```json
{ "rewrites": [{ "source": "/(.*)", "destination": "/" }] }
```

Netlify (`_redirects` in public folder):
```
/*    /index.html   200
```

### "API routes not working"

- Vercel: API routes work automatically for Next.js
- Netlify: Need Netlify Functions (different syntax)
- Cloudflare: Need Workers or Pages Functions
- Others: Need separate backend deployment

### "Build failed"

1. Check build logs (platform dashboard)
2. Run `npm run build` locally to see the error
3. Common issues:
   - Missing dependencies (add to package.json)
   - TypeScript errors
   - Missing env vars (undefined at build time)
   - Case sensitivity (Linux servers are case-sensitive)

### "Site shows old version"

- Clear CDN cache (usually in dashboard)
- Hard refresh browser: Cmd+Shift+R
- Check if deployment actually completed

### "CORS errors"

- Backend and frontend on different domains
- Add CORS headers to your API
- Or use same-origin deployment

## Pre-Deploy Checklist

- [ ] `npm run build` works locally
- [ ] All environment variables documented
- [ ] API keys NOT in code (use env vars)
- [ ] `console.log` statements cleaned up
- [ ] Error handling in place
- [ ] Loading states for async operations
- [ ] Mobile responsive

## Which Platform?

**Use Vercel if:** Next.js project, want easiest experience

**Use Netlify if:** Static site, JAMstack, want forms/functions

**Use Railway if:** Need a database, full-stack app

**Use Render if:** Need Docker, cron jobs, background workers

**Use Cloudflare if:** Want speed, generous free tier, edge functions

**Use Firebase if:** Already using Firebase backend

**Use Replit if:** Quick prototype, want to share link fast

## Environment Variable Cheat Sheet

| Framework | Client-side prefix | Server-side |
|-----------|-------------------|-------------|
| Next.js | `NEXT_PUBLIC_` | No prefix |
| Vite | `VITE_` | No prefix |
| Create React App | `REACT_APP_` | N/A |
| SvelteKit | `PUBLIC_` | No prefix |
