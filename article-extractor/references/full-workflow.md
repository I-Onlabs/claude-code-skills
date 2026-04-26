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
        # Portable across BSD/GNU grep (avoid grep -oP)
        TITLE=$(curl -s "$ARTICLE_URL" \
          | sed -n 's|.*<title[^>]*>\([^<]*\)</title>.*|\1|p' \
          | head -n 1)
        TITLE=${TITLE%% - *}
        TITLE=${TITLE%% | *}
        curl -s "$ARTICLE_URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags and tag in {'p', 'article', 'main', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.in_content = True

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > temp_article.txt
        ;;
esac

# Fallback if title extraction failed
[ -z "$TITLE" ] && TITLE="article"

# Clean filename for filesystem
FILENAME=$(echo "$TITLE" \
  | tr '/' '-' | tr ':' '-' | tr -d '?"<>' | tr '|' '-' \
  | cut -c 1-80 | sed 's/ *$//' | sed 's/^ *//')
[ -z "$FILENAME" ] && FILENAME="article"
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
