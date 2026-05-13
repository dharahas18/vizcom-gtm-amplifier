# Vizcom GTM Amplifier

Turn one organic signal into a coordinated six-channel content drop in Vizcom's voice — without spending an hour on each surface.

The agent takes whatever you have (a customer email, a press release, a one-line chat description, a URL, a Slack export), asks clarifying questions if needed, checks whether you've posted something similar recently, then drafts a blog post, a LinkedIn post, an X two-tweet pair, a GEO/AEO Q&A, a PR pitch, and a posting-sequence summary. All grounded in Vizcom's actual voice from a 16-sample corpus of real recent posts.

---

## What it produces

For every signal, six files in `outputs/{signal_slug}/`:

- `blog.md` — 800–1,500 word canonical long-form
- `linkedin.md` — 600–1,300 char post, hero render or carousel
- `x_thread.md` — two-tweet pair (story tweet + link tweet)
- `geo_aeo.md` — 100–200 word Q&A optimized for answer engines
- `pr_pitch.md` — exactly 3 sentences for trade press
- `summary.md` — classification, posting sequence, auto-fix log, open flags, similarity check

Plus the constructed signal record at `signals/YYYY-MM-DD-{slug}.md`.

---

## Quickstart

### 1. One-time setup

```bash
cd "/Users/dharahaskandikattu/Documents/gtm agent v2"
claude   # opens this folder in Claude Code
```

In Claude Code, verify the agent is registered:

```
/agents
```

You should see `vizcom-gtm-amplifier` in the list.

### 2. Run the agent — three ways

**Option A — drop a document:**
```
Run vizcom-gtm-amplifier on /path/to/customer_email.pdf
```
or drag the file into the Cowork chat and say `Run vizcom-gtm-amplifier on this`.

**Option B — paste text:**
```
Run vizcom-gtm-amplifier — here's the signal:

[paste the email body, press release, transcript, or description]
```

**Option C — describe it in one line:**
```
Run vizcom-gtm-amplifier — we just shipped Smart Dropper, render at /renders/x.png, demo at youtu.be/X
```

The agent then:

1. **Intake.** Extracts facts from your input. If a critical fact is missing (hero render, signal type ambiguity, NDA status), the agent HALTS, writes a partial signal file with `[NEEDS]` markers, and asks you in plain chat text. You add the info and re-run. Non-critical gaps (designer location, IG handle) become `[NEEDS CONFIRMATION]` flags in the output. Note: Claude Code subagents are non-interactive, so the agent can't pop up mid-run multi-choice prompts — the halt-and-ask pattern is what you'll see instead.
2. **Similarity check.** Reads `training/recent_topics.md`. If your new signal overlaps a recent Vizcom post (same designer in 30 days, same form-factor 3+ times in 14 days, same feature in 14 days, etc.) it asks: post anyway, hold this drop, or combine into a recap.
3. **Drafting.** Drafts all six channel files in one ~90s pass. Auto-fixes voice violations (hype words rewritten, lengths trimmed, hashtags stripped). Flags fact gaps as `[NEEDS CONFIRMATION]`.
4. **Reports back** in chat with: signal slug, signal type, files written, posting sequence, intake summary.

### 3. Review the drop

**Open `outputs/{signal_slug}/preview.html` in a browser first** — it visualizes all five channels styled approximately like LinkedIn / X / blog / GEO answer / PR email, with the hero render and any secondary renders embedded. One file, full visual review.

Then open `outputs/{signal_slug}/summary.md`. It tells you:

- Classification and confidence
- Recommended posting sequence with timing
- Voice self-check result (pass/fail per channel)
- Auto-fixes applied
- Open flags — anything tagged `[NEEDS CONFIRMATION]`
- Similarity check log

Then read the files in this order: `blog.md` → `linkedin.md` → `x_thread.md` → `geo_aeo.md` → `pr_pitch.md`. Edit inline if needed.

### 4. Publish

The agent doesn't post. You publish manually per the timing in `summary.md`. Default sequence:

```
T+0    Blog
T+15m  LinkedIn
T+30m  X two-tweet pair
T+60m  Instagram
T+0    PR pitch sent to trade press (parallel)
```

Signal-type-specific adjustments (milestones, events, confidential signals) are listed in `summary.md`.

---

## Worked example — Saman shoe drop

**You drop into chat:**

> "Andrew Moya and Juan Rujana designed The Saman — a mule rooted in Latino culture and Pre-Columbian artifacts. Amber color echoes ancestral gold, seashell body, veins like tree roots. Made with Zellerfeld. Hero render at /renders/saman.png."

**Agent intake asks:**

1. *"I see this could be a `community_moment` (designer feature) or a `customer_win` (Zellerfeld partnership). Which is closer?"* → you pick `community_moment`
2. *"Do you have Instagram or X handles for Andrew and Juan?"* → you provide them or skip

**Agent similarity check fires:**

> *"This is the 3rd mule feature in 14 days (Catapill Apr 14, Digits May 1). Post anyway, hold a week, or combine into a 'mule moment' recap?"*

You pick **post anyway** — the series is deliberate.

**Agent drafts and reports back:**

> "Wrote outputs/2026-05-08-saman-mule/ — `community_moment`. Six files. Posting sequence in summary.md. Intake auto-extracted 8 fields, asked 2 clarifying questions, similarity rule R2 fired (3rd mule in 14 days, user chose: post anyway). 1 [NEEDS CONFIRMATION] flag — designer handles."

A full dry-run example is at `outputs/2026-05-08-saman-mule-dryrun/`.

---

## Project structure

```
.
├── README.md                              ← you are here
├── intake.md                              ← Phase 0 spec: extraction + clarification + similarity
├── workflow.md                            ← full workflow + troubleshooting
├── requirements.md                        ← agent purpose, inputs, outputs, constraints
├── skills.md                              ← voice pillars, channel rules, signal taxonomy
│
├── signals/                               ← agent-written signal records (do not hand-edit)
├── outputs/                               ← agent-written six-file drops
│
├── training/
│   ├── voice_corpus.md                    ← 16 evidence samples + cross-corpus synthesis
│   └── recent_topics.md                   ← rolling log of recent Vizcom posts (for similarity)
│
├── templates/
│   ├── creator_story.md                   ← customer_win, community_moment, ugc_moment, educator_activity
│   ├── product_launch.md
│   ├── milestone.md
│   ├── trend_response.md
│   ├── cultural_moment.md
│   ├── event.md
│   └── press_mention.md
│
└── .claude/agents/
    └── vizcom-gtm-amplifier.md            ← Claude Code subagent definition (auto-registered)
```

---

## What the agent will not do

- Generate images or renders — you provide the `hero_render` file path.
- Post to any platform — you publish manually.
- Write paid-ad copy or sales outbound — different voice rules, out of scope.
- Handle crisis comms or legally sensitive copy — halts and escalates.
- Translate to other languages — English only in v1.
- Batch multiple signals into a single campaign drop — v1 is one signal = one drop.
- Auto-update `training/recent_topics.md` — you append a new entry after the drop is published.

---

## Maintenance

| Cadence | What to refresh |
|---|---|
| **Weekly** | Append the past week's published posts to `training/recent_topics.md` |
| **Every 90 days** | Re-scrape vizcom.com/blog, x.com/Vizcom_, linkedin.com/company/vizcomhq. Add new samples to `training/voice_corpus.md` following the 14-point analysis frame. Update vocabulary if new canonical phrases have emerged. |
| **When voice shifts** | Edit `skills.md` Section 6 (voice pillars) and `templates/*.md` if structures change. |

---

## Where to look for more

- [`intake.md`](./intake.md) — how the agent extracts facts, asks clarifying questions, and runs the similarity check
- [`workflow.md`](./workflow.md) — full workflow + posting timing + troubleshooting
- [`skills.md`](./skills.md) — voice pillars (with evidence), channel rules, hashtag/emoji policy, signal-type → template map
- [`requirements.md`](./requirements.md) — agent purpose, inputs, outputs, constraints, scope
- [`training/voice_corpus.md`](./training/voice_corpus.md) — 16 evidence samples + cross-corpus synthesis
- [`training/recent_topics.md`](./training/recent_topics.md) — rolling log + similarity-check data
- [`templates/`](./templates/) — one blog template per signal type

---

## Status

**v1** — Single-signal mode, English only, intake + clarification + similarity check + auto-fix self-check. Built and dry-run-tested on May 13, 2026. See `outputs/2026-05-08-saman-mule-dryrun/` for the test result.

**Future work** (not in v1):
- Campaign mode (batched signals)
- Localization (non-English channels)
- Posting integration (Buffer / Sprout)
- Auto-recap drops when similarity-check picks "combine"
- Memory of phrasing across past drops to avoid repetition
