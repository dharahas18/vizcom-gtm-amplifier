# Prioritization Framework
**With consultant critique, sourced data, score rationale, and final decision.**
**May 2026. 15 AI companies. Synthesized from 30 research files.**

---

## Consultant critique: what works and what doesn't

### What works
1. **Anchored thresholds.** Each score has a data threshold rather than gut feel. Traction = 3 only when ARR > $5M confirmed OR named F500 with retention.
2. **Urgency factor.** Most VC scorecards omit this. Painkiller-vs-vitamin is the single strongest predictor of conversion rate (80%+ of SaaS unicorns are painkillers).
3. **Community signal scored explicitly.** Forces specificity (named programs, Discord growth, recruiter signals) instead of vague "great community."
4. **Penalizes inferred numbers.** Reve's $1.9B from secondary sources scores 1 on traction, not 3.

### What's weak and how to fix it

| Weakness | Why it matters | Fix |
|---|---|---|
| **No confidence interval per score.** A 3 on traction with 5 primary sources is more reliable than a 3 inferred from 1 secondary source. | Two companies can have the same total score with very different evidence quality. | Add a confidence column: High/Med/Low per cell. |
| **Weights are intuited, not validated.** Why 18% urgency vs 15% community? Not derived from outcome data. | Sensitive to weight choice. Sensitivity analysis missing. | Run sensitivity test: re-rank with ±5% on each weight. If top 3 don't change, framework is robust. |
| **Some factors overlap.** Community signal partially correlates with wedge defensibility (community = switching cost). Risk of double-counting. | Inflates scores for community-strong companies. | Either reduce community weight or explicitly note overlap and adjust. |
| **No regulatory or geographic factor.** Flint has FERPA/COPPA exposure. Rasa banks have AML/KYC compliance. Beeble is South Korea-based affecting M&A optionality. | Material risk for specific companies. | Add as half-weighted modifier (e.g., -10% penalty if material regulatory exposure). |
| **Customer reference quality not captured.** A logo on a wall ≠ deep deployment. | Inflates traction scores for companies with logo walls but shallow contracts. | Penalize traction score if logos are unverified or design-partner-only. |
| **No churn/retention proxy.** Long-term value depends on it. | Companies with high acquisition but unverified retention score the same. | Add retention proxy (G2 reviews trajectory, App Store star count growth, customer story dates). |
| **Time-to-data-update.** Companies move fast. Some data points are 6+ months old. | Stale data leads to outdated ranking. | Add a "data freshness" column: last verified date. |
| **No bias check on category vintage.** AI infra in 2026 may be overscored vs adjacent categories with quieter growth. | Pattern matching to current hype. | Stress test: re-score in a scenario where AI valuations compress 50%. |
| **No founder-commitment flag** (we removed founder factor entirely). Beeble had an unverified red flag on founder commitment that mattered. | Material risk gets buried. | Add a binary "flag" column for unverified material risks, separate from scoring. |
| **Tier boundaries are arbitrary.** Why is 80% "Tier 1" vs 75% "Tier 2"? Not validated against outcome data. | Threshold gaming risk. | Either drop tiers and rank only, or anchor tiers to "in-the-money" outcomes (e.g., > 80% = > 60% historical hit rate for IC approval). |

### Highest-leverage single improvement
**Add data freshness + confidence per cell.** Two companies scoring 80% are not equivalent if one has 4 primary sources and the other has 2 secondary inferences. This is the single change a real consultant would push hardest on.

---

## The 7 factors and weights (recap)

| Factor | Weight |
|---|---:|
| Urgency of pain | 18% |
| Traction evidence | 18% |
| Community building signal | 15% |
| Wedge defensibility | 15% |
| Market opportunity | 12% |
| Scope for expansion | 12% |
| Competitive position | 10% |

---

## Why 3 vs 2 vs 1: the threshold logic

### Urgency
- **Score 3 (Painkiller):** Customer loses money or hours daily without the tool. Active search behavior visible in Reddit/forum posts. Tool replaces a manual process that's a known time-suck. Example: Vizcom replaces 4-8 hour render workflows that designers were already searching for AI tools to solve.
- **Score 2 (Vitamin with ROI):** Customer sees clear value but isn't actively searching. Tool offers measurable lift. Example: Entire (agent context capture is valuable but not blocking work today).
- **Score 1 (Vitamin diffuse):** Customer can rationalize using the tool but has no acute pain. Long sales cycle. Example: Atuin shell history syncing for single-machine users.

### Traction
- **Score 3:** Confirmed ARR > $5M with primary sources OR named Fortune-500 customers with retention or expansion data. Recent Series A+ funding closing with multiple corroborating sources. Examples: Vizcom (Series B Oct 2025, F500 customers, 75% YoY user growth), Tigris ($750K ARR + Spark/a16z Series A), Rasa (180 employees + named F500 banks).
- **Score 2:** Inferred ARR $1M-$5M OR named SMB customers OR strong growth proxies without confirmed dollars. Example: BAML (named customers but no confirmed ARR figure).
- **Score 1:** No revenue OR vanity metrics only OR unverified funding figures. Example: Reve (lost Artificial Analysis #1, $1.9B unverified) and Primitive (pre-launch).

### Community signal
- **Score 3:** Active Discord/forum with growing membership documented (e.g., BAML 700→2,400 in 2025). Named community programs (Design Advocates, Student Ambassadors). Recruiter outbound for tool-specific skills appearing in the wild. Multi-channel community footprint. Example: Vizcom (@DesignersPen 80K + Discord + Design Decoded series + Design Advocates).
- **Score 2:** Founder-led community presence with some events. Some Discord/social engagement but no growth-rate data. Example: Solvely (TikTok creator network but no Discord).
- **Score 1:** Generic positioning. No community footprint visible. Quiet news cycle. Example: Hallway (post-pivot, no v-tuber community retained).

### Wedge defensibility
- **Score 3:** Technical wedge that competitors cannot copy within 12 months. Patented, deeply trained, or architecturally distinct. Example: Vizcom (material-aware sketch-to-render), Tigris (20x throughput, public methodology), Beeble (foundational PBR model on-device).
- **Score 2:** Workflow or UX wedge copyable in 6-12 months. Example: Solvely (step-by-step + photo input, replicable by ChatGPT in iteration).
- **Score 1:** Wedge already commoditized or perished. Example: Reve (lost Artificial Analysis #1 lead within 12 months).

### Market opportunity
- **Score 3:** TAM > $10B with > 20% CAGR. Categories with structural growth. Example: AI design tools $8B 2026 at 22% CAGR (Vizcom), conversational AI $50B+ TAM (Rasa).
- **Score 2:** TAM $1B-$10B OR moderate growth 10-20% CAGR. Example: K-12 edtech (Flint), meeting AI (Quill).
- **Score 1:** TAM < $1B or shrinking. Example: Atuin shell-tooling niche, Hallway embeddable-mascot market.

### Scope for expansion
- **Score 3:** Multi-vertical or multi-segment expansion path with named adjacent markets. Wedge can become platform. Example: Vizcom (auto → footwear → consumer goods → packaging → aerospace with customer-mix proof), BAML (DSL → workflow IDE → eval platform → observability).
- **Score 2:** Adjacent expansion possible but unproven. Example: Flint (independent schools → public districts → international, but public-district path uncertain vs MagicSchool).
- **Score 1:** Niche-locked. Example: Hallway (mascot AI doesn't naturally expand beyond brand-mascot use case).

### Competitive position
- **Score 3:** At scale comparable to or exceeding direct competitors. Example: Vizcom 700K users vs Krea's smaller specialty base.
- **Score 2:** 25-50% of leading competitor's scale OR specialty differentiator. Example: Rasa specialty position vs Sierra ($4.5B); BAML differentiation vs LangChain.
- **Score 1:** < 25% of competitor scale OR getting outpaced. Example: Solvely (vs ChatGPT), Parasail ($42M vs Fireworks $4B), Flint (vs MagicSchool 10x bigger), Quill (vs Granola $1.5B).

---

## Company signals with sources

### Tier 1 (Weighted score ≥ 85%)

#### Tigris Data — 97%

| Factor | Score | Data point | Source |
|---|:-:|---|---|
| Urgency | 3 | Customers report saving 85% on storage costs (Fal.ai case study) | [Tigris Fal case study](https://www.tigrisdata.com/blog/case-study-falai/) |
| Traction | 3 | $750K ARR Sep 2025, 4,000+ customers, $25M Series A | [SiliconAngle Series A](https://siliconangle.com/2025/10/09/tigris-data-raises-25m-ai-optimized-cloud-storage-service/), [a16z post](https://a16z.com/announcement/investing-in-tigris/) |
| Community | 3 | HN front page on benchmark methodology, Fly.io ecosystem default | [HN benchmark thread](https://news.ycombinator.com/item?id=44953971) |
| Wedge | 3 | 20x throughput vs Cloudflare R2 on small objects, published methodology | [Tigris benchmark](https://www.tigrisdata.com/blog/benchmark-small-objects/) |
| Market | 3 | Object storage market multi-$10B; AI workload sub-segment growing 22% CAGR | [Mixpeek 2026 comparison](https://mixpeek.com/blog/object-storage-comparison-2026) |
| Expansion | 3 | AI-storage → general → CDN/edge → cross-cloud sync (4 named adjacent markets) | [Tigris docs](https://www.tigrisdata.com/docs/) |
| Competition | 2 | AWS S3 + Cloudflare R2 incumbents; Backblaze + Wasabi alternatives | [SiliconAngle](https://siliconangle.com/2025/10/09/tigris-data-raises-25m-ai-optimized-cloud-storage-service/) |

#### Vizcom — 97%

| Factor | Score | Data point | Source |
|---|:-:|---|---|
| Urgency | 3 | Renders that took hours now in seconds; founder origin from "designer doing daily renders" | [Index Ventures memo](https://www.indexventures.com/perspectives/inside-vizcoms-vision-to-transform-industrial-design-with-ai/) |
| Traction | 3 | 700K users, 75% YoY growth, F500 customers (Ford, Stellantis, Honda, Sonos, Gulfstream), $27M Series B | [Vizcom Series B blog](https://vizcom.com/blog/announcing-our-series-b), [Vizcom homepage](https://vizcom.com/) |
| Community | 3 | @DesignersPen 80K Instagram (pre-Vizcom), Design Decoded video series, Discord, Design Advocates program, Vizcom for Educators | [Vizcom Series B](https://vizcom.com/blog/announcing-our-series-b), [Vizcom homepage](https://vizcom.com/) |
| Wedge | 3 | Material-aware sketch-to-render with spatial 3D awareness Firefly lacks | [thesmartmakers 2026 review](https://thesmartmakers.com/vizcom-review-2026-the-ai-tool-that-finally-understands-industrial-designers/) |
| Market | 3 | AI-powered design tools $6.74B (2025) → $8.22B (2026) at 22% CAGR | [Business Research Co.](https://www.thebusinessresearchcompany.com/report/ai-powered-design-tools-global-market-report) |
| Expansion | 3 | Auto → footwear → consumer goods → packaging → aerospace; expansion proven in customer mix | [Vizcom homepage logo wall](https://vizcom.com/) |
| Competition | 2 | Adobe Firefly bundled distribution risk; Krea on real-time | [openart Midjourney vs Krea](https://openart.ai/blog/post/midjourney-vs-krea) |

#### Mem0 — 88%

| Factor | Score | Data point | Source |
|---|:-:|---|---|
| Urgency | 3 | Production AI agents break without memory daily; cited by Datadog/Supabase/PostHog/W&B founders as angel investors | [Mem0 Series A blog](https://mem0.ai/series-a) |
| Traction | 3 | 48K GitHub stars, 14M PyPI downloads, 80K developers, AWS Strands Agent SDK exclusive partnership | [TechCrunch Oct 2025](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/), [Mem0 series-a page](https://mem0.ai/series-a) |
| Community | 3 | Active Discord; CrewAI, Flowise, Langflow native integrations; dense angel network | [Mem0 Series A](https://mem0.ai/series-a) |
| Wedge | 2 | Hybrid vector+graph+KV store. Loses public benchmarks to Zep (49% vs 63.8% LongMemEval) and Letta (~83%) | [Zep benchmark audit](https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/) |
| Market | 3 | AI memory layer emerging $10B+ as agent infra | [GrowthNavigate AI SaaS stats](https://www.growthnavigate.com/b2b-saas-statistics) |
| Expansion | 3 | Memory → agent state → multi-tenant context → personalization platform | [Mem0 Series A blog](https://mem0.ai/series-a) |
| Competition | 1 | Zep + Letta both technically ahead on benchmarks; Mem0 wins distribution but loses technical race | [Asymptotic Spaghetti comparison](https://medium.com/asymptotic-spaghetti-integration/from-beta-to-battle-tested-picking-between-letta-mem0-zep-for-ai-memory-6850ca8703d1) |

#### Rasa — 88%

| Factor | Score | Data point | Source |
|---|:-:|---|---|
| Urgency | 3 | Banks/telcos cannot use cloud AI for regulated workflows | [TechCrunch Feb 2024](https://techcrunch.com/2024/02/14/rasa-an-enterprise-focused-dev-platform-for-conversational-genai-raises-30m/) |
| Traction | 3 | 180 employees, 2x ARR growth 2023, named F500 (Adobe, Dell, Amex, Deutsche Telekom, "two of three top global banks") | [TechCrunch Feb 2024](https://techcrunch.com/2024/02/14/rasa-an-enterprise-focused-dev-platform-for-conversational-genai-raises-30m/), [Tracxn Rasa](https://tracxn.com/d/companies/rasa/__JzqUAUUK-mh039Hy6yIM6AzXO07uWa7zZvXQL6Y8Vvo) |
| Community | 3 | 50M+ OSS downloads, 750+ contributors, 15K+ forum members, Forrester Wave 2026 inclusion | [Rasa community](https://rasa.community/), [Forrester Wave 2026](https://cxfoundation.com/blog/forrester-wave-conversational-ai-2026) |
| Wedge | 2 | CALM patented engine (LLM + deterministic). On-prem-first. AI-native peers (Sierra, Decagon) catching up. | [Rasa CALM page](https://rasa.com/calm) |
| Market | 3 | Conversational AI enterprise $50B+ TAM | [GrowthNavigate AI SaaS](https://www.growthnavigate.com/b2b-saas-statistics) |
| Expansion | 2 | Text → voice → multimodal. On-prem stays defensible niche but bounded. | [Rasa Platform](https://rasa.com/product/rasa-platform/) |
| Competition | 2 | Sierra ($4.5B), Decagon ($1.5B) bigger but cloud-only. Rasa $35K Growth vs Sierra $150K. | [Rasa Sierra alternatives blog](https://rasa.com/blog/sierra-ai-alternatives) |

#### BAML — 87%

| Factor | Score | Data point | Source |
|---|:-:|---|---|
| Urgency | 3 | LLM output parsing failures break production daily; named customers (VetRec, Coldreach) explicitly cite this | [Vaibhav 5-years-12-pivots blog](https://boundaryml.com/blog/5-years-12-pivots) |
| Traction | 2 | YC W23. GitHub 1k→7k stars in 2025. Named customers but ARR not confirmed. | [BAML GitHub](https://github.com/BoundaryML/baml), [Vaibhav retrospective](https://boundaryml.com/blog/5-years-12-pivots) |
| Community | 3 | Discord 700→2,400 in 2025. 400-person Saturday workshops. Recruiter outbound for "BAML engineers" appearing in the wild. | [Vaibhav retrospective](https://boundaryml.com/blog/5-years-12-pivots) |
| Wedge | 3 | SAP algorithm in Rust + multi-language client (Python/TS/Ruby/Go/Java/C#/Rust). Patented approach. | [SAP technical blog](https://boundaryml.com/blog/schema-aligned-parsing), [BAML GitHub](https://github.com/BoundaryML/baml) |
| Market | 2 | LLM dev tools subset of $100B+ AI infrastructure market | [GrowthNavigate AI SaaS](https://www.growthnavigate.com/b2b-saas-statistics) |
| Expansion | 3 | DSL → workflow IDE → eval platform → observability (named in roadmap) | [Vaibhav retrospective](https://boundaryml.com/blog/5-years-12-pivots) |
| Competition | 2 | LangChain (Python-only wrappers), Instructor, OpenAI strict mode | [techsy.io comparison](https://techsy.io/en/blog/best-llm-structured-output-libraries) |

### Tier 2 (Weighted score 65-85%)

#### Beeble — 83%

| Factor | Score | Source |
|---|:-:|---|
| Urgency | 3 | [TechCrunch Beeble](https://techcrunch.com/2024/07/10/beeble-ai-raises-4-75m-to-launch-a-virtual-production-platform-for-indie-filmmakers/) (VFX deadlines) |
| Traction | 2 | [Beeble Superman & Lois case](https://beeble.ai/showcase/superman-lois-relighting-vfx) (Boxel Studio) |
| Community | 3 | [CG Channel SwitchLight 3.0](https://www.cgchannel.com/2025/11/beeble-launches-switchlight-3-0/), [Nuke plugin showcase](https://beeble.ai/showcase/nuke-compositing-academy) |
| Wedge | 3 | [CineD Beeble Studio](https://www.cined.com/beeble-studio-launches-with-local-4k-ai-relighting-and-switchlight-3-0-engine/) (foundational AI model) |
| Market | 2 | [TechCrunch Beeble](https://techcrunch.com/2024/07/10/beeble-ai-raises-4-75m-to-launch-a-virtual-production-platform-for-indie-filmmakers/) |
| Expansion | 2 | [Beeble showcase](https://beeble.ai/showcase) (VFX, game art, architecture viz) |
| Competition | 2 | Wonder Dynamics → Autodesk 2024 (industry knowledge) |

#### Solvely — 75%

| Factor | Score | Source |
|---|:-:|---|
| Urgency | 3 | [Solvely homepage](https://solvely.ai/) (homework due tonight; 10M+ students) |
| Traction | 3 | [Latka Solvely](https://getlatka.com/companies/solvely.ai), [ARR Club](https://www.arr.club/signal/solvely-ai-arr-at-6m-up-6x-yoy) ($6M ARR, 6x YoY) |
| Community | 2 | [App Store Solvely](https://apps.apple.com/us/app/solvely-ai-study-tools/id6446930976) (31K reviews; no Discord/forum) |
| Wedge | 2 | [Solvely.ai](https://solvely.ai/), [HomeworkRev review](https://homeworkrev.com/solvely-review) |
| Market | 2 | [GrowthNavigate edtech stats](https://www.growthnavigate.com/b2b-saas-statistics) |
| Expansion | 2 | [Solvely blog](https://solvely.ai/blog/prosumer-ai-40) (K-12 → college path partial) |
| Competition | 1 | ChatGPT EDU structural threat (industry knowledge) |

#### Flint — 74%

| Factor | Score | Source |
|---|:-:|---|
| Urgency | 3 | [Flint Series A](https://flintk12.com/blog/series-a) (teachers overwhelmed) |
| Traction | 2 | [AlleyWatch Flint](https://alleywatch.com/2025/11/flint-ai-powered-personalized-adaptive-learning-k12-education-platform-sohan-choudhury/), [Cognita case](https://www.flintk12.com/press/cognita-partners-with-flint) |
| Community | 3 | [Flint Series A](https://flintk12.com/blog/series-a) (Student Ambassadors, Refer-a-School, ASU GSV) |
| Wedge | 2 | [EdTech Digest](https://www.edtechdigest.com/2025/11/19/giving-every-student-an-ai-co-teacher/) (teacher-monitored AI) |
| Market | 2 | [MagicSchool benchmark](https://getlatka.com/companies/magicschool.ai) (K-12 AI subset) |
| Expansion | 2 | [Flint Series A blog](https://flintk12.com/blog/series-a) (independent → public unclear) |
| Competition | 1 | [MagicSchool Series B](https://www.magicschool.ai/blog-posts/series-b-fundraise-for-teacher-ai) (10x scale) |

#### Parasail — 69%

| Factor | Score | Source |
|---|:-:|---|
| Urgency | 3 | [TechCrunch Parasail](https://techcrunch.com/2026/04/15/parasail-raises-32m-to-feed-tokenmaxxing-ai-developers/) |
| Traction | 2 | [PR Newswire Parasail](https://www.prnewswire.com/news-releases/parasail-raises-32m-series-a-to-build-the-supercloud-that-puts-developers-in-control-of-their-ai-302742856.html) ($32M Series A) |
| Community | 2 | [Parasail homepage](https://parasail.io/) (startup customer concentration) |
| Wedge | 2 | [SiliconAngle Parasail](https://siliconangle.com/2026/04/15/parasail-raises-32m-pay-per-token-inference-cloud/) (GPU brokerage) |
| Market | 2 | [Sacra Fireworks profile](https://sacra.com/c/fireworks-ai/) |
| Expansion | 2 | [Kindred Ventures memo](https://kindredventures.com/announcement/parasail-the-ai-supercloud-for-the-agent-era/) |
| Competition | 1 | [Sacra](https://sacra.com/c/fireworks-ai/) (Fireworks $4B / $315M ARR vs Parasail $42M) |

#### Entire — 69%

| Factor | Score | Source |
|---|:-:|---|
| Urgency | 2 | [TechCrunch Entire](https://techcrunch.com/2026/02/10/former-github-ceo-raises-record-60m-dev-tool-seed-round-at-300m-valuation/) (vitamin → painkiller transition) |
| Traction | 1 | [Entire announcement](https://entire.io/news/former-github-ceo-thomas-dohmke-raises-60-million-seed-round) (zero revenue, 4.3K stars) |
| Community | 2 | [HN launch thread](https://news.ycombinator.com/item?id=46961345) (5 HN front pages) |
| Wedge | 2 | [Entire CLI README](https://github.com/entireio/cli) (git-native side branch) |
| Market | 3 | [GrowthNavigate AI SaaS](https://www.growthnavigate.com/b2b-saas-statistics) (dev tools $20B+) |
| Expansion | 3 | [Entire Vision](https://entire.io/vision) (CLI → platform → marketplace) |
| Competition | 2 | [HN Legit-Control reveal](https://news.ycombinator.com/item?id=46972934) (prior art) |

### Tier 3 (Weighted score < 65%)

| Co. | Score | Key data + source |
|---|:-:|---|
| Quill | 63% | [SiliconAngle Quill](https://siliconangle.com/2026/03/03/quill-meetings-built-agentic-chief-ai-staff-takes-private-meeting-notes/); Granola threat at $1.5B per [TechCrunch](https://techcrunch.com/2026/03/25/granola-raises-125m-hits-1-5b-valuation-as-it-expands-from-meeting-notetaker-to-enterprise-ai-app/) |
| Atuin | 56% | [Atuin GitHub](https://github.com/atuinsh/atuin); [v18.13 release](https://blog.atuin.sh/atuin-v18-13/) |
| Reve | 51% | [Artificial Analysis leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image); [Zapier 2026 review](https://zapier.com/blog/best-ai-image-generator/) (no longer top 5) |
| Hallway | 42% | [Redbud VC memo](https://medium.com/redbudvc/why-we-invested-in-hallway-a14d4df3d05f); [Hallway homepage](https://hallway.ai/) (quiet news cycle) |
| Primitive | 41% | [YC Primitive](https://www.ycombinator.com/companies/primitive); [primitive.dev](https://primitive.dev) (pre-launch) |

---

## Output: weighted ranking

```
1.  Tigris Data  ████████████████████ 97%
2.  Vizcom       ████████████████████ 97%
3.  Mem0         ██████████████████░░ 88%
4.  Rasa         ██████████████████░░ 88%
5.  BAML         █████████████████░░░ 87%
6.  Beeble       █████████████████░░░ 83%
7.  Solvely      ███████████████░░░░░ 75%
8.  Flint        ██████████████░░░░░░ 74%
9.  Parasail     █████████████░░░░░░░ 69%
10. Entire       █████████████░░░░░░░ 69%
11. Quill        ████████████░░░░░░░░ 63%
12. Atuin        ███████████░░░░░░░░░ 56%
13. Reve         ██████████░░░░░░░░░░ 51%
14. Hallway      ████████░░░░░░░░░░░░ 42%
15. Primitive    ████████░░░░░░░░░░░░ 41%
```

---

## Final decision

The data points to Tigris Data and Vizcom tied at the top (97%), with Mem0, Rasa, and BAML clustered just below (87-88%). Beeble is a strong outlier at 83% driven by community signal and wedge strength despite weaker traction.

For Track 2, I chose **Vizcom**.

The framework supports it as a top-tier company, but the personal reason matters more for the kind of work I want to do here. Vizcom is democratizing industrial design and easing one of the oldest pain points in creative work: the gap between idea and visualization. The thing that designers used to spend hours on (rendering, materializing, iterating on form and CMF) now takes seconds. That kind of compression is what made me pay attention. Iteration speed compounds into better products, and Vizcom is the only company in this list whose product directly shortens the distance between a designer's vision and something they can hold in their hands. 


So the choice was: Track 2 (GTM agent), and Vizcom as the company.
