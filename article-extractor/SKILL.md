---
name: article-extractor
description: Extract clean article content from a URL (blog post, news article, tutorial) and save it as readable text with ads, navigation, and other clutter removed. Use when asked to "extract article", "scrape text from URL", "download blog post", "parse HTML article", "save article as text", or "clean article content from a webpage".
allowed-tools:
  - Bash
  - Write
---

# Article Extractor

Extracts the main content from web articles and blog posts, removes navigation, ads, newsletter signups, and other clutter, and saves the result as clean readable text.

## Contents

- [When to Use](#when-to-use)
- [Priority Order](#priority-order)
- [Quick Examples](#quick-examples)
- [Verification](#verification)
- [References](#references)

## When to Use

Activate when the user:

- Provides an article/blog URL and wants the text content
- Says "download this article", "extract content from [URL]", or "save this blog post as text"
- Needs clean article text without distractions

## Priority Order

1. Detect available tool: `reader` → `trafilatura` → fallback
2. Extract content with the best available tool
3. Extract title for filename
4. Clean filename for filesystem (strip illegal chars, cap length)
5. Save to `[clean-title].txt`
6. Show preview and verify (see [Verification](#verification))

See [`references/installation.md`](references/installation.md) for tool detection and install commands.

## Quick Examples

**reader** (recommended):

```bash
reader "URL" > article.txt
TITLE=$(head -n 1 article.txt | sed 's/^# //')
```

**trafilatura** (best for news/non-English):

```bash
trafilatura --URL "URL" --output-format txt --no-comments > article.txt
```

**fallback** (no dependencies):

See [`references/method-fallback.md`](references/method-fallback.md) — uses `curl` + a small inline Python parser.

For the full auto-detect + filename-cleanup script, see [`references/full-workflow.md`](references/full-workflow.md).

## Output Contract

The saved file should contain:

- Article title (when the tool reports one)
- Author and publish date (when available — `trafilatura` JSON, sometimes `reader`)
- Main article text with section headings preserved

The saved file should **not** contain:

- Navigation menus, headers, footers
- Ads and promotional content
- Newsletter signup forms
- Related-articles sidebars
- Cookie / consent banners
- Social-media buttons
- Comment sections (suppress with `trafilatura --no-comments`)

If the output contains any of the above, the extractor either picked the wrong method or the site is hostile to extraction (heavy JS, anti-scraping). Retry with the next tool in the priority chain or surface the failure.

## Verification

After extraction, confirm all of:

- [ ] Output file exists and is non-empty
- [ ] First 10 lines look like article prose, not nav/ads/cookie banners (matches the Output Contract above)
- [ ] Title was extracted (filename is meaningful, not `Article.txt`)
- [ ] Filename has no illegal characters (`/`, `:`, `?`, `"`, `<`, `>`, `|`)
- [ ] Show the preview to the user (first 10–15 lines). The standard report is: extracted title, save path, file size, then preview.

If the site is a JavaScript SPA or requires authentication, all extractors will fail — tell the user explicitly rather than saving empty output.

## References

- [`references/installation.md`](references/installation.md) — tool detection and install
- [`references/method-reader.md`](references/method-reader.md) — `reader` (Mozilla Readability)
- [`references/method-trafilatura.md`](references/method-trafilatura.md) — `trafilatura` flags and use cases
- [`references/method-fallback.md`](references/method-fallback.md) — `curl` + Python fallback parser
- [`references/full-workflow.md`](references/full-workflow.md) — complete end-to-end script
- [`references/troubleshooting.md`](references/troubleshooting.md) — paywall, JS SPAs, noisy output, edge cases
