# Run all samples

Two ready-to-paste prompts for batch-testing the agent across all five sample inputs.

---

## Sequential (recommended for first run)

Paste this into Claude Code. The agent runs once per sample; you'll answer clarifying questions per signal as they come up.

```
Run vizcom-gtm-amplifier sequentially on each of these signal files, one after the other:

samples/01-product-launch-smart-dropper.md
samples/02-community-moment-velocity-skateboard.md
samples/03-customer-win-honda.md
samples/04-milestone-one-million-designers.md
samples/05-event-design-week-amsterdam.md
samples/06-thin-signal-clarification.md

For each one, run the full Phase 0 + Phase B flow (intake, clarifying questions, similarity check, drafting, self-check), save the six output files to outputs/{slug}/, and print the standard <100-word report before moving to the next signal.
```

End state: five folders under `outputs/`, one per signal. Expect 5–10 clarifying questions across the batch.

---

## Parallel (fast smoke test)

Use the default answers suggested in each sample's `## Expected behavior` section. Faster, but noisier in chat.

```
Run vizcom-gtm-amplifier in parallel on all five samples in samples/. For any clarifying question, use the recommended answer noted in that sample's "Expected behavior" section and proceed without halting. After all five runs complete, summarize the batch in one paragraph: which signals produced clean drops, which fired similarity-check flags, and any [NEEDS CONFIRMATION] flags across the batch.
```

End state: same five folders, faster runtime, less interactive control.

---

## What to expect

For each sample, look at `outputs/{slug}/summary.md` first. Verify:

- Signal type classified correctly (matches the type named in the sample file header).
- Auto-fix log makes sense (some samples — like Sample 4 — may trigger a length auto-fix).
- Similarity check ran and logged its result.
- Open flags are honest, not invented (e.g., Sample 5 should flag the 2 TBD panelists; Sample 4 should flag the embargo timing).

Then read each output file. The voice should be indistinguishable from the corpus.

---

## A note on the similarity check during a batch

The similarity check reads from `training/recent_topics.md`, **not** from `outputs/`. So running Sample 2 (skateboard) won't see Sample 1 (Smart Dropper) as a "recent post" — `recent_topics.md` reflects what's actually been published, not what's been drafted in this batch.

If you want each sample to see the previous one in the batch, manually add a row to `training/recent_topics.md` between runs. (For test purposes, this isn't usually necessary.)

---

## After the batch

If everything looks good, the agent is ready for real signals. Delete the dry-run output (`outputs/2026-05-08-saman-mule-dryrun/`) and the batch outputs once you've reviewed them — or keep one as a reference for future voice calibration.
