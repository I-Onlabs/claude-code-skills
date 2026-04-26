# Full Workflow Script

End-to-end extraction with auto-detection and filename cleanup.

```bash
ARTICLE_URL="https://example.com/article"

# Detect available tool
if command -v reader &> /dev/null; then
    TOOL="reader"
elif command -v trafilatura &> /dev/null; then
    TOOL="trafilatura"
else
    TOOL="fallback"
fi
echo "Using $TOOL"

case $TOOL in
    reader)
        reader "$ARTICLE_URL" > temp_article.txt
        TITLE=$(head -n 1 temp_article.txt | sed 's/^# //')
        ;;
    trafilatura)
        METADATA=$(trafilatura --URL "$ARTICLE_URL" --json)
        TITLE=$(echo "$METADATA" | python3 -c "import json, sys; print(json.load(sys.stdin).get('title', 'Article'))")
        trafilatura --URL "$ARTICLE_URL" --output-format txt --no-comments > temp_article.txt
        ;;
    fallback)
        TITLE=$(curl -s "$ARTICLE_URL" | grep -oP '<title>\K[^<]+' | head -n 1)
        TITLE=${TITLE%% - *}
        TITLE=${TITLE%% | *}
        # See method-fallback.md for the inline Python parser
        curl -s "$ARTICLE_URL" | python3 ARTICLE_PARSER.py > temp_article.txt
        ;;
esac

# Clean filename for filesystem
FILENAME=$(echo "$TITLE" \
  | tr '/' '-' | tr ':' '-' | tr -d '?"<>' | tr '|' '-' \
  | cut -c 1-80 | sed 's/ *$//' | sed 's/^ *//')
FILENAME="${FILENAME}.txt"

mv temp_article.txt "$FILENAME"

echo "✓ Extracted: $TITLE"
echo "✓ Saved to:  $FILENAME"
echo ""
echo "Preview:"
head -n 10 "$FILENAME"
```

## Filename cleanup rules

Remove or replace characters illegal on common filesystems:

| Char | Action |
|---|---|
| `/` | replace with `-` |
| `:` | replace with `-` |
| `?` `"` `<` `>` | delete |
| `|` | replace with `-` |

Truncate to 80 characters and trim trailing spaces. Append `.txt`.
