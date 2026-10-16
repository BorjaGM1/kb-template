---
name: capture
description: Turn something the owner sends (text, link, voice note transcript, screenshot) into a well-formed, linked note in the right vault.
---
# Capture

1. From the repo root: `git pull --rebase`.
2. Check scope (AGENTS.md): sent explicitly? Not an excluded topic? Strip any secrets.
3. Extract content:
   - Text: use as-is, tidy wording, keep meaning.
   - Link: fetch the page; note title, author, date, 3-7 key points, the URL in `source`.
   - Voice: transcribe; keep the owner's intent; drop filler.
   - Long threads (X, forums): read replies in full text, not truncated snippets, and beyond the first page. On huge threads cover the substantive bulk (author replies, high-signal replies). **State coverage in the note** (e.g. "read 40 of 55 author replies").
   - Screenshot/image: describe/OCR relevant text; store image in `attachments/` if useful.
4. Pick the vault (table in AGENTS.md). Unclear: default vault `Inbox/` + a question to the owner.
5. Search for existing notes on the same topic (`rg -il "<keywords>" vaults/<v>`). Prefer updating an existing note (bump `updated`) over creating a duplicate.
6. If new: one atomic note per idea; split if the input covers several. Filename per AGENTS.md; frontmatter `created/updated/source/tags`; English content and English tags.
7. Link it: at least one `[[link]]` to a related note or MOC, and add it to the relevant MOC (or `Home.md`). Unsorted: `Inbox/`.
8. Never invent; mark inferences.
9. **Review before commit:** reread the draft note(s) next to related/linked notes and the vault's existing tags (`rg -h '^tags:' vaults/<v> | tr -d '[]' | tr ',' '\n' | sed 's/^ *//' | sort -u`). Check and fix:
   - Body and tags are English.
   - Tags fit the topic and match sibling/linked notes.
   - Reuse existing tags before inventing new ones.
   - Wikilinks and MOC / `Home.md` entries are complete.
   - No invented facts; inferences marked.
10. `python3 scripts/lint.py vaults/<v>`; commit `capture(<v>): <title>`; push immediately.
11. Reply briefly with the note(s) created/updated.
