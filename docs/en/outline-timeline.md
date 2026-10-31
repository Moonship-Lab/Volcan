# Volcan Timeline Outline (General History)

> **Status**: skeleton only — every entry is still unwritten.
> This file defines *which entries to write and what question each must answer*; it does not contain the answers. Once you claim an entry, flip its status to "Drafting" in your branch.

**Status legend**
`Open` · `Drafting` · `In review` · `Awaiting translation` · `Done`

**Naming rule**
Chinese: `docs/zh/entries/{chapter}-{slug}.md`; English: `docs/en/entries/{chapter}-{slug}.md` — same slug, so the two sides can cross-link.
Example: Chapter 3, "Interchangeable Parts" → `docs/en/entries/03-interchangeable-parts.md` and `docs/zh/entries/03-interchangeable-parts.md`.

**Fixed structure for every entry** (see `CONTRIBUTING.md`): One-line definition → What came before → The turning point → What survives today → Common misconceptions → References.

---

## Prologue · Before Manufacturing: Materials, Hands, Measure (prehistory — 1500)

**Core proposition**: Long before anything was called "manufacturing", humanity had accumulated millennia of material knowledge and measurement intuition. Those were the preconditions for every later craft.

Planned entries

- [ ] `00-measurement` **Measurement & Metrology** — The precondition for discussing a part at all: what did "dimension" mean before reference standards existed? `Open`
- [ ] `00-materials` **A Material Genealogy** — Stone, copper, iron, steel: what possibility boundaries did each transition rewrite? `Open`
- [ ] `00-guild` **The Guild System** — How apprenticeship guaranteed quality, and how it blocked diffusion. `Open`

**Links forward**: measurement → gauges (Ch. 2), statistical quality (Ch. 5); guilds → decomposition of skill (Ch. 4).
**To fill**: this chapter's takeaway for AI researchers / practitioners — written by whoever claims it.

---

## Chapter 1 · Workshops and the Precision of Clocks (c. 1500 — 1760)

**Core proposition**: Precision preceded power. Clockmakers and instrument makers made "reproducible dimensions" a discipline before machines existed.

- [ ] `01-clockmakers` **Clockmaking Precision** — How was accuracy achieved and transmitted in an era with no concept of interchangeable parts? `Open`
- [ ] `01-instruments` **Instruments & Navigation** — How did precision demand pull machining capability forward? `Open`
- [ ] `01-workshop` **From Cottage Industry to Workshop** — The first centralisation of production organisation. `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Chapter 2 · Steam, Power and the Factory System (c. 1760 — 1850)

**Core proposition**: Power no longer depended on water and muscle. The factory became a spatial arrangement, and labour was re-cut.

- [ ] `02-steam` **Steam Power** — Why did centralised power change building layout and siting logic? `Open`
- [ ] `02-factory` **The Factory System** — Discipline, working hours, and the new order of "humans beside machines". `Open`
- [ ] `02-division-of-labor` **Division of Labor** — What Adam Smith's pin factory said, and what it left out. `Open`
- [ ] `02-machine-tools` **Machine Tools (Maudslay's lathe)** — "Machines that make machines": precision becomes transferable. `Open`

**To fill**: relationship to interchangeable parts (Ch. 3).

---

## Chapter 3 · Interchangeable Parts and the American System (c. 1850 — 1900)

**Core proposition**: Parts no longer had to be fitted by hand; assembly became a separate operation. The first paradigm shift of modern manufacturing.

- [ ] `03-interchangeable-parts` **Interchangeable Parts** — The Whitney myth and the real difficulty in the armouries: tolerance is the protagonist. `Open`
- [ ] `03-american-system` **The American System** — Special-purpose machinery + general labour + uniform drawings. What did that compose? `Open`
- [ ] `03-gauges-and-limits` **Gauges & Limits** — Inspection moves from "looks right" to judged conformance. `Open`
- [ ] `03-armory-practice` **Armory Practice** — Why do frontier processes arrive at weapons first? `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Chapter 4 · Electricity, Assembly Lines, Mass Production (c. 1900 — 1945)

**Core proposition**: Distributed power made stations rearrangeable. The essence of the assembly line was not the conveyor but the redesign of operation time and labour content.

- [ ] `04-moving-assembly` **The Moving Assembly Line (Ford)** — What actually changed at Highland Park in 1913. `Open`
- [ ] `04-mass-production` **Mass Production** — Where the trade-offs between variety, batch and cost structure begin. `Open`
- [ ] `04-electric-power` **Unit-Drive Electrification** — From one line shaft to one motor per machine: the first time a line could be rearranged. `Open`
- [ ] `04-five-dollars-day` **The $5 Day** — Institutional pricing of labour: welfare and discipline at once. `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Chapter 5 · Wartime Production, Operations Research, Statistical Quality (c. 1940 — 1960)

**Core proposition**: Volumes became too large to inspect everything. Sampling and statistics were forced into the shopfloor; operations research took shape in war.

- [ ] `05-statistical-qc` **Statistical Quality Control (Shewhart)** — Which two kinds of variation does the control chart separate? The ancestor of all anomaly detection. `Open`
- [ ] `05-sampling` **Sampling Inspection** — How WWII procurement wrote risk into tables. `Open`
- [ ] `05-operations-research` **Operations Research** — Scheduling, queueing and inventory mathematics enter industrial practice here. `Open`
- [ ] `05-total-quality` **From QC to TQC (Deming / Juran)** — Quality leaves the inspection department for the whole system. `Open`

**To fill**: takeaway for AI researchers / practitioners (anomaly detection and closed-loop control belong here).

---

## Chapter 6 · Lean Production and the Toyota Way (c. 1950 — 1990)

**Core proposition**: Constrained by scarce capital, scarce currency and high-mix low-volume demand, Japan took the other path — not bigger batches, but shorter flow time.

- [ ] `06-tps` **Toyota Production System** — What do the two pillars (jidoka, JIT) concretely mean? `Open`
- [ ] `06-just-in-time` **Just-in-Time** — Inventory as water level hiding problems, not as asset. `Open`
- [ ] `06-jidoka` **Jidoka (automation with a human touch)** — Machines stopping to report abnormality vs. humans watching: what is the essential difference? `Open`
- [ ] `06-kanban` **Kanban** — An information-flow design, not a board of cards. `Open`
- [ ] `06-kaizen` **Kaizen** — Small, continuous, shopfloor-led improvement. `Open`
- [ ] `06-muda` **The Seven Wastes (Muda)** — A waste list for today: which have data eliminated, which have resisted? `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Chapter 7 · Numerical Control, CAD/CAM and the Automation Wave (c. 1950 — 2000)

**Core proposition**: Machining instructions detached from the human hand and became storable, copyable, transmissible data. Manufacturing became a software problem for the first time.

- [ ] `07-numerical-control` **NC / CNC (Parsons & the MIT Servomechanisms Lab)** — From punched tape to servo loops, and the lesson most relevant to AI researchers: how process knowledge gets encoded. `Open`
- [ ] `07-cad-cam` **CAD/CAM and the Geometry Problem** — Geometry enters computation from drawings. `Open`
- [ ] `07-robots` **Industrial Robots** — From Unimate to welding cells: the trade between repeatability and flexibility. `Open`
- [ ] `07-fms` **Flexible Manufacturing Systems** — The price tag of flexibility: why did it struggle to spread? `Open`
- [ ] `07-plc` **Programmable Logic Controllers** — The control layer that is still the bedrock of OT. `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Chapter 8 · Globalisation, Supply Chains, Electronics Manufacturing (c. 1990 — 2015)

**Core proposition**: Production was split across geography. The variables beyond cost — lead time, risk, compliance — moved to the centre of manufacturing decisions.

- [ ] `08-global-supply-chain` **Global Supply Chains** — Efficiency and fragility of fine-grained division: the same coin. `Open`
- [ ] `08-outsourcing-ems` **Contract Manufacturing & EMS** — Who owns the process owns the say. `Open`
- [ ] `08-lean-six-sigma` **Lean Six Sigma** — The merger of two systems, and how it became a certificate industry. `Open`
- [ ] `08-plm-erp` **PLM / ERP and Data Silos** — The first time manufacturing data entered systems at scale, and got trapped at scale. `Open`

**To fill**: takeaway for AI researchers / practitioners (these pains became the market for industrial AI).

---

## Chapter 9 · Digitalisation, Industry 4.0, Smart Manufacturing (c. 2011 — present)

**Core proposition**: Sensors and networks connected the shopfloor to information systems; data approached real time for the first time. The gap between the pitch and the reality is where today's practitioners live their daily frustration.

- [ ] `09-industry-4-0` **Industry 4.0 / Industrial Internet** — Genealogy of the concept: who coined it when, and how far down it landed. `Open`
- [ ] `09-digital-twin` **Digital Twins** — What maintains consistency between model and physics, and where does it break? `Open`
- [ ] `09-cps-and-edge` **Cyber-Physical Systems & Edge Computing** — The engineering reality of OT/IT convergence. `Open`
- [ ] `09-mes` **Manufacturing Execution Systems** — The translation layer between planning and execution. `Open`
- [ ] `09-data-reality` **What Factory Data Really Looks Like** — Missing values, clock drift, label noise, distribution shift caused by equipment changeover. Required reading before modelling. `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## Closing Chapter · Manufacturing in the AI Era (present — )

**Core proposition**: Large models and falling sensor costs have moved "datafication of experience" to a new position. Which problems disappeared, and which did not?

- [ ] `10-predictive-maintenance` **Predictive Maintenance** — From vibration analysis to remaining useful life: why are demos easy and deployments hard? `Open`
- [ ] `10-defect-inspection` **Automated Defect Inspection** — Sample imbalance, ownership of the defect definition, the economics of escapes. `Open`
- [ ] `10-scheduling-rl` **Scheduling & Reinforcement Learning** — State space, hard constraints, and the irreversibility of real decisions. `Open`
- [ ] `10-llm-in-shopfloor` **LLMs on the Shopfloor** — Retrieval, root-cause attribution, SOP Q&A: where are the boundaries of trust and responsibility? `Open`
- [ ] `10-tacit-knowledge` **Translating Tacit Knowledge** — How does a veteran operator's judgement become a trainable target? This is exactly why Volcan exists. `Open`

**To fill**: takeaway for AI researchers / practitioners.

---

## How to claim an entry

1. Pick a slug in an Issue (or propose a new one with one sentence on why it deserves writing).
2. Change its line here to `- [ ] ... Drafting @yourid`, and include the edit in the same PR.
3. When the body is written, set it to "In review" in that PR.

See [`CONTRIBUTING.md`](../../CONTRIBUTING.md) for the writing and citation rules.
