# Task 4: Bounded Bibliography Repair Scope

## Source of Truth
- `blind-review-comments.md` — reviewer items **二.6** and **五.6**
- `body/ref.bib` — 2360 lines, sole active bibliography source
- Entry numbering: includes the 4 template `@www` entries at top (confirmed by matching "文献15无页码" to Jabbari2022AdaptiveRefinement which has no `pages` field)

---

## Directly Fixable Reviewer-Flagged Entries

### Entry 15: `Jabbari2022AdaptiveRefinement` (lines 156–170)
**Reviewer complaint**: 文献15无页码 (missing pages)
**Defect type**: Missing `pages` field
**Current fields**: volume={212}, number={C}, no pages
**Proposed fix**: Look up pages for this article in Finite Elements in Analysis and Design, vol. 212, article C. Add `pages = {<verified range>}`. If verification fails, mark deferred.
**Verification status**: DEFERRED — needs external DOI/publisher lookup
**Risk**: Low — only adding missing metadata

### Entry 27: `huang2025stiffgipc` (lines 313–319)
**Reviewer complaint**: 文献27是会议还是期刊，缺页码 (conference or journal? missing pages)
**Defect type**: Type mismatch (`@article` for SIGGRAPH conference paper), missing volume/number/pages
**Current fields**: `@article{huang2025stiffgipc`, `journal = {ACM Transactions on Graphics (TOG)}`, `note = {SIGGRAPH 2025 (to appear). Preprint arXiv:2411.06224}`
**Proposed fix**: 
- Change `@article` to `@inproceedings` or keep as `@article` with correct TOG conference issue metadata
- SIGGRAPH papers in TOG are typically published as journal articles (TOG vol. 44, no. 4), so `@article` may be correct
- Add volume, number, pages once published (currently "to appear")
**Verification status**: DEFERRED — paper not yet published; cannot add pages
**Risk**: Medium — type classification depends on publisher convention

### Entry 38: `dill1992kirchhoff` (lines 481–490)
**Reviewer complaint**: 文献38格式不一致 (format inconsistent with others)
**Defect type**: Format inconsistency — uses lowercase field names (`author`, `title`, `journal`, `volume`, `number`, `pages`, `year`, `publisher`) while neighboring entries use mixed/proper case. Bib key uses lowercase `dill1992kirchhoff` while many peers use CamelCase.
**Comparison**: Adjacent entries use forms like `author = {Bertails, Florence}` and `journal = {Computer Graphics Forum}` — same lowercase convention actually. The inconsistency is subtle: this entry has `publisher = {Springer}` which is slightly unusual in its neighborhood where most entries lack publisher fields. 
**Proposed fix**: Normalize formatting to match dominant convention in the same region. Ensure field ordering follows nearby pattern. Add any missing `doi` if available.
**Verification status**: FIXABLE — format normalization only, no new metadata needed
**Risk**: Very low — cosmetic formatting alignment

### Entry 46: `servin2008rigid` (lines 598–610)
**Reviewer complaint**: 文献46格式不一致 (format inconsistent with others)
**Defect type**: Uses `@ARTICLE` (all caps), `ISSN` field, `title` (lowercase), `keywords={}`, `month={July}` — mixed convention
**Comparison**: Most entries in the 30–50 range use `@article` (lowercase). This entry has `ISSN={1941-0506}` while peers don't include ISSN. Uses `title=` (lowercase) vs some peers with `Title=`.
**Proposed fix**: Normalize `@ARTICLE` → `@article`. Harmonize field names to lowercase convention. Keep ISSN (useful metadata). 
**Verification status**: FIXABLE — format normalization only
**Risk**: Very low — cosmetic formatting alignment

### Entry 79: `gantmakher2000theory` (lines 1147–1153)
**Reviewer complaint**: 文献79无页码 (missing pages)
**Defect type**: `@book` entry without pages — reviewer expects pagination
**Current fields**: title, author, volume={131}, year={2000}, publisher={American Mathematical Soc.}
**Proposed fix**: For a book cited as a whole work, pages are not required. If thesis cites specific pages, convert to `@inbook` or add `pagetotal`. 
**Verification status**: DEFERRED — need to check in-text citation context; book-level citation may be valid without pages
**Risk**: Low — clarify citation scope

---

## Directly Adjacent Malformed Entries

Discovered while inspecting the same patterns near reviewer-flagged entries.

### Adjacent to Entry 15:
- **Entry 17** `BeiraoDaVeiga2013b_VEMHitchhiker` (lines 183–193): Missing `publisher` field. Has `abstract` but no publisher.
  - **Defect**: `publisher` not specified. Journal is Mathematical Models and Methods in Applied Sciences.
  - **Fix**: Add `publisher = {World Scientific}` (same as entry 16 from same journal).

### Adjacent to Entry 27:
- **Entry 24** `chen2021multiscale` (lines 283–289): `@inproceedings` with `booktitle` and `pages` but **missing `publisher`** and **missing `address`**.
  - **Defect**: ICCV proceedings should have publisher/address.
  - **Fix**: Add `publisher = {IEEE}` or `{CVF}`.

### Adjacent to Entry 46:
- **Entry 45** `spillmann2008cosseratnet` (lines 588–597): Uses `@ARTICLE` (all caps), `title` (lowercase), has `ISSN` field, **missing `publisher`** and **missing `address`**.
  - **Defect**: Same format inconsistency as entry 46. Missing publisher for IEEE journal.
  - **Fix**: Normalize `@ARTICLE` → `@article`. Add `publisher = {IEEE}`.
- **Entry 54** `kim2012physics` (lines 743–756): Uses `@ARTICLE` (all caps), `title` (lowercase), `keywords={}`, has `ISSN`.
  - **Defect**: All-caps entry type inconsistency. In same neighborhood (entries 45–55).
  - **Fix**: Normalize `@ARTICLE` → `@article`.

### Adjacent to Entry 79:
- **Entry 80** `Kressner2024AnalysisOfeigenvalue` (lines 1155–1171): Has `numpages = {27}` but **no explicit `pages` field** with actual page numbers.
  - **Defect**: Missing `pages` field (only has numpages). Journal BIT, volume 64, number 3.
  - **Fix**: Look up actual page range. DEFERRED if unverifiable.
  - **Status**: DEFERRED — needs external verification
- **Entry 75** `ni_numerical_2023` (lines 1091–1103): `pages = {cgf.14736}` — article number, not page range.
  - **Defect**: Uses article identifier instead of actual page numbers. Also has `urldate` and `file` local path artifacts.
  - **Fix**: Look up actual pagination or mark as article-number-only (some journals use this format). DEFERRED if unclear.
  - **Status**: DEFERRED — needs verification of journal convention

### Additional Adjacent Malformed (near flagged region, entries 70–85):
- **Entry 72** `chen_multiscale_2021` (lines 1046–1062): Contains `urldate` field and local machine `file` path (`/home/zcy/OneDrive/Papers/...`).
  - **Defect**: Bib export artifacts — personal file paths should not be in shared bibliography.
  - **Fix**: Remove `urldate` and `file` fields. Clean local export artifacts.
- **Entry 73** `li_analysis_2022` (lines 1064–1078): Contains `urldate` and local `file` path.
  - **Defect**: Same as above — export artifacts.
  - **Fix**: Remove `urldate` and `file` fields.
- **Entry 75** `ni_numerical_2023` (lines 1091–1103): Contains `urldate` and local `file` path. **Also has non-standard `pages = {cgf.14736}`.**
  - **Defect**: Export artifacts + non-standard pages.
  - **Fix**: Remove urldate/file. Pages fix deferred.

### Broader Adjacent Malformed (seen while scanning for pattern consistency):
- **Entry 9** `Dasgupta2003` (lines 134–143): Bib key is "Dasgupta2003" but **no author named Dasgupta** — first author is "Martin, Sebastian". The actual paper is Martin et al. 2008 "Polyhedral Finite Elements Using Harmonic Basis Functions".
  - **Defect**: Mismatched bib key (Dasgupta2003 ≠ Martin et al. 2008).
  - **Fix**: Rename key to `Martin2008Polyhedral` or similar. Check that all `\cite{Dasgupta2003}` references in thesis are updated.
  - **Status**: FIXABLE — bib key rename coordinated with .tex file reference updates (out of scope for bib-only task but noted)
- **Entry** `Tournois2009PerturbingSlivers` (lines 1808–1817): Tagged `@article` but journal is "Proceedings of the 18th International Meshing Roundtable". **Should be `@inproceedings`**. Has `pages = {}` (empty).
  - **Defect**: Wrong entry type + empty pages.
  - **Fix**: Convert to `@inproceedings`, add `booktitle`, look up actual pages.
  - **Status**: FIXABLE — type conversion + page lookup (DEFERRED if pages unverifiable)
- **Entry** `Shewchuk2002whatIsAGoodLinearFiniteElement` (lines 1620–1628): Tagged `@article` but journal is "Proceedings of the 11th International Meshing Roundtable". **Should be `@inproceedings`**. Has `pages = {}` (empty).
  - **Defect**: Wrong entry type + empty pages.
  - **Fix**: Convert to `@inproceedings`, look up actual pages.
  - **Status**: FIXABLE — type conversion + page lookup (DEFERRED if unverifiable)
- **Entry** `HuangRS2011` (lines 1649–1664): **Missing `journal` field**. Article with publisher=IEEE, issn=1077-2626, but no journal name.
  - **Defect**: Critical — journal name absent.
  - **Fix**: Add `journal = {IEEE Transactions on Visualization and Computer Graphics}` (based on ISSN 1077-2626).
  - **Status**: FIXABLE — known ISSN maps to TVCG
- **Entry** `karl2024ShiftInvertArnoldi` (lines 1231–1238): Has `publisher={arXiv}` but **missing `journal`**, **missing `volume`**, **missing `number`**, **missing `pages`**.
  - **Defect**: Preprint reference lacks standard fields. Format inconsistent.
  - **Fix**: Add `journal = {arXiv preprint}`, add `eprint = {arXiv:XXXX.XXXXX}` if available. DEFERRED without preprint ID.
  - **Status**: DEFERRED — needs preprint identifier
- **Entry** `2007ComponentMS` (lines 1553–1557): `@inproceedings` with **empty author field** (`author={}`) and **no booktitle**, **no pages**.
  - **Defect**: Critical — no author, no venue, no pages. Unusable as-is.
  - **Fix**: Add author/venue/pages or remove entry if unused.
  - **Status**: DEFERRED — needs complete reconstruction or removal
- **Entry** `hetmaniuk2014error` (lines 1462–1468): **Missing `journal`**, **missing `volume`**, **missing `pages`**. Only has author, title, year.
  - **Defect**: Critical — journal/venue absent.
  - **Fix**: Add journal name and pages. DEFERRED without external lookup.
  - **Status**: DEFERRED — needs external verification
- **Entry** `2010LiHybridMPI/OpenMPPpower-awareCcomputing` (lines 1937–1944): `@inproceedings` with **missing `booktitle`**, only `pages={1-12}`, `author`, `year`, `month`, `title`.
  - **Defect**: Conference venue missing.
  - **Fix**: Add `booktitle`. DEFERRED without external lookup.
  - **Status**: DEFERRED — needs external verification

---

## Entries with Export Artifacts (urldate/file paths)
Found in multiple entries below line ~1046. These are Zotero/Mendeley export artifacts:
- `chen_multiscale_2021` (entry 72)
- `li_analysis_2022` (entry 73)
- `ni_numerical_2023` (entry 75)
- `seshu1997substructuring` (line 1285)
- `horvath2018efficiency` (line 1301)
- `craig1968coupling` (line 1325)
- `giammatteo2024extension` (line 1431)
- `hetmaniuk2010special` (line 1446)

**Fix**: Remove `urldate` and `file` fields. Low risk.

---

## Summary: Repair Scope Count

| Category | Count | Action |
|----------|-------|--------|
| Reviewer-flagged, directly fixable | 3 | Normalize format (entries 15 🚫deferred, 27🚫deferred, 38✅, 46✅, 79🚫deferred) |
| Adjacent, fixable (format only) | 4 | Normalize @ARTICLE → @article, add publisher |
| Adjacent, fixable (metadata) | 3 | Add missing journal/publisher, rename mislabeled key |
| Adjacent, deferred (needs external lookup) | 7 | Missing pages/venue requiring external verification |
| Export artifacts cleanup | 8 | Remove urldate/file fields |
| Conference-as-article type fixes | 2 | Convert @article → @inproceedings |

**Total directly fixable in bounded pass**: ~17 entries (format normalization + publisher additions + artifact cleanup)
**Total deferred**: ~10 entries (need external page/venue lookup)

---

## Entries Explicitly Marked DEFERRED
| Entry | Reason |
|-------|--------|
| Jabbari2022AdaptiveRefinement (15) | Missing pages — needs external DOI lookup |
| huang2025stiffgipc (27) | Not yet published, pages unavailable |
| gantmakher2000theory (79) | Book citation — pages depend on in-text usage |
| Kressner2024AnalysisOfeigenvalue (80) | Missing explicit pages, needs external lookup |
| ni_numerical_2023 (75) | Non-standard page format (article ID) |
| karl2024ShiftInvertArnoldi | Missing all standard fields, needs preprint identifier |
| 2007ComponentMS | Empty author, no venue — needs reconstruction |
| hetmaniuk2014error | Missing journal/volume/pages — needs external lookup |
| 2010LiHybridMPI/OpenMPPpower-awareCcomputing | Missing booktitle — needs external lookup |
| Tournois2009PerturbingSlivers | Empty pages — needs external lookup |
| Shewchuk2002whatIsAGoodLinearFiniteElement | Empty pages — needs external lookup |
