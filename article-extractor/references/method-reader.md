# Method: reader (Mozilla Readability)

Best for most articles — based on Firefox Reader View. Outputs Markdown with the title as the first H1.

## Extract content

```bash
reader "URL" > article.txt
```

## Get title

```bash
TITLE=$(reader "URL" | head -n 1 | sed 's/^# //')
```

## Strengths

- Excellent clutter removal (ads, nav, sidebars)
- Preserves article structure (headings, paragraphs)
- Works on most news sites and blogs

## When to prefer over trafilatura

Use `reader` first; fall back to `trafilatura` only if `reader` is unavailable or returns empty output.
