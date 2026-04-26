---
name: dashboard-creator
description: Create HTML dashboards with KPI cards, bar/pie/line charts, progress indicators, and data tables. Use when asked to "create dashboard", "build KPI dashboard", "generate metrics visualization", "make analytics dashboard", "show performance dashboard", or "render data visualization as HTML".
---

# Dashboard Creator

Create interactive HTML dashboards with KPI cards and SVG charts.

## Contents

- [When to Use](#when-to-use)
- [Components](#components)
- [Workflow](#workflow)
- [HTML Skeleton](#html-skeleton)
- [KPI Card Pattern](#kpi-card-pattern)
- [SVG Bar Chart Pattern](#svg-bar-chart-pattern)
- [Verification](#verification)
- [References](#references)

## When to Use

- "Create dashboard for [metrics]"
- "Show KPI visualization"
- "Generate performance / analytics / monitoring dashboard"
- "Make HTML report with charts"

## Components

1. **KPI cards** — metric name, value, change %, trend icon
2. **Charts** — bar / pie / line as inline SVG (no external JS)
3. **Progress bars** — completion indicators
4. **Data tables** — tabular display

## Workflow

1. Extract metrics and structure the data
2. Build KPI cards grid
3. Generate SVG charts for each series
4. Add progress indicators where applicable
5. Write to `[name]-dashboard.html`
6. Verify (see [Verification](#verification))

Use semantic colors: green = positive, red = negative, blue = neutral.

## HTML Skeleton

```html
<!DOCTYPE html>
<html>
<head>
  <title>[Project] Dashboard</title>
  <style>
    body { font-family: system-ui; background: #f7fafc; }
    .kpi-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .kpi-value { font-size: 36px; font-weight: bold; }
    .trend-up { color: #48bb78; }
    .trend-down { color: #e53e3e; }
  </style>
</head>
<body>
  <h1>[Dashboard Name]</h1>
  <div class="grid">
    <!-- KPI cards, charts, progress bars -->
  </div>
</body>
</html>
```

## KPI Card Pattern

```html
<div class="kpi-card">
  <div class="kpi-label">Revenue</div>
  <div class="kpi-value">$124K</div>
  <div class="trend-up">↑ 12.5%</div>
</div>
```

## SVG Bar Chart Pattern

```html
<svg viewBox="0 0 400 300">
  <rect x="50" y="100" width="40" height="150" fill="#4299e1"/>
  <rect x="120" y="80" width="40" height="170" fill="#48bb78"/>
</svg>
```

## Verification

After writing the HTML file, confirm success by checking all of these:

- [ ] File exists at the target path and is non-empty
- [ ] Open in a browser — page renders without console errors
- [ ] Every KPI card shows a value (no empty `[PLACEHOLDER]` strings left in)
- [ ] Every SVG chart has bars/slices/lines proportional to the data (not all the same size)
- [ ] Trend colors match direction (green for positive deltas, red for negative)

If any check fails, fix before reporting completion.

## References

- [`references/design_patterns.md`](references/design_patterns.md) — color system, typography, component patterns
- [`references/svg_library.md`](references/svg_library.md) — SVG shapes, gradients, chart techniques
