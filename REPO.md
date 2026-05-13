# Repository contents

This repository is a complete snapshot of the Vizcom GTM Amplifier project: the agent, the rules and templates that drive it, the voice corpus it learns from, sample inputs, dry-run outputs, and a strategic writeup explaining what was built and why.

## Quick orientation

| If you want to | Open |
|---|---|
| Understand what was built and why (the strategic case) | [`writeup/Vizcom GTM Amplifier — Strategic Writeup.md`](./writeup/Vizcom%20GTM%20Amplifier%20%E2%80%94%20Strategic%20Writeup.md) (or the .html version next to it) |
| See what the agent actually produces | [`outputs/2026-05-08-saman-mule-dryrun/`](./outputs/2026-05-08-saman-mule-dryrun/) — open `preview.html` first |
| Learn how to run the agent yourself | [`README.md`](./README.md) (the quickstart) |
| Read the agent's rules | [`core_rules.md`](./core_rules.md) (loaded every run, ~920 words) |
| Read the agent definition | [`.claude/agents/vizcom-gtm-amplifier.md`](./.claude/agents/vizcom-gtm-amplifier.md) |
| See the voice corpus | [`training/voice_corpus.md`](./training/voice_corpus.md) — 16 captured Vizcom posts with analysis |
| Run a sample yourself | [`samples/README.md`](./samples/README.md) — 6 ready-to-use sample inputs |
| See the full session history | [`LLM chat transcript.md`](./LLM%20chat%20transcript.md) |

## Folder layout

```
.
├── README.md                      Quickstart — how to run the agent
├── REPO.md                        You are here — repo orientation
├── LLM chat transcript.md         Reconstructed session transcript
│
├── core_rules.md                  Universal voice + format rules (loaded every run)
├── intake.md                      Phase 0 spec — extraction + clarification + similarity
├── skills.md                      Deep voice reference (loaded when needed)
├── requirements.md                Agent purpose, inputs, outputs, constraints
├── workflow.md                    User-facing workflow with troubleshooting
│
├── .claude/agents/
│   └── vizcom-gtm-amplifier.md    The Claude Code subagent definition
│
├── templates/                     One blog template per signal type
├── samples/                       6 ready-to-use sample inputs + run-all recipe
├── renders/                       Hero images organized by signal slug
├── signals/                       Agent-written signal records (one per run)
├── outputs/                       Agent-written drops (one folder per run)
├── training/
│   ├── voice_corpus.md            16 evidence samples + cross-corpus synthesis
│   └── recent_topics.md           Rolling log for the similarity check
├── scripts/
│   ├── generate_preview.py        Builds preview.html per drop
│   └── generate_writeup_html.py   Builds the writeup HTML
└── writeup/
    ├── Vizcom GTM Amplifier — Strategic Writeup.md
    ├── Vizcom GTM Amplifier — Strategic Writeup.html   (open in browser)
    └── visuals/                   SVGs embedded in the writeup
```

## Stack

- **Claude Code** as the agent runtime
- **Python 3** (no external dependencies) for the two helper scripts
- **Markdown** as the canonical format for spec, templates, and outputs
- **SVG** for the writeup visuals (embedded inline in the HTML version)

## How to run the agent

See [`README.md`](./README.md) for the full quickstart. Short version:

```bash
cd "/Users/dharahaskandikattu/Documents/gtm agent v2"
claude
```

Inside Claude Code, run `/agents` to verify `vizcom-gtm-amplifier` is registered, then drop any signal:

```
Run vizcom-gtm-amplifier on samples/01-product-launch-smart-dropper.md
```

The agent produces a self-contained drop folder under `outputs/{slug}/` with five channel files, a summary, the hero render, and a browser-openable `preview.html`.

## How the writeup HTML was generated

```bash
python3 scripts/generate_writeup_html.py
```

This reads `writeup/Vizcom GTM Amplifier — Strategic Writeup.md`, inlines the four SVG visuals from `writeup/visuals/`, and produces a single self-contained HTML file next to the markdown source. No external CSS or JS dependencies. Double-click to open.

## License & sharing

This repository contains a build artifact for evaluation. The voice corpus quotes Vizcom's own publicly-published content (blog, X, LinkedIn). Cited external sources retain their original ownership.
