---
name: firebase-buddy
description: Firebase patterns and troubleshooting for vibecoders. Use when user mentions Firebase, Firestore, Firebase Auth, Firebase hosting, security rules, or is working on projects using Firebase backend. Also use for errors like "permission denied", "missing index", or authentication issues in Firebase projects.
---

# Firebase Buddy

Common Firebase patterns without the complexity.

## Quick Setup Checklist

1. **Install Firebase:**
   ```bash
   npm install firebase
   ```

2. **Create config file** (`lib/firebase.js` or `firebase.ts`):
   ```javascript
   import { initializeApp } from 'firebase/app';
   import { getFirestore } from 'firebase/firestore';
   import { getAuth } from 'firebase/auth';
   import { getStorage } from 'firebase/storage';

   const firebaseConfig = {
     apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
     authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
     projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
     storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
     messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
     appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
   };

   const app = initializeApp(firebaseConfig);
   export const db = getFirestore(app);
   export const auth = getAuth(app);
   export const storage = getStorage(app);
   ```

3. **Create `.env.local`:**
   ```
   NEXT_PUBLIC_FIREBASE_API_KEY=your-key
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project
   NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456
   NEXT_PUBLIC_FIREBASE_APP_ID=1:123:web:abc
   ```

## Firestore Patterns

### Read Data
```javascript
import { doc, getDoc, collection, getDocs, query, where, orderBy, limit } from 'firebase/firestore';
import { db } from './firebase';

// Get one document
const docSnap = await getDoc(doc(db, 'users', 'userId'));
if (docSnap.exists()) {
  console.log(docSnap.data());
}

// Get all documents in collection
const querySnapshot = await getDocs(collection(db, 'users'));
querySnapshot.forEach((doc) => {
  console.log(doc.id, doc.data());
});

// Query with filters
const q = query(
  collection(db, 'posts'),
  where('author', '==', 'userId'),
  orderBy('createdAt', 'desc'),
  limit(10)
);
const results = await getDocs(q);
```

### Write Data
```javascript
import { doc, setDoc, addDoc, updateDoc, deleteDoc, collection, serverTimestamp } from 'firebase/firestore';
import { db } from './firebase';

// Set with specific ID
await setDoc(doc(db, 'users', 'userId'), {
  name: 'John',
  email: 'john@example.com',
  createdAt: serverTimestamp()
});

// Add with auto-generated ID
const docRef = await addDoc(collection(db, 'users'), {
  name: 'Jane',
  email: 'jane@example.com'
});
console.log('New doc ID:', docRef.id);

// Update specific fields
await updateDoc(doc(db, 'users', 'userId'), {
  name: 'John Updated'
});

// Delete
await deleteDoc(doc(db, 'users', 'userId'));
```

### Real-time Listener
```javascript
import { doc, collection, onSnapshot, query, where } from 'firebase/firestore';
import { db } from './firebase';

// Listen to one document
const unsubscribe = onSnapshot(doc(db, 'users', 'userId'), (doc) => {
  console.log('Current data:', doc.data());
});

// Listen to collection with query
const q = query(collection(db, 'messages'), where('roomId', '==', 'room1'));
const unsubscribe = onSnapshot(q, (snapshot) => {
  snapshot.forEach((doc) => {
    console.log(doc.data());
  });
});

// Call unsubscribe() to stop listening (important for cleanup!)
```

### React Hook Pattern
```javascript
import { useState, useEffect } from 'react';
import { doc, onSnapshot } from 'firebase/firestore';
import { db } from './firebase';

function useDocument(collectionName, docId) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onSnapshot(doc(db, collectionName, docId), (doc) => {
      setData(doc.exists() ? { id: doc.id, ...doc.data() } : null);
      setLoading(false);
    });
    return unsubscribe; // cleanup on unmount
  }, [collectionName, docId]);

  return { data, loading };
}
```

## Authentication

### Email/Password
```javascript
import { 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword, 
  signOut,
  onAuthStateChanged 
} from 'firebase/auth';
import { auth } from './firebase';

// Sign up
const userCredential = await createUserWithEmailAndPassword(auth, email, password);
const user = userCredential.user;

// Sign in
await signInWithEmailAndPassword(auth, email, password);

// Sign out
await signOut(auth);

// Listen to auth state
onAuthStateChanged(auth, (user) => {
  if (user) {
    console.log('Logged in:', user.uid);
  } else {
    console.log('Logged out');
  }
});
```

### Google Sign-In
```javascript
import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
import { auth } from './firebase';

const provider = new GoogleAuthProvider();
const result = await signInWithPopup(auth, provider);
const user = result.user;
```

### Auth Context (React)
```javascript
import { createContext, useContext, useEffect, useState } from 'react';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from './firebase';

const AuthContext = createContext({});

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });
    return unsubscribe;
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

## Storage (File Uploads)

```javascript
import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';
import { storage } from './firebase';

// Upload file
const storageRef = ref(storage, `uploads/${file.name}`);
await uploadBytes(storageRef, file);

// Get download URL
const url = await getDownloadURL(storageRef);
console.log('File URL:', url);
```

## Common Errors & Fixes

| Error | Meaning | Fix |
|-------|---------|-----|
| "permission-denied" | Security rules blocking access | Update Firestore rules (see below) |
| "not-found" | Document doesn't exist | Check path, check if data exists |
| "unauthenticated" | User not logged in | Sign in first, or update rules |
| "missing index" | Query needs an index | Click link in error to create index |
| "quota exceeded" | Free tier limit hit | Wait or upgrade plan |
| "invalid-argument" | Wrong data type or format | Check your data matches expected types |
| "already-exists" | Trying to create existing doc | Use `setDoc` with merge, or update |

## Security Rules Quick Reference

**Development (allow everything — NOT for production):**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```

**Allow authenticated users only:**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

**Users can only access their own data:**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /users/{userId}/posts/{postId} {
      allow read: if true;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

## Firebase CLI

```bash
# Install
npm install -g firebase-tools

# Login
firebase login

# Initialize project
firebase init

# Deploy rules
firebase deploy --only firestore:rules

# Deploy hosting
firebase deploy --only hosting

# View logs
firebase functions:log
```

## Debugging Tips

1. **Check the Firebase Console** — see actual data and errors
2. **Check auth state** — `console.log(auth.currentUser)`
3. **Check network tab** — see actual requests/responses
4. **Rules Playground** — test rules in Firebase Console
5. **Restart dev server** after changing `.env.local`
6. **Check indexes** — Firestore → Indexes in console
7. **Use emulators** — `firebase emulators:start` for local testing
