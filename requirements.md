# Vizcom GTM Amplifier — Requirements

## 1. Purpose

The Vizcom GTM Amplifier converts a single organic signal — customer win, product launch, event, press mention, milestone, UGC moment, trend response, educator activity, community moment, or cultural moment — into a coordinated, multi-channel content drop in Vizcom's voice, anchored by a Vizcom-rendered visual.

Vizcom ships work in five places (blog, X, LinkedIn, Instagram, trade press); each channel rewards a different cadence and register. The agent removes the asymmetry of manual assembly without removing the human judgment that gives the brand its calm-confident, designer-first edge.

## 2. Inputs

Any input form. The human never writes YAML. Accepted inputs (full spec in `intake.md`):
- Document (.md, .txt, .pdf, .docx).
- Pasted text.
- URL.
- One-line chat description.
- Multiple sources combined.

The agent runs **Phase 0 — Intake** before any drafting. It extracts to an internal schema, halts and returns a plain-text clarification request if a critical field is missing (Claude Code subagents are non-interactive — no mid-run multi-choice prompts), and otherwise writes `signals/YYYY-MM-DD-{slug}.md` with `generated_by_intake: true`. Non-critical gaps become `[NEEDS CONFIRMATION]` flags in the body.

The agent **must not** invent facts. Missing facts → `[NEEDS CONFIRMATION]` in `summary.md`.

## 3. Outputs

Six files to `outputs/{signal_slug}/`:

1. `linkedin.md`
2. `x_thread.md`
3. `blog.md`
4. `geo_aeo.md`
5. `pr_pitch.md`
6. `summary.md`

Channel-length / hashtag / emoji rules: see `core_rules.md` Section 3.
Per-signal-type blog templates: see `templates/{type}.md` (mapping in `core_rules.md` Section 5).

All Markdown is plain text. No inline HTML.

## 4. Voice constraints (strict)

The full rules live in `core_rules.md`. The non-negotiables:

- Designer-first, not tool-first.
- Specific over abstract — real designers, products, materials, workflows, numbers.
- No hype words (full list: `core_rules.md` Section 2).
- Channel-native (each channel earns its own first line).
- Never invent facts.
- No direct competitor names.
- AI as extension, never replacement.

Self-check enforced at file-output level: `core_rules.md` Section 4.

## 5. Non-goals

- The agent does not post. A human publishes.
- The agent does not generate images. Renders must exist at the path the signal specifies.
- No paid-ad copy or sales-team outbound — different voice rules.
- No crisis comms / legally sensitive content — escalate to a human.

## 6. Success criteria

A drop is successful when:

1. All six output files exist, pass the self-check, and respect channel lengths.
2. A reader who already knows Vizcom's blog cannot tell which sentences are agent-written. Voice indistinguishable from the most recent 6–12 months of corpus samples (Samples 1–8 and 11 in `training/voice_corpus.md`).
3. Hero render is named in blog body, tweet 1, and LinkedIn hero slot.
4. `summary.md` contains classification, posting sequence, and self-check result.
5. Zero invented facts. Zero hype words. Zero competitor names.

## 7. Files in this project

```
/
├── core_rules.md                            # universal rules (loaded every run)
├── intake.md                                # Phase 0 spec (loaded every run)
├── requirements.md                          # this file
├── skills.md                                # deep voice spec / signal taxonomy
├── workflow.md                              # how a user runs the agent
├── signals/                                 # agent-written intake records
├── outputs/                                 # one folder per signal
│   └── {signal_slug}/
│       ├── linkedin.md
│       ├── x_thread.md
│       ├── blog.md
│       ├── geo_aeo.md
│       ├── pr_pitch.md
│       └── summary.md
├── training/
│   ├── voice_corpus.md                      # 16 samples + cross-corpus synthesis
│   └── recent_topics.md                     # similarity-check log
├── templates/                               # one blog template per signal type
│   ├── creator_story.md                     # customer_win, community_moment,
│   │                                        # ugc_moment, educator_activity
│   ├── product_launch.md
│   ├── milestone.md
│   ├── trend_response.md
│   ├── cultural_moment.md
│   ├── event.md
│   └── press_mention.md
└── .claude/agents/
    └── vizcom-gtm-amplifier.md              # subagent definition
```

## 8. Open questions / future work

- **Localization.** English-only today. Future: target locale → channel-native hashtags + idioms.
- **Confidentiality.** Confidential signals already produce only `pr_pitch.md` + `summary.md`.
- **Render quality check.** Currently trusts the path. Future: verify resolution / aspect ratio per channel.
- **Corpus refresh.** `training/voice_corpus.md` should be refreshed every 90 days.
