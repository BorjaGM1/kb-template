#!/usr/bin/env python3
"""Report broken [[wikilinks]] and orphan notes in Obsidian vaults.

Usage: python3 scripts/lint.py [vault_dir ...]   (default: every dir in vaults/)
Exit code 1 if problems are found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(!?)\[\[([^\]|#^]*)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
EXEMPT_ORPHAN = {"home"}


def aliases(text):
    text = text.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return []
    fm = m.group(1)
    a = re.search(r"^aliases:\s*\[(.*?)\]", fm, re.M)
    if a:
        return [x.strip().strip("'\"") for x in a.group(1).split(",") if x.strip()]
    a = re.search(r"^aliases:\s*\n((?:\s*-\s*.+\n?)+)", fm, re.M)
    if a:
        return [l.split("-", 1)[1].strip().strip("'\"") for l in a.group(1).splitlines()]
    return []


def lint(vault: Path):
    notes = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts and ".trash" not in p.parts]
    files = {p.relative_to(vault).as_posix().lower() for p in vault.rglob("*") if p.is_file()}
    names = {}
    for p in notes:
        names[p.stem.lower()] = p
        for al in aliases(p.read_text(encoding="utf-8")):
            names[al.lower()] = p
    inbound = {p: 0 for p in notes}
    broken = []
    for p in notes:
        text = FENCE.sub("", p.read_text(encoding="utf-8"))
        for emb, target in LINK.findall(text):
            t = target.strip()
            if not t:
                continue
            key = t.lower()
            dest = names.get(key) or names.get(key.rsplit("/", 1)[-1].removesuffix(".md"))
            if dest is None and key.removesuffix(".md") + ".md" not in files and key not in files \
                    and not any(f.endswith("/" + key) or f == key for f in files):
                broken.append((p.relative_to(vault), t))
            elif dest is not None and dest != p:
                inbound[dest] += 1
    orphans = [p.relative_to(vault) for p, n in inbound.items()
               if n == 0 and p.stem.lower() not in EXEMPT_ORPHAN
               and "Inbox" not in p.relative_to(vault).parts]
    return broken, sorted(orphans)


def main():
    vaults = [Path(a) for a in sys.argv[1:]] or sorted(
        d for d in (ROOT / "vaults").iterdir() if d.is_dir())
    problems = 0
    for v in vaults:
        broken, orphans = lint(v)
        print(f"## {v.name}: {len(broken)} broken link(s), {len(orphans)} orphan(s)")
        for src, t in broken:
            print(f"  BROKEN  {src} -> [[{t}]]")
        for o in orphans:
            print(f"  ORPHAN  {o}")
        problems += len(broken) + len(orphans)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
