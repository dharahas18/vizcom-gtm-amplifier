# Sample 4 — Milestone (1 million designers)

**Signal type:** `milestone`
**Input style:** Pasted founder draft + supporting facts
**What it tests:** Milestone template (founder-letter register), embargo handling, similarity check (Series B was Oct 29, 2025 — last major milestone)

**Run with:**
```
Run vizcom-gtm-amplifier on samples/04-milestone-one-million-designers.md
```

---

THE NEWS: We just crossed 1 million designers on Vizcom. Up from 700K when we announced Series B in October.

Supporting numbers (6 months Nov 2025 → May 2026):
- 1,247,000 minutes spent designing in Vizcom (vs. 657,403 in all of 2025)
- 168 Fortune 500 customers (up from 150)
- 142 countries represented
- 11 Vizcom Worlds community events hosted
- ~4,200 attendees across community events

Embargo: Tuesday May 20, 2026, 6:00 AM Pacific. Press list goes out the night before.

Hero render: samples/renders/one_million_designers_hero.png
Secondary: samples/renders/global_community_map.png

Jordan wrote a draft of the founder letter — paste below. He wants to keep the "What if you could hold your design?" hook style from Series B but reframe for the community milestone. Feel free to adjust.

---

Draft from Jordan:

"It started as a personal frustration about going from sketch to render. Last week, 1 million designers were asking the same question.

When we announced our Series B in October, we said we wanted to make the line go further — to shorten the distance between an idea and something you could hold. Six months later, the line has gone further than any of us predicted. 1.2 million minutes spent in Vizcom this period — more in six months than all of last year combined.

The numbers are real, but they're not the story. The story is in the renders. In the keyboards built from concrete and the mules cut from bronze and the alarm clocks that look like they belong on a real bedside table. Designers showed up with ideas that used to die in sketchbooks, and the ideas didn't die.

We're hiring across engineering, design, and beyond. The next million designers are already showing up..."

---

**What the agent should ask:**

1. **Founder draft integration:** Should the agent use Jordan's draft verbatim, treat it as raw material to rewrite, or blend it into the standard milestone template? Recommended: use as raw material, blend into the milestone H2 structure.
2. **Embargo timing:** Already specified — May 20, 6am PT. Agent should set posting_time accordingly.
3. Similarity check: last `milestone` was Series B on Oct 29, 2025 — 6+ months ago. R4 (same signal_type in last 5 days) does NOT fire. R1/R2/R3/R5/R6 do not fire either. Should pass cleanly.

**Expected behavior:**

- signal_type: `milestone` (high confidence)
- Template: `templates/milestone.md`
- Blog should follow founder-letter form: "What if" hook → Where this started → What we've built (numbers in bold) → What's next → Thank you → hiring CTA.
- PR pitch goes out **the night before** (May 19) for the May 20 embargo.
- Contact: Jordan Taylor (CEO).
- Recycle the autonomous-vehicle analogy and "amplifying the human spark" line from Series B (Sample 7) where they earn their place.
