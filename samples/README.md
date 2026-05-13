# Sample Inputs

Five realistic example signals you can use to test the agent in Claude Code. Each demonstrates a different signal type and a different input style.

| # | File | Signal type | Input style | What it tests |
|---|---|---|---|---|
| 1 | `01-product-launch-smart-dropper.md` | `product_launch` | One-line chat description | Simplest path — minimal clarifying questions |
| 2 | `02-community-moment-velocity-skateboard.md` | `community_moment` | Internal email/note | Creator-story template, designer quote clearance check, new form-factor (not a mule) |
| 3 | `03-customer-win-honda.md` | `customer_win` | Slack-message style with quote | NDA-clearance flow, named designer at customer, allowed-customer (Honda) |
| 4 | `04-milestone-one-million-designers.md` | `milestone` | Founder-draft + facts | Milestone template (founder-letter register), embargo handling, similarity check (Series B was last milestone) |
| 5 | `05-event-design-week-amsterdam.md` | `event` | Structured fact-list | Event template (pre-event variant), pre-event posting sequence (T-7/T-5/T-3/T-1) |
| 6 | `06-thin-signal-clarification.md` | ambiguous | Slack one-liner | **The halt-and-ask flow.** Intentionally missing critical facts so you can verify the agent stops, writes a partial signal file, and asks in plain text instead of drafting blindly. |

---

## How to use a sample

### Way A — drop the file path

In Claude Code:

```
Run vizcom-gtm-amplifier on samples/01-product-launch-smart-dropper.md
```

The agent will `Read` the file, parse the input section, run intake, and draft.

### Way B — paste the content

Open the file, copy everything below the `---` divider, and paste into chat:

```
Run vizcom-gtm-amplifier — here's the signal:

[paste]
```

### Way C — chat directly (no file)

For Sample 1 (Smart Dropper), you can also just describe it in chat:

```
Run vizcom-gtm-amplifier — we just shipped Smart Dropper, render at samples/renders/smart_dropper_hero.png, demo at youtu.be/smart-dropper-demo
```

---

## A note on renders

The `samples/renders/` paths in these files are placeholders. The agent will accept them and reference them in the output blog/LinkedIn/X — for a real run, replace with paths to actual Vizcom renders.

For a quick test where you don't have a render, just say "render placeholder" in the clarifying-question response when the agent asks; the agent will use `[NEEDS CONFIRMATION — hero_render]` and produce drafts you can verify the voice on.

---

## What to expect

For each sample, the agent will:

1. Read the input and extract facts.
2. Ask 1–3 clarifying questions (multi-choice in chat).
3. Run the similarity check against `training/recent_topics.md`.
4. Draft six output files in `outputs/{signal_slug}/`.
5. Report a <100-word summary in chat.

Total runtime: ~90–120 seconds per sample.

After each run, open `outputs/{signal_slug}/summary.md` to see the classification, posting sequence, auto-fixes, and open flags.
