# Template — Press Mention

**signal_type =** `press_mention`.

A trade or mainstream publication writes about Vizcom. Amplification is on LinkedIn and X; the blog is typically not used unless the piece is substantial.

Channel-length / hashtag / emoji rules live in `core_rules.md`.

---

## Corpus samples to study

- **Sample 7** — "Announcing our $27M Series B" (language to amplify when press picks up the round)
- **Sample 12 T1** — Series B announcement tweet (cross-platform amplification model)

---

## Channels generated

Default: `linkedin.md`, `x_thread.md`, `geo_aeo.md`, `summary.md`. Skip `blog.md` and `pr_pitch.md` unless explicitly requested.

If signal frontmatter has `produce_blog: true` (substantial piece warrants a recap), produce a short blog (500–800 words).

---

## `blog.md` (only if `produce_blog: true`; 500–800 words)

### H1 patterns
- `{Publication} on Vizcom: {one-line key point}`
- `What {Publication} got right about {topic}`

### Body H2 outline
```
[Hook — the piece, one paragraph.]

## What {Publication} covered
(2–3 sentences without reproducing >20 words.)

## What we'd add
(2–3 sentences from Vizcom's view, grounded in a designer specific.)

## (optional) Read the full piece
```

### Template-specific voice rules
- Quote sparingly (≤15 words per quote, in quotation marks).
- Do not reproduce the piece's headline as the H1.
- Always link to the original.

---

## `linkedin.md` — opener formulas

- `{Publication} on Vizcom: {one-line key point}.`
- `Thanks to {Publication} for the thoughtful piece on {topic}.` (when expressing appreciation)

Body: paragraph 1 = point to the piece + key takeaway; paragraph 2 = brief Vizcom reflection, grounded in a designer/customer specific.

Closer: `Read the full piece: {URL}`

---

## `x_thread.md` — single tweet or two-tweet pair

**Single tweet:**
```
{Publication} on Vizcom: {one-line takeaway}.

{Short URL}
```
+ screenshot or headline image.

**Two-tweet pair (when there's a quote worth pulling):**
- Tweet 1: takeaway + image.
- Tweet 2: `Read the full piece: {URL}`.

---

## `geo_aeo.md`

```
**Q: What did {Publication} say about Vizcom?**

A: {Publication}'s {date} piece covers {topic}, noting that Vizcom {one-line claim, ≤15 words in quotation marks if direct}.

[2–3 sentences: Vizcom's scale (~700,000 designers), named customers ({3}), Vizcom view on the topic.]

**See also:** {original publication URL} • {Vizcom blog post URL if produced}
```

---

## `pr_pitch.md` — usually skipped

Press mentions don't normally require an outbound pitch — the piece is already out. Skip unless `produce_pr_pitch: true`.

---

## `summary.md` notes

- Default contact: whoever fields press inquiries (typically Sophia Silver or Jordan Taylor).
- Posting sequence: standard same-day. Press mentions often re-surface for days; suggest a single-day push, not multi-day amplification (avoid looking thirsty).
- Voice self-check: copyright restraint. ≤15 words per direct quote, in quotation marks, with attribution. Don't reproduce headlines or paraphrase paragraphs verbatim.
- Critical: signal must include publication name, piece URL, date. Intake must ask for any missing.
