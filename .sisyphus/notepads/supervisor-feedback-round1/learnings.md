# Learnings — supervisor-feedback-round1

## Approved Terminology
- Prefer `频谱过宽`.
- Maintain the thesis-level classification keywords around `物理本构` / `畸变网格单元` or approved discretization wording / `算法机制`.
- Replace `非线性兼容性` with `非线性问题` where this supervisor comment applies.

## Structural Policy
- **Structure before wording**: Diagnose and address structure before wording. Many issues in this thesis are paragraph ordering problems.
- **Harms before sources**: In the flagged intro background block, place harms before source classification.
- **Immediate synthesis**: Provide an immediate synthesis paragraph after bullet lists when required.
- **Paper 1 Conclusion**: The fix for the paper 1 conclusion is a paragraph-order swap, not compression.

## Background Introduction Wording (Task 6)
- **Problem**: Opening paragraphs had overly abstract/assertive claims ("统一新范式", "物理感知能力", "方法论") and mismatched goal statements (CAE/CG aiming for "精确性与稳定性").
- **Decision**: Replaced "方法论" / "统一新范式" / "物理感知能力" with "新思路" / "软硬耦合定位识别" / "建立数值友好表示空间". Adjusted CAE/CG sentence to target "效率与稳定性" reflecting the actual thesis focus on computation time and condition numbers.
- **Rule**: Keep the rhetoric grounded in numerical analysis terms (e.g. condition number, spectrum width, solving efficiency) rather than philosophical terms (e.g. paradigm, physics-aware, methodology).
## Figure Cues in Chinese Academic Writing
- **Rule**: Figure cues like "如图X所示" should immediately introduce what the figure shows (the physical or logical process), rather than starting with a general philosophical statement about the problem.
- **Pattern applied**: Changed `如\Cref{fig:numerical_simulation_process} 所示，物理仿真的基本过程通常表现为：从连续形式的...` to `如\Cref{fig:numerical_simulation_process}所示，物理仿真的基本过程是从连续形式的...` to make the cue direct and tight.

## Terminology
- **Pathology Terminology**: Standardized `频谱分离` to `频谱过宽` (spectrum too wide / large spectrum spread) when referring to the cause of high condition numbers in stiffness matrices. This is mathematically more precise for condition number contexts (ratio of max to min eigenvalues).

### Structure Rules Applied in `1_background.tex`
- **Pathology Block Ordering:** Always present the *harms/impacts* of a problem (e.g., condition number, stability, efficiency) immediately after introducing the challenge, *before* classifying its sources (e.g., physical vs. numerical). This reader-order logic ensures the audience understands *why* the problem matters before delving into *where* it comes from.
- **Immediate Synthesis for Bullets:** A paragraph immediately following a bulleted list should act as a direct synthesis or applicability summary of the items above it, rather than a detached disclaimer. It should tie the listed points back to the overarching methodology or constraints.

### Structure Rules Applied in `1_background.tex`
- **Pathology Block Structure**: Always state the harm/impact of a problem *before* detailing its sources/classifications. This follows reader-order logic (why it matters -> where it comes from).
- **Post-Bullet Synthesis**: Paragraphs immediately following a bulleted list must act as an immediate synthesis or applicability summary of the items above, rather than a detached disclaimer.

## 1_background.tex Structural Edits (Task 8)
- **Pathology Block Ordering**: Placed the harms/impacts paragraph immediately after the numerical challenge opener, before discussing the source classification. This logical progression (what the problem is -> why it's bad -> where it comes from) reads more naturally in academic Chinese writing.
- **Post-Bullet Synthesis**: Transformed the paragraph following the three bullet points into an immediate synthesis/applicability summary rather than a detached disclaimer. The text now clearly ties the specific boundaries of the method to the three concrete problems just enumerated.

### Structural Principles for 1_background.tex
1. **Harms Before Sources**: In the problem diagnosis section, it's more effective to state the impact of a problem (e.g., instability, inefficiency caused by high condition number) *before* classifying its specific sources (e.g., physical constitutive, geometric, algorithmic mechanisms). This creates a more natural "why should we care" -> "where does it come from" flow.
2. **Immediate Post-Bullet Synthesis**: The paragraph immediately following a bullet list summarizing three related but distinct problems should serve as a collective summary or "applicability synthesis" for those points, not as an isolated disclaimer or warning. It should clarify the shared boundaries or objectives across the listed items.

### Task 8: `1_background.tex` Structural Improvements
- **Rule applied:** Harms/impacts should precede source-classification. A reader needs to know *why* an issue is bad (harms) before delving into *where* it comes from (sources). 
- **Rule applied:** A paragraph immediately following a bullet list should function as an immediate synthesis or applicability summary of the items listed, not as a detached disclaimer.

### Structural Rules for Background Introduction
- **Pathology Block Ordering:** Always present the *harms and impact* of a problem (e.g., system ill-conditioning, efficiency/stability drop) *before* discussing the *sources/classification* of the problem. This answers "why does this matter" before "where does this come from."
- **Immediate Synthesis for Bullet Lists:** When presenting a list of applications or problems (bullets), the paragraph immediately following it must serve as an immediate synthesis/applicability summary that ties the items together, rather than reading like a detached disclaimer or isolated boundary condition.
- Structural Rule: When discussing a pathology or numerical challenge, state the harms and impacts before classifying the sources of the problem. This establishes the "why it matters" before diving into the "where it comes from".
- Structural Rule: A paragraph following a bulleted list should act as an immediate synthesis or applicability summary of the items above it, rather than functioning as an isolated or detached disclaimer.

## Structural Editing Rules

1. **Pathology Block Structure:** Always place harms/impacts before source classification when describing a numerical pathology. This explains *why* the issue matters before categorizing its sources.
2. **Post-Bullet Synthesis:** The paragraph following a bulleted list should act as an immediate synthesis or applicability summary of the listed items, rather than reading as a detached disclaimer or isolated concept.
- Structure Rule: Move harms/impacts before source classification to establish the 'why it matters' before the 'where it comes from'.
- Structure Rule: When listing problems via bullets, the immediately following paragraph MUST act as a synthesis/applicability summary rather than a detached disclaimer.
- Structural Rule: When discussing pathologies/harms alongside their sources, always present the harms/impacts first (why it matters) before categorizing the sources (where it comes from).
- Structural Rule: Paragraphs immediately following a bulleted list should function as an immediate synthesis or applicability summary for those items, rather than an isolated disclaimer, ensuring a smooth transition into the closing preview.
- Structural Rule: Reorder pathology paragraphs to explain harms/impacts *before* source classification.
- Structural Rule: Paragraphs following bullet lists should serve as an immediate synthesis or applicability summary, not isolated disclaimers.
- When describing harms and source classification of a problem (e.g. numerical pathology), ALWAYS present the harms/impacts first, followed by the sources/classification. This matches reader-order logic (why it matters -> where it comes from).
- After a bulleted list describing applications or problem types, IMMEDIATELY follow with a synthesis paragraph that connects the items together and summarizes applicability/bounds. Do NOT leave applicability disclaimers isolated.

### Task 8: Pathology Block and Bullet Synthesis (1_background.tex)
- **Pathology Block Ordering**: Always state the harms/impacts before the source classification. This logical flow ("why it matters" -> "where it comes from") is more natural for the reader.
- **Immediate Synthesis**: Paragraphs immediately following a bulleted list should act as an immediate synthesis or applicability summary of the items above, not as a detached disclaimer.

- Structure Rule (Pathology Block): Harms/impacts should precede source classification to establish context before delving into causes.
- Structure Rule (Post-Bullet): Paragraphs immediately following bullet lists should serve as an immediate synthesis or applicability summary of the items, avoiding reading like isolated disclaimers.

## Pathology / Background section structural rules
- Structural order in pathology introduction should be: 
  1. The numerical challenge (ill-conditioning / high condition number)
  2. The practical harms/impacts of this challenge (so the reader knows why it matters)
  3. The specific sources/classification of the challenge (e.g. constitutive, geometric, algorithmic)
- When introducing a set of problems (e.g. bullets), the summarizing/applicability paragraph must follow the bullets *immediately* to synthesize their shared scope and applicability.

- In 1_background.tex, the pathology block was reordered to put harms/impacts before source classification, following the 'harms before sources' rule.
- The post-bullet paragraph was rewritten to act as an immediate synthesis/applicability summary, rather than a detached disclaimer.

### intro/1_background.tex Structural Edits (Task 8)
- **Pathology Block Ordering**: Always present the *harm/impact* of numerical pathology (condition number rise, solving inefficiency, visual artifacts) *before* classifying its sources (constitutive, geometric, algorithmic). This follows the reader-centric logic of "why this matters" before "where this comes from".
- **Bullet Synthesis Rule**: A paragraph immediately following a list of examples/applications (like the three core problems) must act as an immediate synthesis or applicability summary, not an isolated boundary/disclaimer section. It anchors the preceding list to the overall scope.

### Structural Rules
- **Pathology Block**: State the harms and impacts of a problem *before* detailing its sources. This establishes "why it matters" before explaining "where it comes from".
- **Post-Bullet Synthesis**: Paragraphs immediately following a bulleted list should act as an immediate synthesis or applicability summary for the listed items, rather than reading like a detached disclaimer.
- When reordering the pathology block in thesis intro, state the harms/impacts first (e.g. ill-conditioning affects efficiency and stability), then classify the sources of the pathology (e.g. from physical constitutive laws, discretization, algorithm mechanisms). Readers naturally accept 'why this matters' before 'where it comes from'.
- The paragraph immediately following a bullet list of scenarios/methods should function as a synthesis or applicability summary of the bullet items, instead of being framed as an isolated disclaimer.
- **Structural Rule (Pathology Block):** Always state the harms/impacts of numerical pathology before categorizing its sources. This follows the natural "why it matters" -> "where it comes from" logic.
- **Structural Rule (Post-Bullet Synthesis):** Paragraphs immediately following bullet lists should serve as an immediate synthesis or applicability summary of those items, avoiding language that makes them sound like detached disclaimers.
- **Structural Rule (Pathology Block)**: In technical introductions, the explanation of "Why is this a problem?" (harms/impacts) should logically precede the explanation of "Where does it come from?" (source classification). This ensures readers grasp the significance before the mechanism.
- **Structural Rule (Bullet Lists)**: A paragraph immediately following a bullet list should act as an immediate synthesis or a clear statement of applicability to the previous points. It should not read like a detached disclaimer.
- **Structural Rule**: In the thesis introduction, always present the *harms/impacts* of a numerical pathology before classifying its *sources* (e.g., physical constitutive laws vs. spatial discretization).
- **Structural Rule**: When presenting a bulleted list of research applications, immediately follow the list with a summary paragraph that acts as an immediate synthesis/applicability summary, rather than a detached disclaimer.
- Structural Rules from background block edit:
  - Paragraph reordering is crucial: place harms/impacts before classifying sources. It establishes the "why this matters" before getting into technicalities.
  - Applicability boundaries/summaries should directly follow bulleted enumerations rather than standing alone as detached paragraphs.
- When using a bulleted list to summarize thesis contributions (e.g., Chapter 2, 3, 4), always ensure symmetry: if a long-form paragraph follows to explain Chapter 2, there MUST be equivalent paragraphs for Chapter 3 and Chapter 4 in the exact same order.
- Transitional phrases between these paragraphs should bridge the progression from one source of the problem (e.g., constitutive) to the next (e.g., mesh geometry) to the final one (e.g., algorithmic constraints).
- Chapter-ending overview paragraphs should prefer neutral verbs like `讨论`/`说明`/`展望`, and avoid subjective wording such as `反思` in thesis-standard summaries.
- Chapter-ending order rule: when the final two paragraphs are a limitations/outlook paragraph and a higher-level synthesis paragraph, place the limitations/outlook paragraph first and reserve the stronger synthesis paragraph for the chapter close.
- Restored thesis-level vocabulary ('物理本构' / '畸变网格单元' / '算法机制') in paper3 opening recap to match established framing, avoiding terminology drift like '显式几何约束'.
- Rule: Stabilize thesis-level keywords in chapter openings. Paper 3 should reflect '物理本构', '畸变网格单元', and '算法机制' to maintain narrative consistency and avoid rejected framing.

- **Recap Wording Rule**: Always use the stable thesis-level keywords (`物理本构`, `畸变网格单元`, `算法机制/算法构造`) when recapping previous chapters or classifying soft-hard coupling sources. Do not drift into older rejected terminology like `显式几何约束` or `局部离散畸变`.

### Keyword Stabilization Rule
When revising chapter openings (especially Paper 3), strictly maintain the thesis-level classification vocabulary: `物理本构`, `畸变网格单元`, and `算法机制`. Do not revert to older synonyms (like `显式几何约束` or `局部离散畸变`) to ensure cross-chapter narrative consistency.
- **Recap/Framing Rule**: Keep thesis-level classification keywords stable in chapter openings. Use `物理本构`, `畸变网格单元`, and `算法机制` (or equivalent approved wording). Avoid reintroducing rejected framing like `paper2 是桥梁` or `显式几何约束` / `局部离散畸变`.
- Rule: Keep chapter recap keywords stable. Always align backward references (e.g., '前两章分别讨论了...') with the agreed thesis classification keywords (物理本构, 畸变网格单元, 算法机制) and avoid drifting back to earlier paper-specific jargon (like 显式几何约束 or 局部离散畸变).
- 绪论开头回顾：坚持“物理本构 / 畸变网格单元 / 算法构造导致”这三个稳定的维度，不随意替换。
- Recap wording rule: When referring back to previous chapters, strictly use the agreed classification keywords ('物理本构' and '畸变网格单元') rather than loosely paraphrasing them (like '显式几何约束' or '局部离散畸变'), to maintain thesis-level framing stability.
- paper3/1_intro.tex recap must strictly align with the thesis-stable keywords: 物理本构 / 畸变网格单元 / 算法机制诱发. Do not invent new terms or reintroduce rejected storylines (e.g., 'bridge chapter').
- **Thesis keywords stability**: Always use the stable keyword set (物理本构, 畸变网格单元, 算法机制) when summarizing previous chapters. Do not invent new synonyms (like 显式几何约束 or 局部离散畸变) which cause the thesis framing to drift.
- Rule: Keep thesis-level keywords stable ('物理本构', '畸变网格单元', '算法机制'), avoid renaming them across chapters.

- **Recap Wording Stability**: The recap of previous chapters at the beginning of subsequent chapters (like paper 3) MUST exactly match the classification keywords established in the thesis introduction (e.g., `物理本构`, `畸变网格单元`). Never substitute these established keywords with synonyms like `显式几何约束` or `局部离散畸变`.
- **Recap Keyword Adherence Rule**: When referring back to previous chapters, strictly use the agreed classification keywords ('物理本构', '畸变网格单元', '算法构造导致') rather than drifting into rejected terminology ('显式几何约束', '局部离散畸变'). Ensure edits register properly to satisfy verification.
- **Recap Wording Stability**: The recap of previous chapters at the beginning of subsequent chapters (like paper 3) MUST exactly match the classification keywords established in the thesis introduction (e.g., `物理本构`, `畸变网格单元`). Never substitute these established keywords with synonyms like `显式几何约束` or `局部离散畸变`.
- **Recap Wording Stability (Double-Check)**: Ensure that recap paragraphs stringently use the thesis-stable keywords (e.g., `物理本构`, `畸变网格单元`, `算法构造导致`) and never default back to earlier or unapproved phrases.
- **Recap Wording Stability**: When referring to prior chapters in the thesis, always use the stable classification keywords (e.g., `物理本构`, `畸变网格单元`, `算法构造导致`). Avoid reverting to older synonyms like `显式几何约束` or `局部离散畸变` to ensure narrative consistency.
- **Recap Keyword Adherence Rule**: When revising the opening recap in a chapter (e.g., paper 3), verify that the text strictly adheres to the thesis-wide classification vocabulary (e.g., `物理本构`, `畸变网格单元`, and `算法构造导致`). Any synonyms like `显式几何约束` or `局部离散畸变` must be purged to maintain framing consistency.
- **Recap Keyword Stability**: When recapping previous chapters, strictly adhere to the established thesis-level classification keywords (e.g., '物理本构', '畸变网格单元', '算法构造导致'). Never revert to rejected or superseded terminology ('显式几何约束', '局部离散畸变') to ensure a consistent narrative thread.
- **Recap Wording Stability**: The recap of previous chapters at the beginning of subsequent chapters (like paper 3) MUST exactly match the classification keywords established in the thesis introduction (e.g., `物理本构`, `畸变网格单元`). Never substitute these established keywords with synonyms like `显式几何约束` or `局部离散畸变`.
- **Recap Wording Stability**: When referring to previous chapters, strictly use the thesis-level classification keywords established in the intro (e.g., `物理本构`, `畸变网格单元`, `算法构造导致`) rather than varying the terminology (e.g., avoiding `显式几何约束` or `局部离散畸变`) to maintain structural consistency.
- **Recap Wording Stability (Task 12)**: Keep thesis-level keywords stable ('物理本构', '畸变网格单元', '算法构造导致') in chapter recaps. Never revert to synonyms like '显式几何约束' or '局部离散畸变'.
- **Recap Wording Stability**: The recap of previous chapters at the beginning of subsequent chapters (like paper 3) MUST exactly match the classification keywords established in the thesis introduction (e.g., `物理本构`, `畸变网格单元`, `算法构造导致`). Never substitute these established keywords with synonyms like `显式几何约束` or `局部离散畸变`.
- **Recap Wording Stability**: The recap of previous chapters at the beginning of subsequent chapters (like paper 3) MUST exactly match the classification keywords established in the thesis introduction (e.g., `物理本构`, `畸变网格单元`, `算法构造导致`). Never substitute these established keywords with synonyms like `显式几何约束` or `局部离散畸变`.

- **Pseudocode Layout Rule**: In `algorithmic` environments, split long action lines that combine a solve step with tuple-style result assignment into two short `\STATE` lines (e.g., "求解..." + "记录...") to reduce overflow risk without changing algorithm semantics.
