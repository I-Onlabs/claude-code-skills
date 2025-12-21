# Vibe Coding Methodology

**When to activate:** User describes aesthetic, mood, or visual feel for their application

**Core Principles:**
1. Vibe-first approach (aesthetic before implementation)
2. Structured prompting (Context → Objective → Vibe → Technical)
3. Iterative refinement (up to 5 cycles)
4. Vibe validation at every step

## Workflow

### Phase 1: Vibe Understanding

**Extract from user request:**
- Aesthetic style (cyberpunk, vaporwave, minimalist, retro, etc.)
- Mood descriptors (dreamy, sharp, electric, calm, etc.)
- Color preferences (explicit or implied)
- Animation feel (smooth, glitchy, instant, etc.)
- Interaction style (responsive, delayed, micro, etc.)

**Example:**
```
User: "Create a landing page with a startup vibe - clean, modern, trustworthy"

Vibe Extraction:
  - Aesthetic: minimalist
  - Mood: professional, trustworthy, modern
  - Colors: white/blue, subtle accents
  - Animations: subtle, micro-interactions
  - Interactions: smooth, purposeful
```

### Phase 2: Vibe Translation

**Map aesthetic to technical specs using the Vibe Translation Matrix:**

#### Cyberpunk
- **Colors:** Dark bg (#000), cyan (#00FFFF), magenta (#FF00FF)
- **Fonts:** Monaco, Courier New (monospace)
- **Animations:** glitch-effect, scan-lines, neon-glow
- **Interactions:** sharp, instant, electric
- **Components:** Angular borders, neon outlines

#### Vaporwave
- **Colors:** Purple-blue gradients, hot pink (#FF10F0)
- **Fonts:** VT323, Press Start 2P (retro)
- **Animations:** smooth-float, wave-motion, dreamy-fade
- **Interactions:** smooth, delayed, dreamy
- **Components:** Rounded, gradient outlines

#### Minimalist
- **Colors:** Black/white, subtle blue accent
- **Fonts:** Inter, SF Pro (clean sans-serif)
- **Animations:** subtle-fade, micro-interactions
- **Interactions:** understated, clear
- **Components:** Minimal borders, ample whitespace

#### Retro Game
- **Colors:** Neon green (#00FF00), red, yellow
- **Fonts:** VT323, Press Start 2P (pixel)
- **Animations:** pixel-blink, 8bit-bounce
- **Interactions:** clicky, arcade-style
- **Components:** Pixelated borders, terminal boxes

### Phase 3: Code Generation

**Generate code with vibe fully integrated:**

**For Frontend (React/TypeScript):**
```typescript
// Cyberpunk Example
<div className="bg-black border-2 border-cyan-500 shadow-lg shadow-cyan-500/50 p-6">
  <h1 className="text-cyan-400 font-mono text-2xl tracking-wider">
    {title}
  </h1>
  <div className="text-white font-mono animate-glitch">
    {content}
  </div>
</div>
```

**For Styling (Tailwind Config):**
```javascript
// Vaporwave Example
module.exports = {
  theme: {
    extend: {
      colors: {
        'vaporwave-pink': '#FF10F0',
        'vaporwave-purple': '#5B42F3',
        'vaporwave-cyan': '#00FFFF',
      },
      fontFamily: {
        'retro': ['VT323', 'monospace'],
      }
    }
  }
}
```

### Phase 4: Vibe Validation

**After generating code, validate:**
- ✅ Color palette matches vibe
- ✅ Typography aligns with aesthetic
- ✅ Animations match interaction feel
- ✅ Component styling consistent
- ✅ Overall feel matches user's vision

If validation fails, refine and regenerate.

## Integration with Claude Code

**Automatic Activation:**
When user mentions:
- Aesthetic terms: "cyberpunk", "vaporwave", "minimalist", "retro"
- Mood descriptors: "dreamy", "sharp", "clean", "glitchy"
- Visual requests: "neon colors", "gradients", "pixel art"
- Feel descriptions: "smooth animations", "instant feedback"

**Skill Synergy:**
- Combine with `frontend-design` for UI expertise
- Use with `project-context` for consistency
- Pair with `api-design-patterns` for full-stack vibe

## Prompt Templates

### Component Generation
```
Context: {project_type} with {existing_stack}
Objective: Create {component_type} for {feature}
Vibe: {aesthetic_style} - {mood_descriptors}
  Colors: {color_palette}
  Fonts: {typography}
  Animations: {animation_style}
  Interactions: {interaction_feel}
Technical: {language}, {framework}, {styling_approach}
```

## Best Practices

1. **Vibe-First, Then Technical**
   - Start with aesthetic description
   - Translate to technical specs
   - Then implement

2. **Consistency Throughout**
   - Apply vibe to ALL components
   - Maintain aesthetic across pages
   - Consistent interaction patterns

3. **Performance Matters**
   - 60fps animations
   - Optimized images
   - Lazy loading for heavy effects

4. **Accessibility Always**
   - WCAG AA compliance
   - Color contrast ratios
   - Keyboard navigation
   - Screen reader support

## Anti-Patterns to Avoid

❌ Mixing aesthetics inconsistently
❌ Ignoring performance for vibe
❌ Vibe over accessibility
❌ Generic implementation

## Success Criteria

✅ User can describe vibe in natural language
✅ Generated code matches aesthetic perfectly
✅ Consistent vibe across all components
✅ Performance optimized (60fps)
✅ Accessible (WCAG AA)
✅ User satisfaction: "That's exactly the vibe I wanted!"
