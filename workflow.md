# Vizcom GTM Amplifier — Workflow

How to run the agent end-to-end. Written for the human marketer who triggers it.

---

## 1. One-time setup

1. Confirm the folder layout:
    ```
    .
    ├── core_rules.md        ← universal rules (loaded every run)
    ├── intake.md            ← Phase 0 — extraction + clarifying questions
    ├── requirements.md
    ├── skills.md
    ├── workflow.md          ← you are here
    ├── signals/             ← agent writes signal files here (you don't author them)
    ├── outputs/             ← agent writes the six-file drops here
    ├── training/
    │   ├── voice_corpus.md  ← 16 samples + cross-corpus synthesis
    │   └── recent_topics.md ← similarity-check log
    ├── templates/           ← one blog template per signal type
    └── .claude/
        └── agents/
            └── vizcom-gtm-amplifier.md
    ```
2. Open the project in Claude Code. The agent is auto-registered from `.claude/agents/vizcom-gtm-amplifier.md`.
3. Verify with `/agents`. Expected: `vizcom-gtm-amplifier` listed.

---

## 2. Running the agent — just drop something

You don't author YAML. Drop any of these:

| What you have | How to run |
|---|---|
| A doc (.md, .txt, .pdf, .docx) | `Run vizcom-gtm-amplifier on /path/to/doc.pdf` |
| Pasted text | `Run vizcom-gtm-amplifier — here's the signal: {paste}` |
| A URL | `Run vizcom-gtm-amplifier on https://...` |
| A one-line description | `Run vizcom-gtm-amplifier — we just shipped Smart Dropper, render at /renders/x.png, demo at youtu.be/X` |
| Multiple sources | `Run vizcom-gtm-amplifier — here's the email + this render path + the founder's Slack note` |

The agent then:

1. **Phase 0 — Intake.** Reads input. Extracts facts. Asks clarifying questions (multiple-choice in chat) if anything required is missing. Cap: 2 rounds. Writes the signal file.
2. **Phase B — Drafting.** Drafts all six channel files. Auto-fixes mechanical voice violations. Flags fact gaps as `[NEEDS CONFIRMATION]`.
3. **Reports** in chat: signal slug, signal type, files written, posting sequence, intake summary.

Typical runtime: 90–120 seconds.

---

## 3. How the agent handles missing facts

Claude Code subagents can't pause mid-run for multi-choice prompts. The agent uses two patterns instead:

**Halt and ask in chat (critical gaps only):**

- Hero render path missing → halts. Re-run after adding the path.
- Signal type genuinely ambiguous (e.g., customer-win vs. community-moment with no clear lead) → halts.
- Fortune-500 customer named but no NDA-cleared note in the input → halts.

When the agent halts, it writes a partial signal file with `[NEEDS]` markers and prints a plain-text message naming what's missing. Add the info to the input or edit `signals/{slug}.md` directly, then re-run:

```
Run vizcom-gtm-amplifier on signals/{slug}.md
```

**Proceed and flag (non-critical gaps):**

- Designer location / IG handle / secondary renders missing → drafts proceed, gaps flagged as `[NEEDS CONFIRMATION]` in the body.
- Designer quote in input but no explicit clearance note → quote is omitted, gap flagged.
- UGC consent unclear → halts for UGC moments; proceeds with caveat for community moments.

All gaps appear in `outputs/{slug}/summary.md` under `## Open flags`.

**Similarity check is also non-interactive.** It runs every time, logs to `summary.md` under `## Similarity check`, and proceeds with drafting. You read the log and decide post-hoc whether to publish, hold, or rewrite.

---

## 4. Reviewing the drop

Open `outputs/{signal_slug}/summary.md` first. It shows:

- Classification and confidence.
- Channels generated and why.
- Recommended posting sequence with timing.
- Voice self-check result.
- Auto-fixes applied.
- Open flags (`[NEEDS CONFIRMATION]` markers).

If `summary.md` shows a `fail`, fix the underlying signal (missing customer name, quote permission, render path) and re-run on the signal file: `Run vizcom-gtm-amplifier on signals/{slug}.md`.

Then read in order:

1. `blog.md` — canonical long-form.
2. `linkedin.md` — confirm designer/customer in first 200 chars and the standalone closer.
3. `x_thread.md` — confirm render is referenced in tweet 1 and the two-tweet pair holds together.
4. `geo_aeo.md` — confirm the answer is direct and citation-friendly.
5. `pr_pitch.md` — confirm exactly 3 sentences and the contact is named.

Edit directly in the output files. The agent does not own the final copy — you do.

---

## 5. Posting

The agent does not post. A human publishes. Recommended default sequence:

| T+ | Channel | Notes |
|---|---|---|
| 0 | Blog (vizcom.com/blog) | Canonical URL. |
| +15m | LinkedIn (linkedin.com/company/vizcomhq) | Hero render/video/carousel. Default 0 hashtags. Link in comments. |
| +30m | X (x.com/Vizcom_) | Two-tweet pair: story + link. 0 hashtags, 0 emoji in bodies. **Handle is @Vizcom_, not @Vizcom_ai.** |
| +60m | Instagram (instagram.com/vizcom_) | Hero render or reel + short caption echoing tweet 1. |
| 0 (parallel) | PR pitch | Outbound email. |

Adjustments:
- **Milestone:** PR pitch night before for a morning embargo. Blog live at embargo time.
- **Community / Hold Your Ideas:** Skip PR unless the designer is press-known.
- **UGC:** Instagram + X lead. Blog only for a full creator-story feature.
- **Confidential:** PR pitch only (to a curated list).
- **Event (pre):** Blog T-7, LinkedIn T-5, X T-3, reminder X T-1.

---

## 6. Iterating on voice

Voice grounds in `training/voice_corpus.md` and per-signal-type templates. To recalibrate:

1. Add a new sample to `training/voice_corpus.md` following the analysis frame.
2. If a template's H2 outline or opener formulas need to shift, edit `templates/{type}.md`.
3. If a universal rule changes (hashtags, channel length, forbidden word), edit `core_rules.md` — not the templates.
4. Re-run on a recent signal to confirm the voice shifted.

Refresh the corpus every 90 days. Vizcom's blog cadence is ~weekly; in 90 days you'll have ~12 new posts.

---

## 7. When NOT to use the agent

- Crisis comms / legally sensitive — escalate.
- Paid-ad copy — different voice rules.
- Sales outbound / one-to-one — different register.
- Internal-only communications.
- Un-cleared designer quotes — hold the drop.

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Agent asked the same question twice | Round 2 of intake; first answer didn't resolve. | Check `summary.md` → Clarifications. |
| "I asked twice but still need {field}" | Critical field unanswered. | Add to input/signal file and re-run. |
| `[NEEDS CONFIRMATION: customer_name]` | Customer not on allowed list, no source attached. | Add confirmation source URL, or use generic descriptor. |
| `blog.md` > 1,500 words | Too much raw context. | Tighten input or edit `## Raw input` and re-run. |
| X two-tweet pair reads like a brief | 2022-voice verb-stack slipped in. | Edit tweet 1 to the `"{Product} by {Designer}. ... Designed in Vizcom, ..."` formula from `templates/creator_story.md`. |
| Designer name not in first 30 words of blog | Wrong template. | Re-run intake — confirm `signal_type` is creator-story-family, not `product_launch`. |
| LinkedIn caption > 1,300 chars | Self-check missed it. | Open an issue. |
| Render path broken | `hero_render` wrong in signal file. | Edit `signals/{slug}.md` and re-run. |
