# Sample 6 — Thin signal (forces the halt-and-ask flow)

**Signal type:** ambiguous (intentionally)
**Input style:** Slack one-liner with critical info missing
**What it tests:** The halt-and-return clarification flow. The agent should NOT draft. It should write a partial signal file and chat-message back asking for the missing critical facts.

**Run with:**
```
Run vizcom-gtm-amplifier on samples/06-thin-signal-clarification.md
```

---

[from #gtm-signals, posted by Jordan]

Honda is doing something with us next week. Should we amplify?

---

**Why this is intentionally thin:**

- No clear signal type (could be customer_win, event, press_mention, or product_launch)
- No hero render path
- No specifics about what Honda is doing
- No date beyond "next week"
- No NDA-cleared status for Honda (allowed-list customer, but explicit confirmation needed)
- No quote, no named designer

**Expected behavior:**

The agent should HALT after Phase 0c (pre-flight) without drafting any channel files. It should:

1. Write a partial signal file at `signals/2026-05-13-honda-something.md` (or similar slug) with `[NEEDS]` markers on each missing critical field.
2. Print a plain-text chat message naming exactly what's needed, e.g.:

> "I need 4 things before I can draft this:
> 1. **The specific news.** Is this a customer win (Honda using Vizcom on a named project), a product launch (Honda + Vizcom co-announcing a feature), an event (joint webinar / panel), or a press mention (a publication covering Honda + Vizcom)?
> 2. **Hero render path.** A Vizcom-rendered visual to anchor the drop.
> 3. **NDA status for Honda.** Cleared to name publicly, NDA (use generic descriptor), or confidential (PR pitch only)?
> 4. **Date.** 'Next week' is too soft — what's the target post date?
>
> Add these to the input and re-run, or edit `signals/2026-05-13-honda-something.md` directly and run: `Run vizcom-gtm-amplifier on signals/2026-05-13-honda-something.md`"

3. NO channel files are written. NO `summary.md` produced (since nothing was drafted).

**This is the correct, expected behavior** — not a failure. The agent is honestly declining to invent facts it doesn't have. After you provide the missing info and re-run, it should proceed normally.
