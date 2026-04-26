# Troubleshooting

## Tool not installed

Try the next tool in the priority chain: `reader` → `trafilatura` → fallback. Offer install instructions only if the user asks (don't auto-install).

## Paywall or login required

Extraction tools cannot bypass auth. Tell the user: "This article requires authentication; cannot extract."

## Invalid URL

- Verify the URL format (`http://` or `https://` prefix)
- Try with and without trailing slashes
- Some tools handle redirects differently — try a direct URL if the canonical one fails

## No content extracted

Likely a JavaScript-rendered SPA. Try the fallback method as a sanity check; if that also returns empty, inform the user that the site requires a headless browser (out of scope for this skill).

## Special characters in title

When building the filename, strip or replace: `/`, `:`, `?`, `"`, `<`, `>`, `|`. See [`full-workflow.md`](full-workflow.md) for the exact `tr` chain.

## Output looks like noise

If the result includes navigation, ad copy, or related-article snippets:

- If you used `fallback` — try installing `reader` or `trafilatura`
- If you used `trafilatura` — re-run with `--precision`
- If you used `reader` — try `trafilatura` (different heuristics may handle this site better)
