# Sample 3 — Customer win (Honda)

**Signal type:** `customer_win`
**Input style:** Slack-message style with embedded quote
**What it tests:** NDA-clearance question (Fortune-500 customer), designer-at-customer specificity, multi-feature workflow (Studio + Modify + Animate)

**Run with:**
```
Run vizcom-gtm-amplifier on samples/03-customer-win-honda.md
```

---

[from #vizcom-customers, posted by Sophia]

Heads up — Honda's interior-design team has been using Vizcom for 9 months on the next-gen Civic concept. Hiroshi Tanaka (their design lead in Tochigi) did a webinar with us last Thursday walking through the workflow:

- Studio for early ideation — full-bleed canvas, no template constraints
- Modify for material exploration — they tested 30+ interior fabric combinations
- Animate for stakeholder walkthroughs — replaces the 3-week pre-visualization cycle they used to do

Hiroshi cleared this quote (his comms team signed off Tuesday):

> "Vizcom collapses the gap between sketch and review. We're presenting to the executive design team with renders that used to take a week. The decision velocity has changed how we work."
— Hiroshi Tanaka, Senior Designer, Honda

Numbers Hiroshi shared:
- Pre-Vizcom: ~3 design reviews per quarter
- With Vizcom: ~11 design reviews per quarter
- Concept-to-review time: 7 days → 2 days

Hero render: samples/renders/honda_civic_interior.png
Webinar recording: https://vizcom.com/events/honda-webinar-2026
Honda's PR has cleared us to name them publicly. (Confirmation in /Users/sophia/inbox/honda-pr-confirm.eml)

— Sophia

---

**What the agent should ask:**

1. **Customer NDA status:** Honda is on the allowed list, but the agent should still confirm "Honda is cleared to name publicly?" — the input says yes, so this should resolve quickly.
2. **Designer quote clearance:** Hiroshi's quote is explicitly cleared.
3. **Specific designer vs. team-level credit:** Hiroshi is named — agent should ask whether to feature him personally or keep at "Honda interior-design team." Recommended: name Hiroshi (the quote is cleared and he's the protagonist).
4. Similarity check: no recent `customer_win` posts in the log, so should pass cleanly.

**Expected behavior:**

- signal_type: `customer_win` (high confidence)
- Template: `templates/creator_story.md` (customer_win uses the creator-story template per `core_rules.md` Section 5)
- Blog should follow case-study variant of creator story. Open with Hiroshi as protagonist, not Honda as logo.
- LinkedIn should lead with Honda + Hiroshi name in first 200 chars.
- PR pitch should name Sophia Silver as contact (per `core_rules.md` Section 9 — customer-win default).
