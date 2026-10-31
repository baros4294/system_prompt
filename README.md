# System Prompt Suite: Fiction, General & Prompt Engineering

A high-precision system prompt ecosystem engineered for state-of-the-art (SOTA) reasoning (`<think>`) models. Built to eliminate robotic AI tropes, somatic clichés, and structural monoculture while unlocking natural prose, strict narrative grounding in fiction, and adaptive, zero-sycophancy general conversation.

This repository includes the pure `.txt` system prompt, a forensic **Meta-Prompt** used to co-write and audit prompts for reasoning models, a ready-to-use **SillyTavern Chat Completion Preset**, and a custom **Sepia UI Theme** for SillyTavern.

---

## 📂 Repository Contents

| File | Type | Description |
| :--- | :--- | :--- |
| **[`system_prompt.txt`](./system_prompt.txt)** | System Prompt (`.txt`) | The core dual-mode (`General` + `Fiction`) plain-text system prompt for any LLM frontend or API. |
| **[`a_little_more_human.json`](./a_little_more_human.json)** | SillyTavern Preset (`.json`) | Chat Completion preset embedding `system_prompt.txt`, pre-configured for high-effort reasoning models. |
| **[`meta_prompt.txt`](./meta_prompt.txt)** | Meta-Prompt (`.txt`) | Forensic prompt-engineering co-writer and systems auditor protocol designed for SOTA `<think>` models. |
| **[`Sepia.json`](./Sepia.json)** | SillyTavern Theme (`.json`) | Warm, paper-like light-mode UI theme with custom CSS optimized for long-form reading. |

---

## 🧠 1. Core System Prompt (`system_prompt.txt` & `a_little_more_human.json`)

The core prompt is divided into three clean routing layers—**`# Shared`**, **`# General`**, and **`# Fiction`**—designed to maximize expressive range while sealing off common RLHF crutches.

### 🌐 Shared & Prose Style
* **Single-Use ("Spent-Move") Progression:** Every point, comparison, image, gag, tell, or tactic is treated as single-use. Once a move lands, the model advances straight to new ground without reworking or repeating it.
* **Clean Sentence Architecture:** Orders clauses around how perception, causality, and logic unfold. Eliminates robotic micro-sentences, loose `", and"` chains, trailing explanatory tail clauses, and false-purpose infinitives (`"only to [verb]"`).
* **Anti-Slop & Anti-Rhetorical Crutches:** Strips out ornamental adjectives, synonymous stacking, performative self-correction, and rhetorical negation-reframing (*"It wasn't X; it was Y"*).
* **Strict Punctuation & Plain-Text Discipline:** Outputs clean plain prose without unrequested Markdown bloat (headers, bold/italics, bullet lists). Restricts em dashes strictly to cut-off speech or action—never as parentheticals or clause joins.
* **Candid & Unsanitized:** Handles mature, bleak, or taboo themes directly without moralizing, word-masking, or forced positivity, and defaults to metric/setting-appropriate conventions free of US-centric assumptions.

### 💬 General Mode (Non-Fiction & Conversation)
* **Chameleon Register Matching:** Mirrors the user's conversational style across the entire response (tone, formality, all-lowercase casing, slang, language mixing, profanity, and emoji), switching to an external formal register only when drafting standalone artifacts.
* **Zero Sycophancy:** Bases agreement and pushback strictly on logic and accuracy. Corrects flawed premises directly without hedged prefaces, softening praise, or performative apologies.

### 📖 Fiction Mode (Creative Writing & Roleplay)
* **Strict User Agency:** Controls only the world and non-user cast. Never dictates or implies a user character's speech, actions, internal states, silence, or unestablished history.
* **Locked Limited POV & Free Indirect Style:** Locks onto one non-user focal character per continuous scene. Routes all subjectivity (memories, plans, fallible reads of others) through tight free indirect style or brief untagged direct thoughts while banning perception filter verbs (*saw, felt, realized*).
* **Natural Dialogue Mechanics:** Formats dialogue cleanly without attached action beats. Automatically omits speech tags in two-speaker scenes once turn alternation is established, and uses bare *"say"* or *"ask"* tags in 3+ speaker scenes.
* **Material Grounding & Somatic Slop Removal:** Grounds scenes in concrete spatial relations and perceptible cause-and-effect. Ruthlessly eliminates classic AI somatic and sensory clichés (no jaw-clenching, white knuckles, breath-holding, eye-contact tropes, voice octave/register shifts, ambient hums, or unnecessary material/measurement specs).

---

## 🔬 2. Prompt-Engineering Auditor (`meta_prompt.txt`)

`meta_prompt.txt` turns a SOTA reasoning model into a forensic systems auditor and prompt-engineering co-writer. It is built around the **Core Physics of SOTA Thinking Models** and enforces a strict multi-phase engineering protocol:

1. **Phase 1 — Macro & Coupled-Interaction Check:** Audits mode routing, precedence hierarchy, `<think>` load, and simulates all rules firing together to catch coupled failure modes or syntactic monoculture.
2. **Phase 2 — Bullet-by-Bullet Audit & Devil's Advocate:** Inspects every rule individually for root-cause flaws, loophole traps, internal contradictions, and KV-cache self-violations before writing.
3. **Phase 3 — Orthogonal Invariants:** Enforces functional atomicity (one bullet = one job) and targets underlying epistemic/causal failure mechanisms rather than blanket-banning valid grammatical containers.
4. **Phase 4 — Empirical Telemetry & Compliance Triage:** Analyzes test outputs to separate stochastic compliance slips from architectural holes, preventing "whack-a-mole" probability clamping and hydraulic squeezes.

**Key Principles Enforced:**
* **KV-Cache Neutrality:** Prevents prompt phrasing templates (like repeated *"rather than"* constructions) from priming and leaking into model outputs.
* **No Curse-of-Knowledge Gates:** Replaces subjective clarity gates (*"when warranted"*, *"unless ambiguous"*) with objective, observable triggers.
* **No Self-Monitoring Paradoxes:** Avoids *"vary naturally"* commands that force decoders into artificial oscillation.

---

## 🎨 3. Sepia UI Theme (`Sepia.json`)

A custom **SillyTavern UI Theme** crafted for comfortable, distraction-free long-form reading and writing:
* **Warm Paper Palette:** Soft sepia canvas (`#d6c19d` / `#f4e8d1`) with high-contrast deep espresso typography (`rgba(48, 38, 28, 1)`) to reduce eye strain.
* **Refined Typography:** Uses `Inter` with generous line height (`1.7`) for narrative prose and `JetBrains Mono` with contextual ligatures for code and technical blocks.
* **Performance-First CSS:** Strips out heavy backdrop blurs and drop shadows (`backdrop-filter: none`, `noShadows: true`) for instant, lag-free scrolling, while cleanly styling `<think>` reasoning dropdowns, blockquotes, and mobile viewports.

---

## 🚀 How to Use

### Using `system_prompt.txt` or `meta_prompt.txt` (Universal)
1. Open [`system_prompt.txt`](./system_prompt.txt) (for general chat/writing) or [`meta_prompt.txt`](./meta_prompt.txt) (to audit/co-write prompts).
2. Copy the raw text and paste it into the **System Prompt** or **Custom Instructions** field of your preferred LLM interface (Claude, ChatGPT, OpenWebUI, LM Studio, API playground, etc.).

### Importing `a_little_more_human.json` (SillyTavern Preset)
1. Download raw [`a_little_more_human.json`](./a_little_more_human.json).
2. In **SillyTavern**, open the **AI Response Configuration** panel (sliders icon at the top left).
3. Ensure your API is set to **Chat Completion**, click the **Import** button next to the preset dropdown, and select `a_little_more_human.json`.

### Importing `Sepia.json` (SillyTavern Theme)
1. Download raw [`Sepia.json`](./Sepia.json).
2. In **SillyTavern**, open the **User Settings** panel (person/gear icon in the top bar).
3. Under the **UI Theme** section, click **Import Theme** and select `Sepia.json`.

---

## 🛠️ Customization & Feedback

Feel free to fork this repository, test the prompt against your favorite reasoning models, or run your own custom prompts through `meta_prompt.txt`. Issues, telemetry findings, and pull requests are always welcome!
