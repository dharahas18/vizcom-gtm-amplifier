# Recent Vizcom Topics (Rolling Log)

The Vizcom GTM Amplifier reads this file during intake — specifically the **similarity check** step (Section 7 of `intake.md`) — to catch topic overlap between a new signal and recent Vizcom posts.

This file is the lookup data. The rules for what counts as "similar" live in `intake.md` Section 7.

**Refresh cadence:** weekly. Keep ~30 days of posts.
**Last refresh:** 2026-05-13 (initial population from the authenticated X + LinkedIn scrape; covers Apr 7 → May 9, 2026 + Oct 29, 2025 Series B).

---

## Active campaigns / series

| Series tag | What it is | Recent entries |
|---|---|---|
| **Hold Your Ideas** | Designer-feature series; sketch → physical object | Liven (Feb 2026), Exhaust Light (Mar 2026), Saman (May 2026), Digits (May 2026), Catapill (Apr 2026), Concrete keyboard (Apr 2026) |
| **Make It Real** | Production-handoff stories | Fabracers (Jan 2026) |
| **Vizcom Worlds** | Community event series (luma.com calendar) | Apr 21, 2026 event drop |

---

## Last 30+ days of posts

| Date | Channel | Type | Topic signature | Designers / features named | Form-factor / theme tags |
|---|---|---|---|---|---|
| 2026-05-09 | X (UGC mention, not Vizcom-authored) | ugc_mention | Smart Dropper amplified by @amypretzel | @amypretzel | feature mention, voice |
| 2026-05-08 | LinkedIn | community_moment | The Saman | Andrew Moya, Juan Rujana | mule, footwear, Pre-Columbian, Zellerfeld |
| 2026-05-08 | X | community_moment | The Saman | Andrew Moya, Juan Rujana | mule, footwear, Pre-Columbian, Zellerfeld |
| 2026-05-08 | blog | product_launch | Credits launch | (no designer) | pricing, usage system |
| 2026-05-05 | LinkedIn | product_launch | Collections | (no designer) | asset library, references |
| 2026-05-01 | X | community_moment | Digits | Kolbe Correia | mule, footwear, sculptural, fingerprint |
| 2026-04-30 | X | brand_voice | "Most ideas die in sketchbooks" tagline | (n/a) | aphorism, recurring line |
| 2026-04-21 | X | event | Vizcom Worlds events drop | (community) | event series, luma |
| 2026-04-17 | X | community_moment | Liven (BTS) | Otto Loikkanen | bedside electronics, Finland, sunrise alarm |
| 2026-04-15 | X | product_launch | Speech-to-text + Prompt suggestions | speech_to_text, prompt_suggestions | input, voice control |
| 2026-04-14 | X | community_moment | Catapill | Prithviraj Taware | mule, footwear, biomimetic, Zellerfeld |
| 2026-04-14 | X | event | Seymourpowell webinar announce | Seymourpowell | webinar, partner event |
| 2026-04-13 | X | brand_voice | "just vibe your way through it" | (n/a) | aphorism |
| 2026-04-10 | X | community_moment | The Exhaust Light (BTS) | Julius / @julius.works | lighting, metalwork, Berlin, stainless steel |
| 2026-04-07 | blog | community_moment | Concrete keyboard | Emil Lukas | hardware, employee creator, building story |
| 2026-03-31 | blog | product_launch | Extract, Try On, Export | Extract, Try_On, Export | multi-feature toolkit |
| 2026-03-13 | blog | community_moment | The Exhaust Light (long-form) | Julius | lighting (full feature) |
| 2026-02-20 | blog | community_moment | Liven Sunrise Clock (long-form) | Otto Loikkanen | bedside (full feature) |
| 2026-01-23 | blog | community_moment | Fabracers Derby Cars | Ádám Miklósi | modular, toy car, Hungary, Make It Real |
| 2025-12-22 | blog | milestone | 2025 Year in Review | (no specific designer) | year-end, community |
| 2025-11-12 | blog | product_launch | New Vizcom Studio | Studio | UI overhaul |
| 2025-10-29 | X | milestone | $27M Series B | @RadicalVCFund (lead), Index, Unusual, Basis Set | funding |

---

## Patterns to watch (as of 2026-05-13)

These are observed clusters from the scrape, useful for the similarity check:

- **Mule features:** Catapill (Apr 14), Digits (May 1), Saman (May 8) — three in 24 days, two within 8 days. The agent should flag the 4th mule signal aggressively.
- **Pricing / usage launches:** Credits (May 8), Collections (May 5) — two launches in 3 days. The agent should hold new launches ~10 days unless they're tied to a clear campaign.
- **Footwear-with-Zellerfeld:** Catapill, Saman — Zellerfeld appears repeatedly as the production partner. If a third Zellerfeld-named signal arrives soon, ask if it's a deliberate series.
- **Hold Your Ideas series cadence:** roughly biweekly long-form blog + intermittent BTS short-forms. If a new Hold Your Ideas signal arrives < 7 days after the last, the agent should suggest holding.
- **Designer-feature overall cadence:** roughly every 5–10 days. If you've shipped one in the last 5 days, the agent should ask whether the new one can wait.

---

## Schema (for adding new entries)

When refreshing this file, add new rows at the top of the table. Each row is:

```
| YYYY-MM-DD | channel | signal_type | topic signature (short) | named designers/features (comma-sep) | form-factor / theme tags (comma-sep) |
```

The form-factor tags are the agent's primary similarity dimension. Use canonical tags:

- footwear taxonomy: `mule`, `sneaker`, `boot`, `slide`, `sandal`, `runner`
- product taxonomy: `bedside_electronics`, `lighting`, `keyboard`, `audio_object`, `homeware`, `automotive_interior`, `automotive_exterior`, `consumer_electronics`
- partner tags: `Zellerfeld`, `Seymourpowell`, etc.
- feature tags: `Workbench`, `Modify`, `Animate`, `Studio`, `Extract`, `Try_On`, `Export`, `Speech_to_text`, `Prompt_suggestions`, `Collections`, `Smart_Dropper`, `Free_View`, `Adaptive_Canvas`, `Credits`
- campaign tags: `HoldYourIdeas`, `MakeItReal`, `VizcomWorlds`

The wider this tag vocabulary, the better the similarity check.

---

## How the agent uses this file

During intake step 0e, the agent:

1. Reads this file's table.
2. Extracts the new signal's topic signature (form-factor, designer, features, campaign tags).
3. Applies the rules in `intake.md` Section 7.
4. If a match fires, logs the match in `summary.md` under `## Similarity check` with the three standard options listed (**post anyway / hold this drop / combine into a recap or series**) and the recommended one. The agent always proceeds with drafting; the human reads summary.md and decides whether to publish, hold, or rewrite. (Claude Code subagents are non-interactive — no mid-run prompts.)
5. Logs the match check (hit or no hit) in `summary.md` under `## Similarity check`.

---

## Maintenance

The corpus refresh cadence (every 90 days, per `workflow.md` Section 6) should also re-scrape the @Vizcom_ and @vizcomhq feeds and rebuild this table. A weekly lighter refresh is recommended if Vizcom's posting cadence picks up.
