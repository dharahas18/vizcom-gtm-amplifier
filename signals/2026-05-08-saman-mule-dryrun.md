---
signal_type: community_moment
slug: 2026-05-08-saman-mule-dryrun
date: 2026-05-08
headline: "Andrew Moya and Juan Rujana's The Saman — a Pre-Columbian-inspired mule, designed in Vizcom and produced with Zellerfeld"
hero_render: ./renders/saman_hero.png
secondary_renders:
  - ./renders/saman_detail_amber.png
  - ./renders/saman_detail_veins.png
named_features: []
named_people: []
named_customers: []
named_partners:
  - name: Zellerfeld
    role: footwear 3D-printing production partner
named_designers:
  - name: Andrew Moya
    location: ""
    handle: ""
  - name: Juan Rujana
    location: ""
    handle: ""
designer_quotes: []
materials:
  - amber (color, echoing ancestral gold)
  - seashell shape (body form)
  - veins like tree roots (surface treatment)
  - sole
consent_to_amplify: true
confidential: false
customer_under_nda: false
posting_time: 2026-05-08T09:00:00-07:00
channels_to_skip: []
generated_by_intake: true
dry_run: true
dry_run_version: 2
notes: "Dry-run v2 — validates the optimized architecture (core_rules.md + lean templates). Loads ~3,500 words instead of ~30,000."
---

## Raw input

> "Andrew Moya and Juan Rujana designed The Saman — a mule rooted in Latino culture and Pre-Columbian artifacts. They drew from indigenous art of Central and South America: gold figures, ceremonial objects, primordial forms. The Amber color echoes ancestral gold. The seashell shapes the shoe itself. Veins run through the surface like tree roots — carrying through to the sole. Made with Zellerfeld. Hero render at /renders/saman_hero.png."

## Clarifications

1. **Signal type — community_moment vs. customer_win?**
   - Asked: "I see this could be a `community_moment` (designer feature) or a `customer_win` (Zellerfeld partnership). Which is closer?"
   - Answer: `community_moment` — the designers are the lead; Zellerfeld is named as a partner, not the headline.

2. **Designer handles?**
   - Asked: "Do you have Instagram or X handles for Andrew Moya and Juan Rujana?"
   - Answer: Not in initial input. Proceeding without; flagged for human to fill in before posting.

## Similarity check (Phase 0e)

Checked against `training/recent_topics.md` (last refresh: 2026-05-13).

- **R1** (same designer in last 30 days): no match. Andrew Moya and Juan Rujana have not been featured before.
- **R2** (same form-factor 3+ times in last 14 days): **MATCH** — mule features in last 14 days: Catapill (Apr 14), Digits (May 1). The Saman is the 3rd in 24 days.
  - User chose: **post anyway** (deliberate Hold Your Ideas + Zellerfeld series).
- **R3** (same feature in last 14 days): no match.
- **R4** (same signal_type in last 5 days): no match. Last community_moment was Digits (May 1, 7 days ago).
- **R5** (same campaign tag in last 7 days): **MATCH** — `HoldYourIdeas` posts: Digits.
  - User chose: **continue the series**.
- **R6** (same partner in last 14 days): **MATCH** — Zellerfeld named in Catapill (Apr 14).
  - User chose: **post anyway** (Zellerfeld is the recurring footwear partner).

Three matches fired. User chose to proceed on all three.

## Notes

This is dry-run v2. The expected outputs in `outputs/2026-05-08-saman-mule-dryrun/` are tested against Sample 12 T3 (X) and Sample 13 P1 (LinkedIn) — the real captured Vizcom posts for this exact signal — to verify the optimized system (core_rules.md + lean templates + 6-line corpus summaries) still produces a drop indistinguishable from what Vizcom actually shipped.
