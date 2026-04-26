# Method: Fallback (curl + Python HTML parser)

Use only when neither `reader` nor `trafilatura` is installed. Less reliable but dependency-free.

## Extract content

```bash
curl -s "URL" | python3 -c "
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
" > article.txt
```

## Get title

```bash
TITLE=$(curl -s "URL" | grep -oP '<title>\K[^<]+' | head -n 1)
TITLE=${TITLE%% - *}   # strip "- Site Name"
TITLE=${TITLE%% | *}   # strip "| Site Name"
```

## Limitations

- May include some noise (cookie banners, related-article boilerplate)
- Less accurate paragraph detection
- Will not work on JavaScript-rendered sites
- No metadata (author, publish date) extraction

Always show a preview and offer to retry with a real extractor if installable.
