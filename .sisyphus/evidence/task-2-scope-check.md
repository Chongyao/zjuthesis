# Task 2: Scope Sanity Check — First-Person Inventory

**Generated:** 2026-05-09  
**Purpose:** Confirm that the `我们` inventory is complete and correctly scoped to active build files only.

---

## 1. Active File Graph Verification

Source: `body/graduate/content.tex`

```
content.tex
├── Chapter 1: intro/main.tex
│   ├── intro/1_background.tex          ✓ (scanned, clean)
│   ├── intro/2_related_and_problems.tex ✓ (scanned, 4 hits)
│   └── intro/3_contributions_and_organization.tex ✓ (scanned, 1 hit)
├── Chapter 2: paper1/main.tex
│   ├── paper1/1_intro.tex              ✓ (scanned, clean)
│   ├── paper1/2_representation.tex     ✓ (scanned, clean)
│   ├── paper1/3_simulation.tex         ✓ (scanned, clean)
│   ├── paper1/4_results.tex            ✓ (scanned, clean)
│   └── paper1/5_conclusion.tex         ✓ (scanned, clean)
├── Chapter 3: paper2/main.tex
│   ├── paper2/1_intro.tex              ✓ (scanned, 1 hit)
│   ├── paper2/2_related.tex            ✗ COMMENTED OUT — excluded
│   ├── paper2/3_background.tex         ✓ (scanned, 1 hit)
│   ├── paper2/4_method.tex             ✓ (scanned, 14 hits)
│   ├── paper2/5_results.tex            ✓ (scanned, 13 hits)
│   └── paper2/6_summary.tex            ✓ (scanned, clean)
├── Chapter 4: paper3/main.tex
│   ├── paper3/1_intro.tex              ✓ (scanned, clean)
│   ├── paper3/2_foundation.tex         ✓ (scanned, 1 hit)
│   ├── paper3/2_representation.tex     ✓ (scanned, 2 hits)
│   ├── paper3/3_simulation.tex         ✓ (scanned, 17 hits)
│   ├── paper3/4_results.tex            ✓ (scanned, 19 hits)
│   └── paper3/5_conclusion.tex         ✓ (scanned, clean)
└── Chapter 5: conclusion.tex           ✓ (scanned, clean)
```

**All 20 active .tex files verified.** Coverage: 100%.

---

## 2. Excluded Files (NOT in active build — correctly omitted)

| Excluded Path | Reason |
|---------------|--------|
| `paper1_backup/**` | Backup (not referenced by any `\inputbody`) |
| `paper2_backup/**` | Backup |
| `paper3_backup/**` | Backup |
| `paper2/2_related.tex` | Commented out in `main.tex` (`%\inputbody{paper2/2_related}`) |
| `paper2/figures/**`, `paper3/figures/**`, etc. | Non-prose data directories |
| `page/graduate/**`, `config/**` | Template infrastructure (not prose) |
| `zjuthesis.tex`, `zjuthesis.cls` | Template infrastructure |

**Note:** `paper{1,2,3}_backup/` directories collectively contain ~200+ `我们` hits. These are correctly excluded per task directive: "Do NOT include backup trees as unresolved blockers."

---

## 3. Search Methodology Verification

| Step | Tool | Scope | Result |
|------|------|-------|--------|
| 1 | `read content.tex` | Identify active includes | 5 chapters, 20 sub-files |
| 2 | `grep "我们" intro/*.tex` | Intro only | 5 hits in 2 files |
| 3 | `grep "我们" paper1/*.tex` | Paper 1 only | 0 hits (files_with_matches) |
| 4 | `grep "我们" paper2/*.tex` | Paper 2 only | 4 files w/ matches |
| 5 | `grep "我们" paper3/*.tex` | Paper 3 only | 4 files w/ matches |
| 6 | `grep "我们" conclusion.tex` | Conclusion only | 0 hits |
| 7 | `grep "我们" paper2/4_method.tex` | Full context | 14 hits, verified |
| 8 | `grep "我们" paper2/5_results.tex` | Full context | 13 hits, verified |
| 9 | `grep "我们" paper3/3_simulation.tex` | Full context | 17 hits, verified |
| 10 | `grep "我们" paper3/4_results.tex` | Full context | 19 hits, verified |
| 11 | `grep "我们" intro/*.tex` | Full context | 5 hits, verified |

**No double-counting, no missed files.**

---

## 4. Boundary Cases & Ambiguities

### 4.1 Figure Captions (`\caption[...]{...我们...}`)
- **paper2/4_method.tex** line ~73: `\caption[...]{...我们分别考虑...}`
- **paper2/5_results.tex** line ~83: `\caption[...]{...没有我们的方法时...}`
- **paper2/5_results.tex** line ~109: `\caption[...]{...我们使用...}`
- **paper2/5_results.tex** line ~121: `\caption[...]{...我们的方法识别...}`
- **paper3/2_representation.tex** line 12: `\caption[...]{...我们比较了...}`
- **paper3/2_representation.tex** line 35: `\caption[...]{...我们通过滑动...}`
- **paper3/3_simulation.tex** line 114: `\caption[...]{...我们提取...}`
- **paper3/4_results.tex** line 312: `\caption[...]{...我们的方法...}`

**Decision:** Included in inventory but classified as LOW rewrite priority (figure captions). These are borderline and depend on thesis style guide.

### 4.2 Mathematical Reasoning ("不失一般性，我们假设...")
- **paper3/2_foundation.tex** line 11
- **paper2/4_method.tex** line ~81 ("为简单起见，我们首先考虑同质情形...")

**Decision:** Included but classified as T (technical/math reasoning). These are weaker violations — impersonal phrasing ("不失一般性，可假设...") is preferable but not a hard blocker.

### 4.3 "我们的方法" (Possessive)
- Arguably the most defensible `我们` usage since `本文的方法` is the natural replacement

**Decision:** Tracked identically to other authorial uses. Replacement is straightforward (`我们的方法` → `本文方法` or `所提方法`).

---

## 5. Verification Checklist

- [x] All 20 active `.tex` files searched for `我们`
- [x] All backup directories correctly excluded
- [x] Commented-out includes correctly excluded (`paper2/2_related.tex`)
- [x] Each hit assigned file path and line context
- [x] Classification scheme applied (A/T/C → HIGH/MEDIUM/LOW)
- [x] Paper 1 confirmed clean (0 hits) — aligns with known migration
- [x] Conclusion confirmed clean (0 hits)
- [x] No false positives (e.g., `我们` inside BibTeX entries, LaTeX macros)
- [x] Total count reconciled: 5 + 0 + 29 + 39 + 0 = 73

---

## 6. Confidence Level

**HIGH.** All active files searched. All backup trees excluded. All hits classified. No unverified boundary cases remain.
