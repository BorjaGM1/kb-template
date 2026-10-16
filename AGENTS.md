# AGENTS.md: rules for any agent

## Scope (what goes in)
- **Only content the owner explicitly sends.** No pulling in other tools' memories, inboxes or chats on your own initiative.
- **Excluded topics**: list here anything that must never enter the KB (e.g. work under NDA). Default: none.
- **Never store secrets**: no tokens, passwords, API keys, private keys, recovery codes, card numbers. Replace with a pointer ("token stored in password manager") or omit.
- **Never invent facts.** Record what was sent; mark your own inferences as such (`> [!note] Agent inference`). If unsure, leave it in `Inbox/` with a question.

## Which vault
Each vault is a separate Obsidian vault under `vaults/`. Example layout:

| Vault | Content |
|---|---|
| `vaults/personal` | Personal life, ideas, learning, side projects, default when unclear |
| `vaults/work` | Your business or job (products, content, processes) |
| `vaults/agency` | Client work (clients, deliverables, processes) |

This template ships with a single `vaults/example`. Rename it or add more and update this table.
Do not cross-link between vaults with wikilinks (they are separate Obsidian vaults); mention the other vault in plain text if needed. If ambiguous, use the default vault's `Inbox/` and ask.

## Obsidian style
- **Small atomic notes**: one idea, person, project, decision or source per note.
- **Language**: English (change to yours). Write note content in this language; quote sources in their original language when needed.
- **Links**: `[[Note title]]` / `[[Note title|alias]]` wikilinks, never Markdown links between notes. Every note links to at least one other note or MOC.
- **Tags**: lowercase, kebab-case, few, e.g. `#person`, `#project`, `#decision`, `#source`, `#idea`. Nested allowed (`#project/web`).
- **MOCs**: each vault has `Home.md` as the root MOC. Add topic MOCs (`MOC - Topic.md`) only when a topic has ~5+ notes. Keep MOCs short lists of links with one-line context.
- **Frontmatter** (required on every note):
```yaml
---
created: 2026-10-15
updated: 2026-10-15
source: "chat message" | URL | "voice note" | ...
tags: [idea]
---
```
  Optional: `aliases: []`, `status: active|archived`.

## File naming
- Filename = note title, human-readable, English, `Title Case or sentence case.md` (e.g. `Newsletter Signup Flow.md`). No dates in names except for logs (`2026-10-15 Meeting X.md`).
- No `/ \ : * ? " < > | # ^ [ ]` in filenames. Keep titles unique within a vault.
- Attachments go in `attachments/` inside the vault.
- Folders stay shallow: `Inbox/`, optionally a few top-level area folders. Prefer links and tags over deep folders.

## Workflow
1. Work in a **local clone**. **Always `git pull --rebase` before editing**, and **push immediately after** committing.
2. **One commit per logical change**, message like `capture(personal): Newsletter signup flow` / `garden(agency): merge duplicate client notes`.
3. On conflicts: **resolve, never overwrite**. Never `push --force`. Merge both sides' content; if unclear, keep both and flag in the note.
4. Quick reads or single-note appends may use the GitHub API without a clone (fetch latest sha first).
5. Run `python3 scripts/lint.py` after structural changes (moves, renames, merges).
6. **Ask the owner before deleting notes** (or merging that drops content). Archiving (`status: archived`) is fine.
7. Commit directly to `main`; no branches/PRs unless the owner asks.

## Skills
See `skills/`: `capture`, `query`, `gardening`. Follow their steps.
