# Method: trafilatura

Python-based extractor. Very accurate, handles complex layouts and non-English content.

## Extract content

```bash
trafilatura --URL "URL" --output-format txt > article.txt
```

With recommended cleanup options:

```bash
trafilatura --URL "URL" --output-format txt --no-comments --no-tables > article.txt
```

## Get title

```bash
TITLE=$(trafilatura --URL "URL" --json \
  | python3 -c "import json, sys; print(json.load(sys.stdin)['title'])")
```

## Useful flags

| Flag | Effect |
|---|---|
| `--no-comments` | Skip comment sections |
| `--no-tables` | Skip data tables |
| `--precision` | Favor precision over recall |
| `--recall` | Extract more content (may include some noise) |

## When to prefer

- Academic articles
- News sites with complex layouts
- Non-English content
- Sites where `reader` returns partial output
