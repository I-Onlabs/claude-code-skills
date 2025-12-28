---
name: api-connector
description: Patterns for connecting to external APIs like Stripe, OpenAI, Anthropic, Supabase, Replicate, and others. Use when user wants to integrate a third-party service, asks about API keys, authentication, making HTTP requests, or is troubleshooting API connection issues like CORS, 401, 403, or rate limits.
---

# API Connector

Hook up external services without getting lost in docs.

## Universal Pattern

Every API connection follows the same shape:

```javascript
const response = await fetch('https://api.example.com/endpoint', {
  method: 'POST',  // or GET, PUT, DELETE
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.API_KEY}`
  },
  body: JSON.stringify({ your: 'data' })
});

const data = await response.json();
```

## Environment Variables

**Never put API keys in code.** Use `.env.local`:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
STRIPE_SECRET_KEY=sk_test_...
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJ...
REPLICATE_API_TOKEN=r8_...
```

Access them:
- Node/Backend: `process.env.API_KEY`
- Next.js Client: `process.env.NEXT_PUBLIC_API_KEY` (prefix required)
- Vite Client: `import.meta.env.VITE_API_KEY`

## AI APIs

### OpenAI
```javascript
const response = await fetch('https://api.openai.com/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
  },
  body: JSON.stringify({
    model: 'gpt-4o',
    messages: [{ role: 'user', content: 'Hello!' }]
  })
});
const data = await response.json();
console.log(data.choices[0].message.content);
```

### Anthropic/Claude
```javascript
const response = await fetch('https://api.anthropic.com/v1/messages', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': process.env.ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01'
  },
  body: JSON.stringify({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 1024,
    messages: [{ role: 'user', content: 'Hello!' }]
  })
});
const data = await response.json();
console.log(data.content[0].text);
```

### Groq (Fast Inference)
```javascript
const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.GROQ_API_KEY}`
  },
  body: JSON.stringify({
    model: 'llama-3.1-70b-versatile',
    messages: [{ role: 'user', content: 'Hello!' }]
  })
});
```

### Replicate (Image/Audio/Video Models)
```javascript
const response = await fetch('https://api.replicate.com/v1/predictions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Token ${process.env.REPLICATE_API_TOKEN}`
  },
  body: JSON.stringify({
    version: 'model-version-id',
    input: { prompt: 'A photo of a cat' }
  })
});
// Poll for result using returned URLs
```

### Together AI
```javascript
const response = await fetch('https://api.together.xyz/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.TOGETHER_API_KEY}`
  },
  body: JSON.stringify({
    model: 'meta-llama/Llama-3-70b-chat-hf',
    messages: [{ role: 'user', content: 'Hello!' }]
  })
});
```

## Payment & Commerce

### Stripe (Backend Only!)
```javascript
import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

// Create payment intent
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,  // in cents ($10.00)
  currency: 'usd'
});

// Create checkout session
const session = await stripe.checkout.sessions.create({
  payment_method_types: ['card'],
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: { name: 'Product' },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  mode: 'payment',
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
});
```

## Database Services

### Supabase
```javascript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_KEY
);

// Query data
const { data, error } = await supabase
  .from('users')
  .select('*')
  .eq('status', 'active');

// Insert data
const { data, error } = await supabase
  .from('users')
  .insert({ name: 'John', email: 'john@example.com' });

// Auth
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password'
});
```

### Upstash Redis
```javascript
import { Redis } from '@upstash/redis';

const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL,
  token: process.env.UPSTASH_REDIS_REST_TOKEN,
});

await redis.set('key', 'value');
const value = await redis.get('key');
```

## Communication

### Resend (Email)
```javascript
import { Resend } from 'resend';
const resend = new Resend(process.env.RESEND_API_KEY);

await resend.emails.send({
  from: 'you@yourdomain.com',
  to: 'user@example.com',
  subject: 'Hello',
  html: '<p>Hi there!</p>'
});
```

### Twilio (SMS)
```javascript
import twilio from 'twilio';
const client = twilio(
  process.env.TWILIO_ACCOUNT_SID, 
  process.env.TWILIO_AUTH_TOKEN
);

await client.messages.create({
  body: 'Hello!',
  from: '+1234567890',
  to: '+0987654321'
});
```

## Common Errors

| Error | Meaning | Fix |
|-------|---------|-----|
| 401 Unauthorized | Bad/missing API key | Check key is correct, check env var name |
| 403 Forbidden | Key valid but not allowed | Check API permissions/scopes |
| 429 Too Many Requests | Rate limited | Add delays, or upgrade plan |
| CORS Error | Browser blocking request | Call API from backend, not frontend |
| Network Error | Can't reach API | Check URL, check internet |
| 400 Bad Request | Malformed request | Check request body format |
| 500 Server Error | API is down | Wait and retry |

## Frontend vs Backend

**Call from BACKEND when:**
- API key is secret (Stripe, OpenAI, Anthropic)
- Processing payments
- Sensitive operations
- API doesn't support CORS

**Call from FRONTEND when:**
- API allows it (Supabase, Firebase)
- Key is meant to be public
- Real-time updates needed

### Create API Route (Next.js App Router)
```javascript
// app/api/chat/route.js
export async function POST(request) {
  const { message } = await request.json();
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4o',
      messages: [{ role: 'user', content: message }]
    })
  });
  
  const data = await response.json();
  return Response.json(data);
}
```

### Create API Route (Next.js Pages Router)
```javascript
// pages/api/chat.js
export default async function handler(req, res) {
  const { message } = req.body;
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4o',
      messages: [{ role: 'user', content: message }]
    })
  });
  
  const data = await response.json();
  res.json(data);
}
```

## Debugging Tips

1. **Log the response:** `console.log(await response.text())`
2. **Check status code:** `console.log(response.status)`
3. **Test in Postman/Insomnia first** before coding
4. **Read the error message** — APIs usually tell you what's wrong
5. **Check rate limits** — most APIs have dashboards showing usage
6. **Verify env vars loaded:** `console.log(process.env.API_KEY?.slice(0,10))`
