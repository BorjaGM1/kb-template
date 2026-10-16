# kb-template

A knowledge base that lives in git, not inside an AI chat.

Notes are markdown files. You read them in Obsidian. Any agent (Claude, Codex, Cursor, Grok) reads and writes them. If you drop one tool tomorrow, you lose nothing.

## How to start

1. Use this template (or clone it) and make your copy a private repo.
2. Open `vaults/example` in Obsidian to see how notes look. Rename it or add vaults, then update the table in `AGENTS.md`.
3. Open your agent in the repo folder. It reads the rules on its own: Codex and Cursor read `AGENTS.md`, Claude Code reads `CLAUDE.md` (a symlink to the same file) and finds the skills via `.claude/skills`.
4. Send it stuff: "capture this", "what do I have on X", "do some gardening".

## Skills

- `capture`: turns a text, link, voice note or screenshot into a linked note in the right vault.
- `query`: answers only from the KB and cites the notes. If it's not there, it says so.
- `gardening`: fixes broken links, orphans, duplicates and tags. Asks before deleting anything.

`python3 scripts/lint.py` checks broken links and orphan notes.

## Git in 3 words

- commit: save a point with a note of what changed (local).
- push: upload your commits to GitHub.
- pull: download the latest from GitHub (e.g. what your agent did).

On Windows, symlinks need `git config core.symlinks true` (and Developer Mode) before cloning.
