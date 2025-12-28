---
name: code-explainer
description: Explain code in plain English for non-technical users. Use when user asks "what does this do", "explain this code", "I don't understand this", "what is happening here", or pastes code and wants to understand it without technical jargon.
---

# Code Explainer

Translate code into plain English using everyday analogies.

## How to Explain Code

When user shares code:
1. Start with a one-sentence summary of what it does overall
2. Break down into steps using everyday analogies
3. Avoid jargon — use comparisons to real-world things
4. Highlight what the user might want to change

## Analogy Library

Use these when explaining concepts:

### Variables
**Code:** `const name = "John"`
**Explain as:** "A labeled box that holds something. This box is labeled 'name' and contains 'John'."

**Code:** `let count = 0`
**Explain as:** "A whiteboard where you can erase and rewrite. Right now it says '0'."

### Functions
**Code:** `function greet(name) { return "Hello " + name }`
**Explain as:** "A recipe or machine. You put something in (name), it does something (adds 'Hello'), and gives you the result back."

### Arrow Functions
**Code:** `const add = (a, b) => a + b`
**Explain as:** "A shorthand recipe. Takes two numbers, adds them, gives you the answer. Same as a regular function, just shorter to write."

### If Statements
**Code:** `if (age >= 18) { ... }`
**Explain as:** "A decision point, like a bouncer at a club. If age is 18 or more, you get in. Otherwise, you don't."

### Ternary
**Code:** `const status = age >= 18 ? "adult" : "minor"`
**Explain as:** "A quick yes/no question. 'Is age 18 or more? If yes, write adult. If no, write minor.'"

### Loops
**Code:** `for (let i = 0; i < 5; i++) { ... }`
**Explain as:** "A repeat instruction. 'Do this 5 times' — like telling someone to knock on a door 5 times."

**Code:** `while (waiting) { ... }`
**Explain as:** "Keep doing this until something changes — like waiting in line until it's your turn."

### Arrays
**Code:** `const fruits = ["apple", "banana", "orange"]`
**Explain as:** "A numbered list. Position 0 is apple, position 1 is banana, position 2 is orange."

### Objects
**Code:** `const person = { name: "John", age: 30 }`
**Explain as:** "A form or profile card. This person card has a name field (John) and an age field (30)."

### Classes
**Code:** `class Dog { bark() { console.log("Woof!") } }`
**Explain as:** "A blueprint for creating things. This blueprint says 'every Dog can bark'. You can make many dogs from this blueprint."

### API Calls / Fetch
**Code:** `fetch('https://api.example.com/data')`
**Explain as:** "Sending a letter to another computer asking for information, then waiting for a reply."

### Async/Await
**Code:** `const data = await getData()`
**Explain as:** "Order coffee and wait at the counter. The 'await' is you waiting until the coffee is ready before continuing."

### Promises
**Code:** `.then(result => ...).catch(error => ...)`
**Explain as:** "A pinky promise. 'When you're done, then do this. But if something goes wrong, catch it and handle it.'"

### Try/Catch
**Code:** `try { ... } catch (error) { ... }`
**Explain as:** "Try to do this risky thing. If it fails, don't crash — just catch the problem and deal with it."

### Imports
**Code:** `import { Button } from './components'`
**Explain as:** "Borrowing a tool from another file. 'I need the Button tool from the components toolbox.'"

### Exports
**Code:** `export default function App() { ... }`
**Explain as:** "Making this available for others to borrow. 'Here, other files can use this App.'"

## React-Specific

### Props
**Code:** `<Button color="blue" />`
**Explain as:** "Settings or instructions you pass to a component. 'Make me a button, and make it blue.'"

### State
**Code:** `const [count, setCount] = useState(0)`
**Explain as:** "A whiteboard that the component can update. 'count' is what's on the board, 'setCount' is the eraser and marker to change it. When it changes, the screen updates."

### useEffect
**Code:** `useEffect(() => { ... }, [dependency])`
**Explain as:** "A side task that runs after the component appears. The stuff in brackets says 'only re-run this task if these things change.'"

**Code:** `useEffect(() => { ... }, [])` (empty array)
**Explain as:** "Run this once when the component first appears, then never again."

### useRef
**Code:** `const inputRef = useRef(null)`
**Explain as:** "A sticky note that points to something on the page. You can read or modify that thing directly."

### Context
**Code:** `const user = useContext(UserContext)`
**Explain as:** "A shared bulletin board. Any component in the app can read what's on this board without passing it down manually."

### Children
**Code:** `<Card>{children}</Card>`
**Explain as:** "A container that wraps around whatever you put inside it. Like a picture frame — the frame is the Card, and whatever's inside is the children."

## Common Patterns to Recognize

| Pattern | Plain English |
|---------|--------------|
| `.map()` | "Do this to each item in the list" |
| `.filter()` | "Keep only items that match this rule" |
| `.find()` | "Find the first item that matches" |
| `.reduce()` | "Combine all items into one result" |
| `.some()` | "Is there at least one that matches?" |
| `.every()` | "Do all of them match?" |
| `async/await` | "Do this, wait for result, then continue" |
| `try/catch` | "Try this, but if it fails, do this instead" |
| `?.` | "If this exists, then get this property" |
| `??` | "If empty/null, use this default instead" |
| `...spread` | "Copy everything from here" |
| `=>` | "Then do this" |
| `&&` | "If this is true, then show/do this" |
| `\|\|` | "Use this, or if empty, use that" |

## Explaining Patterns

### When explaining React components:
1. "This component is like a [real-world thing]..."
2. "It takes these settings: [props]..."
3. "It keeps track of: [state]..."
4. "When [trigger], it does [action]..."

### When explaining API code:
1. "This asks [service] for [what]..."
2. "It waits for the answer..."
3. "Then it does [action] with the result..."

### When explaining database code:
1. "This looks in the [collection/table] filing cabinet..."
2. "It finds all records where [condition]..."
3. "And returns [what fields]..."

### When explaining loops:
1. "For each [item] in [list]..."
2. "It does [action]..."
3. "Until it's gone through all of them."

## Tips for Explaining

- Start with the BIG PICTURE before details
- Use "imagine..." to set up analogies
- Point out what they CAN change vs what's structural
- If code is complex, explain it in layers
- Validate their confusion: "This is tricky because..."
- Use visual metaphors: boxes, lists, machines, recipes
- Relate to everyday tasks when possible
