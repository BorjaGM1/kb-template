---
name: gardening
description: Lint and tidy the vaults (broken links, orphans, duplicates, stale notes, tags, MOCs) and produce a report. Deletions require the owner's OK.
---
# Gardening

1. From the repo root: `git pull --rebase`.
2. Run `python3 scripts/lint.py` (all vaults) and collect output.
3. **Broken links**: fix typos/renames by pointing to the existing note; if the target is genuinely missing, create a stub only if useful, else unlink. Never fabricate content.
4. **Orphans**: link each orphan from a related note or MOC; if it doesn't fit, move to `Inbox/`.
5. **Duplicates**: find similar titles/aliases/content (`rg`, compare). Merge into the better note (keep all facts, union of sources, add alias, redirect links). Merges that drop content or remove files: propose, don't do.
6. **Stale notes**: `updated` > 6 months, empty stubs, finished projects: propose `status: archived` or deletion.
7. **Tags**: normalize case/kebab-case, merge synonyms (`#ideas` to `#idea`), remove one-off noise tags.
8. **Frontmatter**: ensure created/updated/source/tags present and valid.
9. **Inbox**: file notes from `Inbox/` into the right place when clear.
10. **MOCs**: keep `Home.md` and topic MOCs current; create a MOC when a topic reaches ~5 notes.
11. Re-run lint; commit per logical change (`garden(<v>): ...`); push right after each.
12. **Report** to the owner: what was fixed, plus proposed deletions/merges/archives needing approval. **Never delete without the owner's OK.**
