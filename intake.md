# Intake — Vizcom GTM Amplifier (Phase 0)

The intake + clarification loop the agent runs **before** any drafting. No drafting until pre-flight passes.

The human never writes YAML. The agent extracts facts from whatever was dropped, asks clarifying questions if anything required is missing, then writes the signal file as the record of what it understood.

**See `core_rules.md`** for: signal_type → template map, allowed customers/partners, forbidden words.

---

## 1. Inputs the agent accepts

| Input form | How the agent reads it |
|---|---|
| File in Cowork (.md, .txt, .pdf, .docx) | `Read` the file path |
| Pasted text in chat | Use directly |
| URL (tweet, article, blog, transcript) | `web_fetch` the URL |
| One-line chat description | Use directly |
| Multiple sources combined | Concatenate, treat as one input |

The agent **does not** accept hand-written YAML signal files as the primary path.

---

## 2. The intake loop

### 0a — Parse input
Read file / `web_fetch` URL / use text directly. Concatenate multiples.

### 0b — Extract to internal schema

```yaml
signal_type:        # one of the 10 (see core_rules.md Section 5)
slug:               # kebab-case, agent-generated
date:               # ISO; defaults to today
headline:           # one line
hero_render:        # file path or URL — REQUIRED
secondary_renders:  # optional list
named_features:     # Vizcom features in play
named_people:       # internal Vizcom or external
named_customers:    # validated against allowed list
named_partners:     # Zellerfeld, Seymourpowell, etc.
named_designers:    # {name, location, handle}
designer_quotes:    # {quote, attribution, cleared_for_publication}
materials:          # list
consent_to_amplify: # bool (ugc_moment only)
confidential:       # bool — suppresses public channels
customer_under_nda: # bool — redacts customer publicly
posting_time:       # timestamp or null
channels_to_skip:   # list
```

### 0c — Pre-flight: required fields per signal type

Beyond `signal_type`, `slug`, `headline`, `hero_render`:

| signal_type | Required fields |
|---|---|
| `customer_win` | `named_customers` (on allowed list OR confirmation source attached) |
| `product_launch` | `named_features` (≥1) |
| `community_moment` | `named_designers` (≥1 with name + location/handle) |
| `ugc_moment` | `named_designers`, `consent_to_amplify` |
| `educator_activity` | school OR program OR `named_designers` with educator role |
| `milestone` | a `specific_fact` (dollar amount, count, date) |
| `event` | `date`, location_or_url, `event_mode` (pre/post) |
| `press_mention` | publication, link |
| `trend_response` | the_trend (one-line) |
| `cultural_moment` | the_moment (one-line) |

Always ask `customer_under_nda?` for Fortune-500 customer signals (even if on allowed list).
Always ask `cleared_for_publication?` for every designer quote found.

### 0d — Decide the state ([HALT] / [PROCEED] / [CLEAN])

After extraction and pre-flight, decide which of the three states applies. **Section 7 below is the authoritative definition** — read it on every run. Summary:

- **`[HALT]`** when a true blocker is present (missing render, unclear signal type, Fortune-500 customer with no NDA status, etc.). Write a partial signal file with `[NEEDS]` markers and return a chat message in the format `[HALT] Cannot draft. Missing: {list}. Add and re-run signals/{slug}.md.`
- **`[PROCEED]`** when only soft gaps remain (missing designer handle, location, secondary render, partial date). Draft normally; flag each gap as `[NEEDS CONFIRMATION: {field}]` inline + in `summary.md` under `## Open flags`.
- **`[CLEAN]`** when nothing is missing.

Claude Code subagents are non-interactive — there is no mid-run multi-choice prompt. The chat report (step 11 in the agent file) is how the agent communicates state back to the human.

**Phrasing reference for when the agent halts or names a soft flag:**

- **Signal-type confirmation** (when two types ≥40% plausible): "{type_a} or {type_b}?" / Options: type_a / type_b / both as separate drops.
- **Hero render missing:** "What's the path or URL to the hero render?" (Free-form.)
- **Designer quote clearance:** "I found a quote from {designer}: '{quote}'. Cleared?" / Options: Yes / Omit / Paraphrase without attribution.
- **Customer NDA status:** "Is {customer} cleared to be named publicly?" / Options: Name publicly / NDA — generic descriptor / Confidential — PR pitch only.
- **Named feature missing for launch:** "What feature(s) are launching?" (Free-form.)
- **UGC consent:** "Has {creator} consented to amplifying?" / Options: Yes / Asking now — hold / No — inspiration only.
- **Designer-or-team for customer wins:** "Credit a specific designer at {customer}, or team-level?" / Options: Name designer / Team-level / Get a name later.
- **Ambiguous double-signal:** "Two signals — separate drops or focus on one?" / Options: Separate / Focus on {type_a} / Focus on {type_b}.

### 0e — Similarity check (see Section 4)

### 0f — Construct and save the signal file

1. Build YAML frontmatter from the schema.
2. Build a free-form raw-facts body (lightly cleaned).
3. Write `signals/YYYY-MM-DD-{slug}.md` with:
   - `generated_by_intake: true` in frontmatter.
   - The frontmatter.
   - `## Raw input` (original or summary if long).
   - `## Clarifications` (Q&A for auditability).

The signal file is permanent and re-readable on a re-run.

---

## 3. What the agent CAN and CANNOT infer

| Field | Strategy |
|---|---|
| `signal_type` | Classify from content. Two types ≥40% → ask. |
| `slug` | Generate from date + headline. |
| `date` | Today, unless input specifies. |
| `headline` | Extract or paraphrase. |
| `hero_render` | **Cannot infer.** Always ask. |
| `secondary_renders` | Extract if listed. Optional. |
| `named_features` | Extract. Launch without feature → ask. |
| `named_people` / `customers` / `partners` / `designers` | Extract. Customer not on allowed list → ask for confirmation source. |
| `designer_quotes` | Extract. **Always ask `cleared_for_publication?`** |
| `materials` | Extract. |
| `consent_to_amplify` | **Cannot infer.** Always ask for `ugc_moment`. |
| `confidential`, `customer_under_nda` | **Cannot infer.** Always ask for Fortune-500 customer signals. |
| `posting_time` | Defaults to today + standard sequence. Ask only if implied. |
| `channels_to_skip` | Defaults to none. Ask only if implied. |

---

## 4. Similarity check (step 0e)

Vizcom posts ~weekly on blog and 1–3×/week on X/LinkedIn. Two similar drops too close dilutes the work. The agent compares the new signal against `training/recent_topics.md` and asks the user when it finds overlap. The user always makes the call.

### 4a — Topic signature

| Dimension | Source |
|---|---|
| `signal_type` | from schema |
| `designers` | `named_designers[].name` |
| `features` | `named_features` |
| `partners` | `named_partners[].name` |
| `form_factor` | inferred from materials/body/context (mule, lighting, bedside_electronics, keyboard, automotive_interior — see `training/recent_topics.md`) |
| `campaign_tags` | from input (`HoldYourIdeas`, `MakeItReal`) |

### 4b — Similarity rules (first match fires)

| # | Rule | Trigger | Severity |
|---|---|---|---|
| R1 | Same designer in last 30 days | designers overlap | high |
| R2 | Same form-factor 3+ times in last 14 days | form_factor already appears 2+ times | medium |
| R3 | Same feature in last 14 days | features overlap | high |
| R4 | Same signal_type in last 5 days | signal_type appears in last 5 days | low |
| R5 | Same campaign tag in last 7 days | campaign_tags overlap | low |
| R6 | Same partner in last 14 days | partners overlap | medium |

Severity:
- **high:** always ask, default "hold this drop"
- **medium:** ask, no default
- **low:** ask only unless overridden for this session

### 4c — Ask the user (canonical 3 options)

> **High severity:** "We featured {designer/feature} {N} days ago in {channel}. Same {dimension}. How should we handle it?"
> Options: 1. Post anyway — timely or deliberate series / 2. Hold this drop — wait until {last_date + 7 days} / 3. Combine into a recap or series post

> **Medium severity (form-factor):** "This is the {N+1}th {form_factor} drop in 14 days. Recent: {2–3 prior}. Continue or pace?"
> Options: 1. Continue / 2. Hold — recommend after {date} / 3. Combine into a recap

> **Low severity (same signal_type within 5 days):** "We posted a {signal_type} {N} days ago. Space it or run back-to-back?"
> Options: 1. Run back-to-back / 2. Space it — wait until {date}

Group up to 4 questions per call (rare — usually 1–2 fire).

### 4d — Log to `summary.md`

Whether or not a rule fires, log under a `## Similarity check` heading. Example:

```markdown
## Similarity check
Checked against training/recent_topics.md (last refresh: {date}).
- R1 (same designer in last 30 days): no match
- R2 (form-factor 3+ in 14 days): **MATCH — mule features: Catapill (Apr 14), Digits (May 1), Saman (May 8). 4th.**
  - User chose: Post anyway
- R3–R6: no match
```

### 4e — After the user answers

- **Post anyway / continue / run back-to-back** → proceed to 0f.
- **Hold this drop** → write signal file with `hold_until: {date}` in frontmatter, report drop is held, do not draft.
- **Combine** → write signal file with `combine_with: [{prior_slug}]`, halt drafting. (Recap mode is future work; v1 halts.)

### 4f — Updating `training/recent_topics.md`

After every drop publishes, the human (or future scheduled task) appends a new entry to the top of the table. The agent does not auto-update during a run.

---

## 5. Edge cases

- **Multiple signals in one input.** Ask once: "Separate drops or focus on one?" If separate, write two signal files; tell user to re-run on each. No auto-loop in v1.
- **Crisis / legal-sensitive.** Halt immediately. Escalate.
- **Insufficient input.** "What's the signal? Doc, URL, or one-line description?"
- **Competitor name in input.** Strip from raw-facts body; note in Clarifications. Drafting has its own no-competitor backstop.
- **Two rounds done, required field missing.** Halt: "I asked twice but still need {field}. Update input or signal file and re-run."
- **Confidential signal.** Proceed but drafting will produce only `pr_pitch.md` + `summary.md`.

---

## 6. Reporting

Phase B's <100-word chat summary must include: fields auto-extracted, clarifying questions asked, signal file path.

Example: "Intake auto-extracted 8 fields and asked 2 clarifying questions. Signal saved to signals/2026-05-13-saman-mule.md."

---

## 7. Order of operations

```
0a. Parse input
0b. Extract to schema
0c. Pre-flight required-fields check
0d. Clarifying questions (cap 2 rounds)
0e. Similarity check (training/recent_topics.md)
0f. Construct and save signal file
→ Phase B (see .claude/agents/vizcom-gtm-amplifier.md)
```

Similarity check (0e) runs **after** required-fields clarification (0d) — know what the signal is before checking against history.

---



## Three states — what the agent does after intake

After Phase 0 finishes extracting facts, the agent always lands in **exactly one** of three states. Be strict about which one — over-flagging confuses the human.

### State A — `[HALT]` (true blocker)

Halt ONLY when one of these is true:

1. `hero_render` is missing OR the file at the given path does not exist on disk.
2. `signal_type` cannot be determined — two or more types plausible at ≥40% confidence each AND no clear lead.
3. A required field for the signal type (per Section 0c table) is missing AND cannot be inferred from the input.
4. A Fortune-500 customer is named with no "cleared to name publicly" / NDA flag in the input.
5. Signal is crisis-related or legally sensitive.

When halting: write partial `signals/{slug}.md` with `[NEEDS]` markers, return a plain-text chat message:

```
[HALT] Cannot draft. Missing:
- hero render (drop at renders/{slug}/hero.jpg)
- signal type — could be {A} or {B}

Add the missing info and re-run on signals/{slug}.md.
```

### State B — `[PROCEED]` (soft flag — drafting still happens)

Proceed and flag in body + `summary.md ## Open flags` when:

1. Designer location or IG/X handle missing (creator-story signals).
2. Designer quote in input but no explicit clearance note → omit the quote, flag in summary.
3. Customer named but not on allowed list AND has a confirmation source URL attached → use the customer name, flag for human verification.
4. Partial date ("next week," "Q4") → proceed with the relative date, flag.
5. Secondary renders mentioned but not present on disk → use only the hero, flag.

Chat report:

```
[PROCEED] Drafted with {N} soft flag(s): {short list}. See outputs/{slug}/summary.md ## Open flags.
```

### State C — `[CLEAN]` (no flags)

When all required fields are present and complete. Most well-formed signals (Samples 1, 4) should land here. The chat report is:

```
[CLEAN] Drafted. 0 flags. See outputs/{slug}/preview.html.
```

### Rule of thumb

If the human can publish the drop without going back to fix anything → CLEAN.
If the human can publish but should glance at the flags first → PROCEED.
If the human has to add information before publishing makes sense → HALT.

**Do not invent "soft" reasons to flag.** If the field isn't required by the signal type and isn't actually missing, don't surface it.

## 8. After intake

Once the signal file is written and pre-flight + similarity-check pass, the agent proceeds to **Phase B: Drafting** as described in `.claude/agents/vizcom-gtm-amplifier.md`. The agent reads the matching template from `templates/{type}.md` (see `core_rules.md` Section 5) and drafts the channels in order.
