# Sample 1 — Product launch (Smart Dropper)

**Signal type:** `product_launch`
**Input style:** One-line chat description (the simplest path)
**What it tests:** Minimal clarifying questions, product-launch template, single-tweet X variant

**Run with:**
```
Run vizcom-gtm-amplifier on samples/01-product-launch-smart-dropper.md
```

Or paste the signal block below into chat after `Run vizcom-gtm-amplifier — here's the signal:`

---

We just shipped Smart Dropper. It absorbs the vibe of any reference image — point it at a retro Mac, a tamagotchi, or your favorite album cover, and it applies the style to your design.

Going live today, May 13, 2026. Available for all users.

Hero render: samples/renders/smart_dropper_hero.png
Demo video: https://youtu.be/smart-dropper-demo

---

**What the agent should ask (expected clarifying questions):**

1. Probably none — the input is self-contained for a product launch.

**Expected behavior:**

- signal_type: `product_launch` (high confidence)
- Template: `templates/product_launch.md`
- Similarity check should flag R4 (last `product_launch` was Credits on May 8 — 5 days ago) and ask whether to pace this drop.
- Output should match the captured @Vizcom_ register: aphoristic hook + "now live in Vizcom" tail.
