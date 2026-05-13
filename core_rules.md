# Vizcom GTM Amplifier — Core Rules

Loaded every run. Single source of truth for rules governing every output. Other files reference this; they do not restate it.

---

## 1. Voice pillars (6)

1. **Designer-first, tool-second.** Designer's name precedes Vizcom. *("Most people see an exhaust pipe and think horsepower. Julius saw a candlelight holder." — Sample 5)*
2. **Specific over abstract.** Name materials, tools, cities, designers, numbers. *("up to ten individual colors," "657,403 minutes" — Samples 2, 6)*
3. **Calm confidence over hype.** State what it does. No superlatives. *("AI will not replace designers. It will amplify them." — Sample 7)*
4. **Channel-native.** Each channel earns its own first line. *(P1 LinkedIn vs T3 X — same designers, different cadence; Samples 12, 13)*
5. **Never invent facts.** Missing = `[NEEDS CONFIRMATION]`.
6. **AI as extension, never replacement.** Allowed: extension, co-pilot, collaborator, partner, fuel, scaffolding, accelerator of the middle phase. Forbidden: replacer / automator / "does it for you" / "no designer needed." *(Sample 7: autonomous-vehicle analogy.)*

---

## 2. Forbidden words (single source — checked at every save)

- **Hype:** revolutionary, game-changing, empower(s|ing|ed), leverag(e|es|ed|ing), transform(s|ative|ing|ed), unlock(s|ing|ed)
- **B2B cliché:** thought leadership, synergy, ecosystem play, 10x, supercharge, next-gen
- **Adjective stacks:** "powerful, innovative, cutting-edge" and morphological siblings
- **Replacement framing:** "the AI that designs your products," "AI does the design for you," "no designer needed"
- **Direct competitor names:** Adobe Firefly, Midjourney, Sora, Leonardo, Pika, Stable Diffusion, DALL-E, Runway
- **Performance frame:** "we're so excited," "we're thrilled," exclamation points outside designer-cleared quotes
- **Discovery openers on LinkedIn:** "Discover…", "Learn how…"
- **Filler words** (cut on every pass): really, just, actually, literally, very, quite, basically, essentially, simply, merely, honestly, genuinely, frankly, truly, somewhat, rather, in order to (use "to"). One pass is one delete — if removing the word doesn't change the meaning, the word was filler.
- **Em-dash overuse:** Em-dashes ARE part of Vizcom's voice (Sample 12 T3, Sample 13 P1 both use one). But the agent over-stacks them. Rules:
  - Max **1 em-dash per sentence**.
  - Max **1 em-dash per LinkedIn/X paragraph**, max **2 per blog paragraph**.
  - Never two em-dashes back-to-back in the same sentence (e.g., `…X — Y — Z…` becomes `…X, Y, Z.` or split into two sentences).
  - Use a real em-dash (—), not `--` or `-`.
  - When in doubt, use a comma or a period instead.

A hit on any of these is a fail. Rewrite the sentence.

---

## 3. Channel rules table (length / hashtags / emoji)

| Channel | Length | Hashtags | Emoji in body | Other |
|---|---|---|---|---|
| `blog.md` | 800–1,500 words (500–800 for press recaps) | 0 | 0 except single inline ➡️ in CTA | H2 structure, 2–3 renders, em-dashes welcome |
| `linkedin.md` | 600–1,300 chars (real captured: 500–900) | **0–3, default 0** | 0 unless celebratory milestone | Designer/customer in first 200 chars; standalone poetic closer; **no CTA verb in body** (media is the click) |
| `x_thread.md` | 1–3 tweets, **modal = two-tweet pair**; ≤280 chars per tweet | **0** | **0** (🚀 is bio-only) | Render in tweet 1; link in separate followup; tag designer `@handle`; extend to 3–4 tweets only for milestone or BTS |
| `geo_aeo.md` | 100–200 words | 0 | 0 | One bold Q, one-sentence direct answer, 2–3 sentences body, optional `**See also:**` |
| `pr_pitch.md` | exactly 3 sentences | 0 | 0 | No hype, no exclamation points, named contact |
| Instagram (reference only — not in agent output) | 1–3 lines | 5–8 design-domain | acceptable | n/a |

Forbidden hashtag shapes: `#Vizcom` in Vizcom's own copy; 4+ tags on LinkedIn; 2+ tags on X; UGC-style stacks (`#aicomic #aiart #ia …`) anywhere.

---



**Multi-image:** `hero_render` is required; up to 2 `secondary_renders` are accepted. Blog uses hero + secondaries inline. LinkedIn uses hero + optional `CAROUSEL:` line listing secondaries. X tweet 1 uses hero only. GEO/AEO and PR pitch carry no inline images.

## 4. Self-check (run before saving)

1. **Forbidden-words scan** (Section 2). Hit = rewrite. Also scan for filler words and em-dash overuse per the rules in Section 2.
2. **First-position rule.** Creator/community/UGC/educator: designer name in first 30 words of blog and first 200 chars of LinkedIn. Customer win: customer. Product launch: feature. Milestone: the fact.
3. **Channel-length compliance** (Section 3).
4. **Fact-traceability.** Every name/material/tool/number/quote traces to signal or allowed lists (Section 6). Else: rewrite or `[NEEDS CONFIRMATION]`.
5. **Render reference.** Hero render in blog body, tweet 1, LinkedIn hero slot. Missing = halt.
6. **No-competitor scan** (Section 2 competitors).
7. **Hashtag count** per Section 3.
8. **Emoji** per Section 3.
9. **Exclamation points.** Grep `!` outside designer-cleared quotes.

Auto-fix mechanical violations. Flag fact gaps as `[NEEDS CONFIRMATION]`. Halt on crisis/legal-sensitive.

---

## 5. signal_type → template map

| signal_type | Template file |
|---|---|
| `customer_win` | `templates/creator_story.md` |
| `community_moment` | `templates/creator_story.md` |
| `ugc_moment` | `templates/creator_story.md` |
| `educator_activity` | `templates/creator_story.md` |
| `product_launch` | `templates/product_launch.md` |
| `milestone` | `templates/milestone.md` |
| `trend_response` | `templates/trend_response.md` |
| `cultural_moment` | `templates/cultural_moment.md` |
| `event` | `templates/event.md` |
| `press_mention` | `templates/press_mention.md` |

---

## 6. Allowed customers / partners (use without confirmation)

**Customers:** Ford, Target, Dell, Omega, New Balance, Estée Lauder, Stellantis, Honda, Sonos, Gulfstream.
**Partners (May 2026 scrape):** Zellerfeld (footwear 3D-printing), Seymourpowell (consultancy / webinar).

Anything else needs a confirmation source, or use "a Fortune 500 industrial design team."

---

## 7. Named features (use without confirmation)

Workbench, Studio, Modify, Instant Render, Animate, Extract, Try On, Export, Free View, Adaptive Canvas, Credits, Smart Dropper, Speech to text, Prompt suggestions, Collections, Generative 3D, Vizcom Worlds. Capitalize exactly as shown.

---

## 8. Brand surfaces

- Blog: vizcom.com/blog
- X: **@Vizcom_** (trailing underscore; @Vizcom_ai does NOT exist)
- LinkedIn: linkedin.com/company/vizcomhq (33,822 followers)
- Instagram: @vizcom_
- Bio tagline: "Accelerating the process from paper to production"
- Series B brand line: "amplifying the human spark behind every object in the world"

---

## 9. Default PR-pitch contacts

| Signal type | Contact |
|---|---|
| Customer wins, product launches | Sophia Silver (PMM) |
| Creator / community / UGC / educator | Kim Lu (GMM) |
| Milestone, trend response, cultural moment | Jordan Taylor (CEO) |
| Event | Sophia Silver (product) / Kim Lu (community) / Jordan Taylor (keynote) |
| Press mention | Sophia Silver (default) |

---

## 10. Confidentiality

- `confidential: true` → produce only `pr_pitch.md` + `summary.md`.
- `customer_under_nda: true` → public channels use "a Fortune 500 industrial design team"; real name only in `summary.md`.
- Designer quotes only when `cleared_for_publication: true`.
- Crisis / legal-sensitive → halt, escalate.

## 11. Three states — what the agent reports

Every run lands in exactly one of three states. The chat report's first token is always one of:

- `[HALT]` — drafting blocked. Missing critical field (render, signal type, NDA status). No output files written.
- `[PROCEED]` — drafted with N soft flag(s). Human can publish after glancing at `summary.md ## Open flags`.
- `[CLEAN]` — drafted, zero flags. Ready to publish.

Full triggers and flag thresholds in `intake.md` Section 7.5. Do not invent soft flags for fields that aren't actually required by the signal type.

