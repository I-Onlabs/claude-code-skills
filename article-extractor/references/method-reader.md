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

## Quick example (one-shot)

```bash
reader "https://example.com/article" > temp.txt
TITLE=$(head -n 1 temp.txt | sed 's/^# //')
FILENAME="$(echo "$TITLE" | tr '/' '-').txt"
mv temp.txt "$FILENAME"
echo "Saved to: $FILENAME"
```

## With graceful fallback

```bash
if ! reader "$URL" > temp.txt 2>/dev/null; then
    if command -v trafilatura &> /dev/null; then
        trafilatura --URL "$URL" --output-format txt > temp.txt
    else
        echo "Error: install reader or trafilatura" >&2
        exit 1
    fi
fi
```
