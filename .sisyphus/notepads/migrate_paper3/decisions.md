## Decisions Made During Migration

### 1. Figure Copy Permission Errors
**Decision**: Accept partial copy with permission errors on .out files
**Rationale**: .out files are simulation output logs, not needed for LaTeX compilation

### 2. BibTeX Key Extraction Strategy
**Decision**: Extract keys from existing ref.bib using grep for '@[a-zA-Z]*{' patterns
**Rationale**: Simple and effective for identifying existing entries

### 3. String Entries Handling
**Decision**: Include @String definitions from source as they may be referenced by entries
**Rationale**: Prevents undefined string reference errors in LaTeX

### 4. Duplicate Detection
**Decision**: Use exact key matching (case-sensitive)
**Rationale**: BibTeX keys are case-sensitive; different case = different entries
