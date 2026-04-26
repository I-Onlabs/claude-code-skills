# Installation

Check tool availability in priority order:

## Option 1: reader (recommended)

Mozilla's Readability algorithm — best general-purpose extractor.

```bash
command -v reader
```

If missing:

```bash
npm install -g @mozilla/readability-cli
# or
npm install -g reader-cli
```

## Option 2: trafilatura

Python-based, very accurate on news/blogs and non-English content.

```bash
command -v trafilatura
```

If missing:

```bash
pip3 install trafilatura
```

## Option 3: fallback

`curl` + a small inline Python HTML parser. Always available, less accurate. See [`method-fallback.md`](method-fallback.md).
