---
name: project-starter
description: Templates for starting new projects with common stacks. Use when user wants to "start a new project", "create an app", "build something from scratch", or asks about project setup, folder structure, or boilerplate code. Covers Next.js, React, Node.js, Python, and mobile.
---

# Project Starter

Get coding fast with ready-to-go project templates.

## Quick Start Commands

| Stack | Command |
|-------|---------|
| Next.js (React) | `npx create-next-app@latest my-app` |
| React (Vite) | `npm create vite@latest my-app -- --template react-ts` |
| Node.js API | `mkdir my-api && cd my-api && npm init -y` |
| Python FastAPI | `mkdir my-api && cd my-api && python -m venv venv` |
| Expo (React Native) | `npx create-expo-app my-app` |
| Electron | `npm init electron-app@latest my-app` |

## Next.js (Recommended for Web Apps)

```bash
npx create-next-app@latest my-app
cd my-app
npm run dev
```

**Say YES to:**
- TypeScript (catches errors)
- ESLint (code quality)
- Tailwind CSS (easy styling)
- App Router (newer, better)
- `src/` directory (cleaner)

**Folder Structure:**
```
my-app/
├── src/
│   ├── app/              # Pages and routes
│   │   ├── page.tsx      # Home page (/)
│   │   ├── layout.tsx    # Shared layout
│   │   ├── globals.css   # Global styles
│   │   └── api/          # Backend routes
│   ├── components/       # Reusable UI
│   └── lib/              # Utilities, configs
├── public/               # Static files
└── .env.local            # Environment variables
```

**Add shadcn/ui (great components):**
```bash
npx shadcn@latest init
npx shadcn@latest add button card input
```

## React with Vite (Lighter Alternative)

```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npm run dev
```

**Add Tailwind:**
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Add to `tailwind.config.js`:
```javascript
content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
```

Add to `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Node.js API (Backend)

```bash
mkdir my-api
cd my-api
npm init -y
npm install express cors dotenv
```

**Create `index.js`:**
```javascript
import express from 'express';
import cors from 'cors';
import 'dotenv/config';

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Hello!' });
});

app.get('/api/users', (req, res) => {
  res.json([{ id: 1, name: 'John' }]);
});

app.post('/api/users', (req, res) => {
  const { name } = req.body;
  res.json({ id: 2, name });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

**Add to `package.json`:**
```json
{
  "type": "module",
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js"
  }
}
```

## Python FastAPI

```bash
mkdir my-project
cd my-project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn python-dotenv
```

**Create `main.py`:**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello!"}

@app.get("/api/users")
def get_users():
    return [{"id": 1, "name": "John"}]

# Run with: uvicorn main:app --reload
```

**Create `requirements.txt`:**
```
fastapi
uvicorn
python-dotenv
```

## Expo (React Native Mobile)

```bash
npx create-expo-app my-app
cd my-app
npx expo start
```

**Scan QR code with Expo Go app on your phone.**

**Add navigation:**
```bash
npx expo install expo-router react-native-screens react-native-safe-area-context
```

## Essential First Steps (All Projects)

### 1. Initialize git
```bash
git init
git add .
git commit -m "initial commit"
```

### 2. Create `.env.local` (add to `.gitignore`)
```
API_KEY=your-secret-key
DATABASE_URL=your-db-url
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### 3. Install common packages

**React/Next.js:**
```bash
# State management
npm install zustand

# Data fetching
npm install @tanstack/react-query

# Forms
npm install react-hook-form zod @hookform/resolvers

# Icons
npm install lucide-react
```

**Backend:**
```bash
npm install express cors dotenv
npm install -D nodemon
```

## Common Additions

**Firebase:**
```bash
npm install firebase
```

**Supabase:**
```bash
npm install @supabase/supabase-js
```

**Authentication (NextAuth):**
```bash
npm install next-auth
```

**Database (Prisma):**
```bash
npm install prisma @prisma/client
npx prisma init
```

**Date handling:**
```bash
npm install date-fns
```

**Animation:**
```bash
npm install framer-motion
```

## Project Templates (Starter Kits)

**Next.js + Supabase + Auth:**
```bash
npx create-next-app -e with-supabase
```

**T3 Stack (Next.js + tRPC + Prisma + Tailwind):**
```bash
npm create t3-app@latest
```

**Remix:**
```bash
npx create-remix@latest
```

## Which Stack to Choose?

| Need | Best Choice |
|------|-------------|
| Full web app with pages | Next.js |
| Simple UI, no backend | React + Vite |
| API/backend only | Node.js + Express or Python + FastAPI |
| Mobile app | Expo (React Native) |
| Desktop app | Electron |
| Quick prototype | Replit or v0.dev |
| Real-time features | Supabase or Firebase |
| E-commerce | Next.js + Stripe |
| Blog/CMS | Next.js + MDX or Sanity |
