# Sample 5 — Event (Dutch Design Week, pre-event)

**Signal type:** `event`
**Input style:** Structured fact-list
**What it tests:** Event template (pre-event variant), pre-event posting sequence (T-7/T-5/T-3/T-1, not the standard 0/15m/30m), partner-name handling

**Run with:**
```
Run vizcom-gtm-amplifier on samples/05-event-design-week-amsterdam.md
```

---

EVENT: Dutch Design Week 2026
MODE: pre-event (announcement going out one week before)

DATES: October 19–27, 2026
LOCATION: Klokgebouw, Strijp-S, Eindhoven, Netherlands
SCALE: ~350,000 attendees over the week

VIZCOM PRESENCE:
- Booth in the Material Futures hall (booth M-114)
- Live demo every day at 14:00 and 17:00 CET — Sophia Silver leading
- Panel on October 22, 16:00 CET: "AI in industrial design — five practitioners, no slides"
  - Moderator: Emil Lukas (Vizcom)
  - Confirmed panelists: Julius (julius.works, Berlin), Ádám Miklósi (Budapest)
  - Two more panelists TBD by mid-September

BOOTH RENDER: samples/renders/ddw_2026_booth.png
PANEL POSTER: samples/renders/ddw_2026_panel_poster.png

RSVP / SCHEDULE: https://ddw.nl/vizcom-2026
BOOK A DEMO: https://vizcom.com/events/ddw-2026

PRESS CONTACT: Sophia Silver, Product Marketing
COMMUNITY CONTACT: Kim Lu, Growth Marketing

We're going public with this on October 12 (T-7 days before the event opens). Want the announcement live by 9am CET that day.

---

**What the agent should ask:**

1. **Pre vs. post:** Already specified (`pre-event` in MODE). Agent should not need to ask.
2. **Confirmed designer handles:** Julius (julius.works) and Ádám Miklósi are named with location; should be enough.
3. **Two TBD panelists:** Agent should NOT invent names. Should flag `[NEEDS CONFIRMATION — 2 panelists TBD]` in the blog body and `summary.md`.
4. Similarity check: no recent `event` posts in the log; should pass.

**Expected behavior:**

- signal_type: `event` (high confidence)
- Template: `templates/event.md` (pre-event variant)
- Blog: "Vizcom at Dutch Design Week 2026: What we're bringing" or similar.
- Pre-event posting sequence per `templates/event.md`: blog T-7 (Oct 12) / LinkedIn T-5 (Oct 14) / X T-3 (Oct 16) / X reminder T-1 (Oct 18).
- PR pitch goes out parallel with the blog.
- Contact mapping: Sophia Silver (product-focused event with Vizcom demo) per `core_rules.md` Section 9.
- Tag @julius.work on X when applicable.
