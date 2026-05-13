# `renders/` — Hero and supporting images for each signal

The agent references hero renders from this folder. Each signal's renders live in a subfolder named with the signal slug.

```
renders/
└── {signal_slug}/
    ├── hero.jpg          ← required (used as the hero render on blog, LinkedIn, X)
    ├── detail-{name}.jpg ← optional secondary renders for the blog body
    └── (any other supporting assets)
```

The agent's intake step validates that `renders/{signal_slug}/hero.jpg` (or `.png`/`.webp`) exists before drafting. If it doesn't, the agent halts and asks the human to drop the render in.

When the agent finalizes a drop, it copies the renders into `outputs/{signal_slug}/` so the drop folder is self-contained and the publisher can drag-and-drop from one location.

---

## Source of the current images

The images currently in this folder were pulled from Vizcom's public blog CDN (`cdn.prod.website-files.com`) as placeholder/presentation assets. They are real Vizcom-rendered images from published blog posts:

| File | Source post |
|---|---|
| `2026-05-08-saman-mule-dryrun/hero.jpg` | "Hold Your Ideas: The Exhaust Light" (Mar 2026) |
| `2026-05-08-saman-mule-dryrun/detail-amber.jpg` | "Make It Real: Fabracers" (Jan 2026) |
| `2026-05-08-saman-mule-dryrun/detail-veins.jpg` | "Most Ideas Die in Sketchbooks" (Apr 2026) |
| `01-product-launch-smart-dropper/hero.jpg` | "Introducing Extract, Try On & Export" (Mar 2026) |
| `02-community-moment-velocity-skateboard/hero.jpg` | "Make It Real: Fabracers" (Jan 2026) |
| `02-community-moment-velocity-skateboard/detail.jpg` | "Hold Your Ideas: The Exhaust Light" (Mar 2026) |
| `03-customer-win-honda/hero.jpg` | "Announcing our $27M Series B" (Oct 2025) |
| `04-milestone-one-million-designers/hero.jpg` | "2025 Year in Review" (Dec 2025) |
| `05-event-design-week-amsterdam/hero.jpg` | "Meet the new Vizcom Studio" (Nov 2025) |

They are matched to each sample by **register**, not subject — e.g., the customer-win sample uses Series-B imagery (high-stakes corporate announcement register), the milestone sample uses Year-in-Review imagery (community-celebration register).

**For real signals**, swap these placeholders for renders that actually depict the signal's subject: the actual product for product launches, the actual designer's work for community moments, the actual customer's render for customer wins.

---

## Naming convention

- Lowercase, hyphenated slug matching the signal file: `2026-05-13-smart-dropper-launch/hero.jpg`
- Hero render: always `hero.jpg` or `hero.png` or `hero.webp`
- Secondary renders: `detail-{descriptor}.jpg` — e.g., `detail-amber.jpg`, `detail-back-panel.jpg`
- Aspect ratios: hero should be landscape ≥1500×800 for cross-channel use. The publisher crops per-channel.
- File size: <500 KB per render for portability; up to 2 MB acceptable for blog heroes that need detail.

---

## When the agent halts asking for a render

The chat message will look something like:

> "I need a hero render at `renders/{slug}/hero.jpg` before I can draft this. Drop one in and re-run: `Run vizcom-gtm-amplifier on signals/{slug}.md`"

When that happens: put the right render in the named folder, then re-run. The agent picks up where it left off.
