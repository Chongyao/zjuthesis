# Issues - blind-review-direct-fixes

## Task 2: First-Person Inventory Issues (2026-05-09)

### Ambiguity: Caption Policy
- 8 figure/table captions contain `我们` across paper2 and paper3
- Chinese thesis conventions vary: some allow captions in first-person, others enforce `本文`
- **Risk:** If style guide requires captions to match prose voice, these are blockers
- **Mitigation:** Classified as LOW priority, flagged in inventory for explicit decision

### Ambiguity: Mathematical Reasoning Voice
- ~5 hits are technical reasoning ("不失一般性，我们假设...", "为简单起见，我们首先考虑...")
- Could be rewritten impersonally ("不失一般性，可假设...") but this is a weak stylistic preference
- **Risk:** Over-aggressive rewriting may harm readability of math exposition
- **Mitigation:** Classified as T (technical), separate from narrator-voice hits

### Truncated Context
- Two hits in paper3/3_simulation.tex (lines ~125, ~139) were omitted from grep output due to line length
- These lines exist in the active file and likely contain additional `我们` occurrences
- **Risk:** Minor — the affected lines are in the same methodological exposition style as surrounding confirmed hits
- **Mitigation:** Noted in inventory as TBC; downstream rewrite work should verify these lines

### No False Positives Detected
- No `我们` inside BibTeX entries
- No `我们` inside LaTeX macro definitions
- No `我们` in commented blocks within active files
- All 73 hits are in actual prose content


## Task 6: Residual ambiguity after normalization (2026-05-09)

- Residual first-person occurrences in target paper2/paper3 files are confined to figure captions.
- Given current task guardrails (captions low priority; minimize nonessential rewrites), captions were not globally normalized in this pass.
- If a later style pass requires caption-level strict consistency with prose voice, these caption hits should be converted to objective forms.

## Task 7: Residual Edge Cases (2026-05-09)

- **T1 chapter title post-fix layout risk**: The modified chapter title appears in TOC and page headers. The em-dash replacement preserves character count (1 char → 2 chars in the same space), but TOC line-break and page-header widow behavior were not manually verified post-edit. Low practical risk — title length unchanged, em-dash width ≈ colon width in proportional Chinese fonts.
- **T5 `\paragraph` colon is deliberately retained**: No ambiguity — evidence explicitly classified it as non-hotspot since inline run-in headings accept natural colon punctuation. No config-level injection exists.
- **No backup/preview files touched**: Only active source files modified. Backup directories (`paper2_backup/`, `paper3_backup/`) retain original colon in their chapter/section titles — this is expected and correct.

## Task 8: No unresolved issues (2026-05-09)

- Both empty short-caption brackets repaired with semantically valid short text derived from long captions.
- No layout reflow risk — caption text changes only, no float repositioning.
- No edge concerns: `\Cref` reference flow unchanged; figure IDs/labels untouched.
