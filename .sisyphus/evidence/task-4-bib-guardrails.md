# Task 4: Bibliography Repair Guardrails

## Guiding Principle
This audit is **bounded** — it covers only reviewer-flagged bibliography entries (`二.6`, `五.6`) and **directly adjacent** malformed entries discovered while inspecting the same defect patterns. No full-database rewrite.

---

## Do-Not-Expand Section

### 1. Do NOT normalize the entire 2360-line bib database
**Rationale**: The reviewer complaints (`二.6` and `五.6`) flag specific entries (15, 27, 38, 46, 79) plus general formatting issues. A full-database rewrite would:
- Risk introducing new errors in untested entries
- Exceed the direct-fix scope defined in the plan
- Make the change set unreviewable

**Scope boundary**: Edits limited to:
- The 5 explicitly flagged entries (15, 27, 38, 46, 79)
- Directly adjacent entries (within ±3 positions of flagged entries) showing the SAME defect pattern
- Entries with identifiable metadata defects (missing journal, missing publisher) within the flagged regions
- Export artifact cleanup (urldate/file fields) in entries near the flagged region

### 2. Do NOT guess venue type or page ranges
**Rationale**: For entries like Jabbari2022AdaptiveRefinement (missing pages), huang2025stiffgipc (preprint), and gantmakher2000theory (book without pages), we cannot fabricate metadata. These are marked **DEFERRED**.

**Deferred vs. Fixable boundaries**:
- ✅ FIXABLE: `@ARTICLE` → `@article` (cosmetic, no metadata change)
- ✅ FIXABLE: Adding `publisher = {IEEE}` when ISSN/journal clearly identifies the publisher
- ✅ FIXABLE: Adding `journal = {IEEE TVCG}` when ISSN 1077-2626 is present
- ✅ FIXABLE: Removing `urldate` and local `file` paths (export artifacts)
- 🚫 DEFERRED: Adding `pages = {...}` without external verification
- 🚫 DEFERRED: Adding `volume = {...}` for preprint entries
- 🚫 DEFERRED: Reconstructing entries with empty/missing core fields (author, title, venue)

### 3. Do NOT change entry types based on speculation
**Rationale**: Some `@article` entries have "Proceedings" in their journal name (Tournois2009PerturbingSlivers, Shewchuk2002whatIsAGoodLinearFiniteElement). Changing to `@inproceedings` is a metadata assertion. These are noted as fixable but only if verified.

### 4. Do NOT modify citation infrastructure
**Rationale**: The plan explicitly says "change entry data, not citation infrastructure." The bib style (`config/format/general/reference.tex`) is OUT OF SCOPE. Issues like "journal names not italicized" are controlled by the biblatex style, not bib data.

### 5. Do NOT touch entries outside the flagged regions unless they share the exact same defect
**Rationale**: The bib file contains entries from multiple domains (graphics simulation, numerical methods, structural dynamics). Unrelated cleanup risks scope creep.

### 6. Do NOT modify `@String` declarations or template entries
**Rationale**: The `@String{cgforum}` and `@String{tog}` declarations and the 4 template `@www` entries (zjuthesisrules, tikz, zjuthesis, zjugradthesisrules) are not reviewer-flagged and are part of the template infrastructure.

---

## Scope Boundary Map

```
Lines 1–30:    @www templates + @String declarations → OUT OF SCOPE
Lines 31–155:  Entries 5–14 (Thingi10K to SukumarMalsch2006) → OUT OF SCOPE (check entry 9 Dasgupta2003 for key mismatch only)
Lines 156–170: Entry 15 (Jabbari2022AdaptiveRefinement) → IN SCOPE (flagged), DEFERRED
Lines 172–193: Entries 16–17 (VEM papers) → ADJACENT, entry 17 fixable (missing publisher)
Lines 283–289: Entry 24 (chen2021multiscale) → ADJACENT to 27, fixable (missing publisher)
Lines 313–319: Entry 27 (huang2025stiffgipc) → IN SCOPE (flagged), DEFERRED
Lines 481–490: Entry 38 (dill1992kirchhoff) → IN SCOPE (flagged), FIXABLE (format)
Lines 492–503: Entry 39 (deul_direct_2018) → ADJACENT, appears complete
Lines 588–610: Entries 45–46 (spillmann2008cosseratnet, servin2008rigid) → IN SCOPE (flagged 46), BOTH FIXABLE
Lines 743–756: Entry 54 (kim2012physics) → ADJACENT to 46 pattern, FIXABLE (format)
Lines 1046–1103: Entries 72–75 (chen_multiscale_2021 to ni_numerical_2023) → ADJACENT to 79, PARTIALLY FIXABLE (export artifacts)
Lines 1147–1171: Entries 79–80 (gantmakher2000theory, Kressner2024) → IN SCOPE (flagged 79), BOTH DEFERRED
Lines 1620–1628: Shewchuk2002whatIsAGoodLinearFiniteElement → ADJACENT malformed, DEFERRED
Lines 1649–1664: HuangRS2011 → ADJACENT malformed, FIXABLE (missing journal)
Lines 1808–1817: Tournois2009PerturbingSlivers → ADJACENT malformed, DEFERRED
```

---

## Verification Checks for Task 10

When Task 10 executes the actual bib edits, verify:
1. Only entries in the above scope map are modified
2. No `@String` declarations are touched
3. No template `@www` entries are touched
4. Deferred entries are NOT modified (only documented)
5. Export artifacts (urldate, file) are removed, not other fields
6. All `@ARTICLE` → `@article` conversions preserve all field content
7. Added `publisher`/`journal` fields are verified against known ISSN/journal mappings
