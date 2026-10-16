---
name: query
description: Answer the owner's questions using only the knowledge base, citing the notes used, without inventing anything.
---
# Query

1. Pull latest (`git pull --rebase`) or read via GitHub API.
2. Pick the vault(s) by topic.
3. Search: `rg -i "<terms>" vaults/<v>` incl. synonyms, tags (`#tag`), aliases in frontmatter; start from `Home.md` / MOCs and follow `[[links]]`.
4. Read the matching notes fully, not just grep hits.
5. Answer in the owner's language, concisely, citing each fact with its note: `([[Note]], vault personal)`.
6. If the KB doesn't contain the answer, say so plainly. You may add general knowledge only if clearly labelled as not from the KB.
7. Point out contradictions or stale notes you found (old `updated`) and offer gardening.
8. Read-only: do not edit notes during a query unless asked (then use capture).
