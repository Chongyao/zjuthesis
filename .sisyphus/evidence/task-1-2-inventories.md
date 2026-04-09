# Paper3 Source Inventory Verification
Date: 2026-04-07

## Original Paper Inventory
Location: `/home/zcy/workspace/records/primal-dual_modes`
Main entry points: `paper-tog.tex` -> `paper-body/document.tex`

Text-bearing Source Files:
1. `abstract.tex` - Used in intro
2. `teaser.tex` - Abstract/Results summary content
3. `1.0-introduction.tex` - Introduction text
4. `2.0-related_work.tex` - Literature review
5. `3.0-background.tex` - Theoretical background
6. `4.0-method-new.tex` - Core methodology
7. `4.1-implementation.tex` - Implementation details
8. `4.1.1-alg-adaptive-shifting.tex` - Algorithm pseudo-code
9. `5.0-results.tex` - Main results
10. `5.1-statistics.tex` - Data tables (hardware/models)
11. `6.0-conclusion.tex` - Conclusion text
12. `7.0-appendix.tex` - Mathematical proofs and breakdowns

Other files:
- `0.0preamble.tex` / `0.1package_def.tex` (Macros/Config, non-text)
- `superlarge.txt` / `conclusion-explain-validation.txt` (Text notes, might contain scattered sentences)

## Thesis Paper3 Inventory
Location: `/home/zcy/workspace/records/zjuthesis_paper3/body/graduate/paper3`
Main entry point: `main.tex`

Text-bearing Files:
1. `1_intro.tex` - Introduction (Mixed source candidate)
2. `2_representation.tex` - Background/Theory (Matches 3.0/4.0)
3. `3_simulation.tex` - Method/Implementation (Mixed source candidate)
4. `4_results.tex` - Results (Mixed source candidate)
5. `5_conclusion.tex` - Conclusion (Mixed source candidate, heavily expanded)
6. `5_1_alg_adaptive_shifting.tex` - Algorithm implementation (Matches 4.1.1)

Files have been significantly restructured from the 7 chapters of the original to the 5 sections of the thesis chapter.

Mixed-source candidates:
- `1_intro.tex`: Fuses abstract + 1.0-intro + 2.0-related + thesis context
- `3_simulation.tex`: Fuses 4.1-implementation + 7.0-appendix + method details
- `4_results.tex`: Fuses 5.0-results + 5.1-statistics + teaser details
- `5_conclusion.tex`: 6.0-conclusion + extensive thesis-specific expansion