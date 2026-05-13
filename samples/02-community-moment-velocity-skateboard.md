# Sample 2 — Community moment (Velocity skateboard by Maya Okonkwo)

**Signal type:** `community_moment`
**Input style:** Internal email/note from the community team
**What it tests:** Creator-story template, designer-quote clearance check, a new form-factor (not a mule — important for similarity check), African design community surfacing

**Run with:**
```
Run vizcom-gtm-amplifier on samples/02-community-moment-velocity-skateboard.md
```

---

Subject: New project worth featuring — Velocity skateboard, Maya Okonkwo, Lagos

Hi team,

Wanted to share Maya Okonkwo's new project. She's an industrial designer in Lagos who just finished a skateboard called Velocity — the deck is shaped from a single piece of cast bronze, with the grip surface micro-textured to look like rippled water. She said she wanted to capture the moment a wave breaks.

Materials:
- Cast bronze deck
- Polyurethane wheels (off-the-shelf, 56mm, 78A)
- Brushed steel trucks (custom)
- Hand-finished, single-edition piece

Workflow notes from Maya:
- Started in Vizcom Workbench with a CAD line drawing from Rhino
- Used Modify heavily to test ~20 surface-texture variations in an afternoon
- Used Instant Render to set the bronze patina before casting
- Animated the final piece for her portfolio

Production: Maya partnered with a foundry in Accra to lost-wax cast the bronze deck. Total weight: 11.4 kg (heavy on purpose — the project is about presence, not skatepark performance).

Maya's links:
- Instagram: @mayaokonkwo.design
- Website: mayaokonkwo.com

Hero render: samples/renders/velocity_hero.png
Secondary renders: samples/renders/velocity_surface_detail.png, samples/renders/velocity_truck.png

She's cleared this quote for publication:

> "Vizcom let me make decisions about texture I would have had to leave to chance. By the time I sent files to the foundry, I had already lived with the surface for two weeks."
— Maya Okonkwo

— Kim Lu

---

**What the agent should ask:**

1. The quote is cleared — agent should detect "she's cleared this quote" and proceed.
2. No NDA flag needed (not a Fortune-500 customer).
3. Similarity check should fire R5 (`HoldYourIdeas` posts in last 7 days — Saman May 8, Digits May 1) and possibly flag for pacing. Different form-factor (skateboard, not mule) means R2 doesn't fire.

**Expected behavior:**

- signal_type: `community_moment` (high confidence)
- Template: `templates/creator_story.md`
- Blog should follow Hold-Your-Ideas creator-story structure with Maya's quote as a blockquote.
- Credits footer: Maya Okonkwo / Lagos, Nigeria / Industrial Design / Vizcom / cast bronze + brushed steel + polyurethane.
