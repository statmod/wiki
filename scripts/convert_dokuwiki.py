#!/usr/bin/env python3
"""Convert DokuWiki pages/media dump to MkDocs Material docs/ tree."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}
EXCLUDE_PREFIXES = ("wiki/", "playground/", "common/")
EXCLUDE_PAGES = {"navigation"}

INDEXMENU_RE = re.compile(r"\{\{indexmenu>([^}|]+)(?:\|[^}]*)?\}\}", re.I)
GALLERY_RE = re.compile(r"\{\{gallery>([^}?]+)(?:\?[^}]*)?\}\}", re.I)
NOTE_RE = re.compile(r"<note(\s+\w+)?>(.*?)</note>", re.I | re.S)
HTML_BLOCK_RE = re.compile(r"<html>(.*?)</html>", re.I | re.S)
FONT_RE = re.compile(r"</?font[^>]*>", re.I)
# Media: allow spaces inside id (legacy typos like "study:fall2009: file.pdf")
MEDIA_RE = re.compile(r"\{\{\s*([^}|]+?)(?:\?([^}|]*))?(?:\s*\|\s*([^}]*))?\s*\}\}")
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^(={2,6})\s*(.+?)\s*\1\s*$", re.M)
PH_RE = re.compile(r"¤¤PH(\d+)¤¤")


def log(msg: str) -> None:
    print(msg, flush=True)


def normalize_id(page_id: str) -> str:
    # collapse internal whitespace (legacy "study:fall2009: file")
    s = page_id.strip().strip(":").lower().replace("\\", "")
    s = re.sub(r"\s+", "", s)
    return s


def doku_id_to_relpath(page_id: str) -> str:
    return normalize_id(page_id).replace(":", "/")


def discover_pages(pages_root: Path) -> Dict[str, Path]:
    mapping: Dict[str, Path] = {}
    for txt in pages_root.rglob("*.txt"):
        rel = txt.relative_to(pages_root).as_posix()
        if any(rel.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        page_id = normalize_id(rel[:-4].replace("/", ":"))
        if page_id in EXCLUDE_PAGES:
            continue
        mapping[page_id] = txt
    return mapping


def output_md_path(page_id: str, pages_root: Path) -> Path:
    rel = doku_id_to_relpath(page_id)
    if (pages_root / rel).is_dir():
        return Path(rel) / "index.md"
    return Path(rel + ".md")


def build_id_to_docs(pages: Dict[str, Path], pages_root: Path) -> Dict[str, Path]:
    return {pid: output_md_path(pid, pages_root) for pid in pages}


def media_fs_candidates(media_root: Path, media_id: str) -> List[Path]:
    media_id = normalize_id(media_id.split("?")[0])
    rel = media_id.replace(":", "/")
    direct = media_root / rel
    if direct.is_file():
        return [direct]
    parent = media_root / Path(rel).parent
    name = Path(rel).name.lower()
    if parent.is_dir():
        matches = [p for p in parent.iterdir() if p.is_file() and p.name.lower() == name]
        if matches:
            return matches
    return []


def media_docs_rel(media_id: str) -> str:
    rel = normalize_id(media_id.split("?")[0]).replace(":", "/")
    return f"assets/{rel}"


def list_media_images(media_root: Path, ns: str) -> List[Path]:
    folder = media_root / normalize_id(ns).replace(":", "/")
    if not folder.is_dir():
        return []
    return sorted(
        p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS
    )


def relative_link(from_docs: Path, to_docs: Path) -> str:
    rel = os.path.relpath(to_docs.as_posix(), start=from_docs.parent.as_posix() or ".")
    return rel.replace(os.sep, "/")


def extract_title(text: str) -> Optional[str]:
    m = HEADING_RE.search(text)
    return m.group(2).strip() if m else None


def parse_indexmenu_target(spec: str) -> str:
    core = spec.strip().split("#")[0].strip().strip(":")
    if core.endswith(":*"):
        core = core[:-2]
    elif core.endswith("*"):
        core = core[:-1].rstrip(":")
    return normalize_id(core)


def generate_indexmenu_md(
    ns: str,
    pages: Dict[str, Path],
    id_to_docs: Dict[str, Path],
    from_page: str,
) -> str:
    prefix = ns + ":" if ns else ""
    children = []
    for pid in sorted(pages):
        if ns:
            if not pid.startswith(prefix) or pid == ns:
                continue
            rest = pid[len(prefix) :]
            if ":" in rest:
                continue
            children.append(pid)
        elif ":" not in pid:
            children.append(pid)

    lines = []
    from_docs = id_to_docs[from_page]
    for pid in children:
        title = pid.split(":")[-1]
        try:
            text = pages[pid].read_text(encoding="utf-8", errors="replace")
            m = HEADING_RE.search(text)
            if m:
                title = m.group(2).strip()
        except OSError:
            pass
        href = relative_link(from_docs, id_to_docs[pid])
        lines.append(f"- [{title}]({href})")
    if not lines:
        return f"<!-- indexmenu: no children under {ns or '/'} -->"
    return "\n".join(lines)


def generate_gallery_md(ns: str, media_root: Path, from_docs: Path) -> str:
    files = list_media_images(media_root, ns)
    if not files:
        return f"<!-- gallery empty: {ns} -->"
    lines = []
    for f in files:
        docs_target = Path("assets") / f.relative_to(media_root).as_posix()
        href = relative_link(from_docs, docs_target)
        lines.append(f"![{f.name}]({href})")
    return "\n\n".join(lines)


def resolve_wiki_target_smart(
    target: str, current_page: str, id_to_docs: Dict[str, Path]
) -> str:
    t = target.strip()
    if "#" in t:
        t = t.split("#", 1)[0].strip()
    if not t:
        return normalize_id(current_page)
    if t.startswith(":"):
        return normalize_id(t)

    cur_ns = ":".join(normalize_id(current_page).split(":")[:-1])

    if t.startswith(".."):
        parts = cur_ns.split(":") if cur_ns else []
        rest = t
        while rest.startswith(".."):
            if parts:
                parts.pop()
            rest = rest[2:]
            if rest.startswith(":"):
                rest = rest[1:]
        if rest:
            parts.append(normalize_id(rest))
        return normalize_id(":".join(parts))

    if t.startswith("."):
        rest = t[1:]
        if rest.startswith(":"):
            rest = rest[1:]
        return normalize_id(f"{cur_ns}:{rest}" if cur_ns else rest)

    if ":" in t:
        return normalize_id(t)

    # bare name: current ns, then root
    if cur_ns:
        cand = normalize_id(f"{cur_ns}:{t}")
        if cand in id_to_docs:
            return cand
    root = normalize_id(t)
    if root in id_to_docs:
        return root
    if cur_ns:
        return normalize_id(f"{cur_ns}:{t}")
    return root


class PlaceholderStore:
    def __init__(self) -> None:
        self._items: List[str] = []

    def put(self, md_snippet: str) -> str:
        idx = len(self._items)
        self._items.append(md_snippet)
        # Use characters unlikely to be altered by pandoc dokuwiki reader
        return f"¤¤PH{idx}¤¤"

    def restore(self, text: str) -> str:
        def repl(m: re.Match) -> str:
            i = int(m.group(1))
            if 0 <= i < len(self._items):
                return self._items[i]
            return m.group(0)

        # Pandoc may escape or alter placeholders; try several forms
        text = PH_RE.sub(repl, text)
        text = re.sub(r"¤¤PH(\d+)¤¤", repl, text)
        text = re.sub(r"&curren;&curren;PH(\d+)&curren;&curren;", repl, text)
        text = re.sub(r"¤¤PH(\d+)¤¤", repl, text)
        # underscore/backslash variants
        text = re.sub(r"¤\\?¤PH(\d+)¤\\?¤", repl, text)
        return text


def preprocess(
    text: str,
    page_id: str,
    pages: Dict[str, Path],
    id_to_docs: Dict[str, Path],
    media_root: Path,
    missing_media: List[Tuple[str, str]],
    store: PlaceholderStore,
) -> str:
    from_docs = id_to_docs[page_id]

    def repl_indexmenu(m: re.Match) -> str:
        ns = parse_indexmenu_target(m.group(1))
        md = generate_indexmenu_md(ns, pages, id_to_docs, page_id)
        return store.put("\n\n" + md + "\n\n")

    text = INDEXMENU_RE.sub(repl_indexmenu, text)

    def repl_gallery(m: re.Match) -> str:
        ns = normalize_id(m.group(1).strip().strip(":"))
        md = generate_gallery_md(ns, media_root, from_docs)
        return store.put("\n\n" + md + "\n\n")

    text = GALLERY_RE.sub(repl_gallery, text)

    def repl_note(m: re.Match) -> str:
        kind = (m.group(1) or "note").strip().lower() or "note"
        adm = {"tip": "tip", "warning": "warning", "important": "important"}.get(kind, "note")
        body = m.group(2).strip()
        # Recursively convert links/media inside note? Keep as plain text for now;
        # notes often have plain prose. Still run link/media on the whole doc first
        # — notes are replaced before links, so convert inner wiki syntax lightly.
        body_conv = body
        indented = "\n".join(("    " + line) if line.strip() else "" for line in body_conv.splitlines())
        return store.put(f"\n\n!!! {adm}\n\n{indented}\n\n")

    text = NOTE_RE.sub(repl_note, text)

    def repl_html(m: re.Match) -> str:
        inner = FONT_RE.sub("", m.group(1)).strip()
        return store.put("\n\n" + inner + "\n\n")

    text = HTML_BLOCK_RE.sub(repl_html, text)
    text = FONT_RE.sub("", text)

    def repl_media(m: re.Match) -> str:
        raw = m.group(1).strip()
        query = (m.group(2) or "").strip()
        title = (m.group(3) or "").strip()
        if raw.lower().startswith(("indexmenu>", "gallery>")):
            return m.group(0)
        if re.match(r"https?://", raw, re.I):
            return store.put(f"[{title or raw}]({raw})")
        # Normalize id but preserve path for lookup; strip odd spaces
        media_id = normalize_id(raw)
        width = None
        if query:
            wm = re.match(r"(\d+)(?:x(\d+))?", query)
            if wm:
                width = wm.group(1)
        cands = media_fs_candidates(media_root, media_id)
        if not cands:
            # try without collapsing spaces differently — already collapsed
            # try original with spaces→nothing already done
            missing_media.append((page_id, media_id))
            docs_rel = media_docs_rel(media_id)
        else:
            docs_rel = "assets/" + cands[0].relative_to(media_root).as_posix()
        href = relative_link(from_docs, Path(docs_rel))
        label = title or Path(docs_rel).name
        ext = Path(docs_rel).suffix.lower()
        if ext in IMAGE_EXTS:
            if width:
                snippet = f'<img src="{href}" alt="{label}" width="{width}" />'
            else:
                snippet = f"![{label}]({href})"
        else:
            snippet = f"[{label}]({href})"
        return store.put(snippet)

    text = MEDIA_RE.sub(repl_media, text)

    def repl_link(m: re.Match) -> str:
        inner = m.group(1).strip()
        if "|" in inner:
            target, label = inner.split("|", 1)
            target, label = target.strip(), label.strip()
        else:
            target, label = inner.strip(), ""

        if re.match(r"https?://", target, re.I) or target.startswith("//"):
            return store.put(f"[{label or target}]({target})")
        if "@" in target and "://" not in target:
            if re.match(r"^[^\[\]/\s]+@[^\[\]/\s]+$", target):
                return store.put(f"[{label or target}](mailto:{target})")
        if re.match(r"^(doku|wp|go|php|amazon|google|skype|tel|bug)>", target, re.I):
            return store.put(f"`{label or target}`")
        if target.startswith(("en.wikipedia.org/", "ru.wikipedia.org/")):
            return store.put(f"[{label or target}](https://{target})")
        if target.startswith("#"):
            return store.put(f"[{label or target}]({target})")
        if "://" in target:
            return store.put(f"`{target}`")
        # Footnote-like or code indexes e.g. [[1]] — leave as literal text
        if re.fullmatch(r"\d+", target):
            return target if not label else f"{label}"

        resolved = resolve_wiki_target_smart(target, page_id, id_to_docs)
        if not label:
            label = target.split(":")[-1] if target else resolved
        if resolved in id_to_docs:
            href = relative_link(from_docs, id_to_docs[resolved])
            return store.put(f"[{label}]({href})")
        return store.put(f"[{label}](BROKEN:{resolved})")

    text = LINK_RE.sub(repl_link, text)
    return text


def run_pandoc(src_text: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as inf:
        inf.write(src_text)
        in_path = inf.name
    out_path = in_path + ".md"
    try:
        proc = subprocess.run(
            ["pandoc", "--wrap=none", "-f", "dokuwiki", "-t", "gfm", "-o", out_path, in_path],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise subprocess.CalledProcessError(proc.returncode, proc.args, proc.stdout, proc.stderr)
        return Path(out_path).read_text(encoding="utf-8")
    finally:
        for p in (in_path, out_path):
            try:
                os.unlink(p)
            except OSError:
                pass


def fallback_convert(text: str) -> str:
    """Lightweight conversion when pandoc fails (complex tables)."""
    # Headings
    def heading(m: re.Match) -> str:
        level = 7 - len(m.group(1))  # ====== → 1
        level = max(1, min(6, level))
        return "#" * level + " " + m.group(2).strip()

    out = HEADING_RE.sub(heading, text)
    # bold / italic (rough)
    out = re.sub(r"\*\*(.+?)\*\*", r"**\1**", out)
    out = re.sub(r"(?<!:)//(.+?)//", r"*\1*", out)
    # linebreaks
    out = out.replace("\\\\", "  \n")
    # DokuWiki tables → GFM tables (best-effort): ^ header, | row
    lines = []
    for line in out.splitlines():
        if line.startswith("^") or (line.startswith("|") and line.endswith("|")):
            cells = re.split(r"\^|\|", line)
            cells = [c.strip() for c in cells if c.strip() != "" or True]
            # split properly
            raw_cells = re.split(r"[\^|]", line)
            raw_cells = [c.strip() for c in raw_cells]
            if raw_cells and raw_cells[0] == "":
                raw_cells = raw_cells[1:]
            if raw_cells and raw_cells[-1] == "":
                raw_cells = raw_cells[:-1]
            row = "| " + " | ".join(raw_cells) + " |"
            lines.append(row)
            if line.startswith("^"):
                lines.append("| " + " | ".join(["---"] * len(raw_cells)) + " |")
        else:
            lines.append(line)
    return "\n".join(lines)


def finalize_md(md: str, title: Optional[str], store: PlaceholderStore) -> str:
    md = store.restore(md)
    # Unescape leftover backslash-escapes from pandoc
    md = md.replace(r"\[", "[").replace(r"\]", "]")
    md = md.replace(r"\-", "-").replace(r"\*", "*")
    md = md.replace(r"\<", "<").replace(r"\>", ">")
    md = md.replace(r"\&", "&")
    # Legacy dead links on the home page
    md = md.replace("](BROKEN:doc)", "](books/index.md)")
    md = md.replace("](BROKEN:other)", "](study/index.md)")

    body = md
    if title:
        body = re.sub(r"^#\s+.+\n+", "", body, count=1)
        safe = title.replace("\\", "\\\\").replace('"', '\\"')
        body = f'---\ntitle: "{safe}"\n---\n\n' + body.lstrip()

    body = re.sub(r"\n{4,}", "\n\n\n", body)
    return body


def parse_navigation(nav_txt: Path) -> List[Tuple[int, str, str]]:
    items = []
    if not nav_txt.is_file():
        return items
    for line in nav_txt.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(\s*)\*\s*\[\[([^\]]+)\]\]", line)
        if not m:
            continue
        spaces = len(m.group(1).replace("\t", "  "))
        depth = spaces // 2
        inner = m.group(2)
        if "|" in inner:
            target, label = inner.split("|", 1)
        else:
            target, label = inner, inner
        items.append((depth, normalize_id(target.strip()), label.strip()))
    return items


def build_nav_yaml(
    nav_items: List[Tuple[int, str, str]],
    id_to_docs: Dict[str, Path],
    pages: Dict[str, Path],
) -> str:
    lines = ["nav:", "  - Home: index.md"]
    featured = set()

    def docs_entry(pid: str) -> Optional[str]:
        if pid not in id_to_docs:
            return None
        return id_to_docs[pid].as_posix()

    i = 0
    while i < len(nav_items):
        depth, pid, label = nav_items[i]
        featured.add(pid)
        entry = docs_entry(pid)
        children = []
        j = i + 1
        while j < len(nav_items) and nav_items[j][0] > depth:
            children.append(nav_items[j])
            j += 1
        indent = "  "
        if children:
            lines.append(f'{indent}- "{label}":')
            if entry:
                lines.append(f"{indent}  - Overview: {entry}")
            for _cd, cpid, clabel in children:
                featured.add(cpid)
                centry = docs_entry(cpid)
                if centry:
                    lines.append(f'{indent}  - "{clabel}": {centry}')
            i = j
        else:
            if entry:
                lines.append(f'{indent}- "{label}": {entry}')
            i += 1

    study_semesters = sorted(
        pid
        for pid in pages
        if re.match(r"^study:(fall|spring)\d{4}$", pid) and pid not in featured
    )
    if study_semesters:
        lines.append('  - "Учеба (архив)":')
        for pid in study_semesters:
            entry = docs_entry(pid)
            if not entry:
                continue
            title = pid.split(":")[-1]
            try:
                t = extract_title(pages[pid].read_text(encoding="utf-8", errors="replace"))
                if t:
                    title = t
            except OSError:
                pass
            # escape quotes in title
            title = title.replace('"', "'")
            lines.append(f'    - "{title}": {entry}')
            featured.add(pid)

    for pid in sorted(pages):
        if pid in featured or pid == "index":
            continue
        if ":" in pid:
            continue
        entry = docs_entry(pid)
        if not entry:
            continue
        title = pid
        try:
            t = extract_title(pages[pid].read_text(encoding="utf-8", errors="replace"))
            if t:
                title = t.replace('"', "'")
        except OSError:
            pass
        lines.append(f'  - "{title}": {entry}')
        featured.add(pid)

    return "\n".join(lines) + "\n"


def write_mkdocs_yml(wiki_root: Path, nav_yaml: str) -> None:
    header = """site_name: StatMod Wiki
site_description: Wiki кафедры статистического моделирования
site_url: https://statmod.github.io/wiki/
repo_url: https://github.com/statmod/wiki
repo_name: statmod/wiki

# For a custom domain later (e.g. wiki.statmod.ru), change site_url only.
# Keep all documentation links relative so both base paths work.

theme:
  name: material
  language: ru
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy

plugins:
  - search:
      lang:
        - ru
        - en

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - tables
  - footnotes
  - attr_list
  - md_in_html
  - toc:
      permalink: true

extra:
  social: []

# Known missing media from the original DokuWiki dump (Cyrillic filenames, etc.)
validation:
  omitted_files: info
  absolute_links: info
  unrecognized_links: info

"""
    (wiki_root / "mkdocs.yml").write_text(header + nav_yaml, encoding="utf-8")


def copy_media(media_root: Path, assets_root: Path) -> int:
    if assets_root.exists():
        shutil.rmtree(assets_root)
    if not media_root.is_dir():
        return 0
    shutil.copytree(media_root, assets_root)
    return sum(1 for p in assets_root.rglob("*") if p.is_file())


def fix_broken_links(docs_root: Path, id_to_docs: Dict[str, Path]) -> int:
    fixed = 0
    id_set = set(id_to_docs)
    broken_re = re.compile(r"\[([^\]]*)\]\(BROKEN:([^)]+)\)")
    for md_file in docs_root.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        from_docs = md_file.relative_to(docs_root)

        def repl(m: re.Match) -> str:
            nonlocal fixed
            label, target = m.group(1), normalize_id(m.group(2))
            candidates = [target]
            if ":" in target:
                parts = target.split(":")
                for i in range(1, len(parts)):
                    candidates.append(":".join(parts[i:]))
                candidates.append(parts[-1])
            for c in candidates:
                if c in id_set:
                    href = relative_link(from_docs, id_to_docs[c])
                    fixed += 1
                    return f"[{label}]({href})"
            return m.group(0)

        new = broken_re.sub(repl, text)
        if new != text:
            md_file.write_text(new, encoding="utf-8")
    return fixed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "wikidata",
    )
    ap.add_argument(
        "--dest",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    ap.add_argument("--skip-media", action="store_true")
    args = ap.parse_args()

    pages_root = args.source / "pages"
    media_root = args.source / "media"
    docs_root = args.dest / "docs"

    if not pages_root.is_dir():
        log(f"pages not found: {pages_root}")
        return 1

    pages = discover_pages(pages_root)
    id_to_docs = build_id_to_docs(pages, pages_root)
    log(f"Discovered {len(pages)} pages")

    missing_media: List[Tuple[str, str]] = []
    pandoc_failures: List[str] = []

    # Remove old markdown only
    if docs_root.exists():
        for p in docs_root.rglob("*.md"):
            p.unlink()
    docs_root.mkdir(parents=True, exist_ok=True)

    n = 0
    for page_id, src in sorted(pages.items()):
        dest = docs_root / id_to_docs[page_id]
        raw = src.read_text(encoding="utf-8", errors="replace")
        title = extract_title(raw)
        store = PlaceholderStore()
        pre = preprocess(raw, page_id, pages, id_to_docs, media_root, missing_media, store)
        try:
            md = run_pandoc(pre)
        except subprocess.CalledProcessError as e:
            pandoc_failures.append(page_id)
            log(f"  pandoc fallback for {page_id}")
            md = fallback_convert(pre)
        md = finalize_md(md, title, store)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(md, encoding="utf-8")
        n += 1
        if n % 50 == 0:
            log(f"  converted {n}/{len(pages)}")

    log(f"Converted {n} pages → {docs_root}")
    if pandoc_failures:
        log(f"Pandoc fallbacks: {', '.join(pandoc_failures)}")

    fixed = fix_broken_links(docs_root, id_to_docs)
    log(f"Fixed {fixed} BROKEN links via fallback resolution")

    if not args.skip_media:
        if not (docs_root / "assets").exists():
            count = copy_media(media_root, docs_root / "assets")
            log(f"Copied {count} media files → docs/assets/")
        else:
            log("docs/assets already present — skipping media copy (use --force by deleting assets)")
    else:
        log("Skipped media copy")

    nav_items = parse_navigation(pages_root / "navigation.txt")
    nav_yaml = build_nav_yaml(nav_items, id_to_docs, pages)
    write_mkdocs_yml(args.dest, nav_yaml)
    log(f"Wrote {args.dest / 'mkdocs.yml'}")

    report = args.dest / "conversion-report.md"
    by_media: Dict[str, List[str]] = defaultdict(list)
    for pid, mid in missing_media:
        by_media[mid].append(pid)
    lines = [
        "# Conversion report",
        "",
        f"- Pages converted: {n}",
        f"- Pandoc fallbacks: {len(pandoc_failures)} ({', '.join(pandoc_failures) or 'none'})",
        f"- Unique missing media refs: {len(by_media)}",
        f"- BROKEN links fixed by fallback: {fixed}",
        "",
        "## Known irreducible issues",
        "",
        "- Legacy links to non-existent pages `doc` and `other` on the home page.",
        "- Media files referenced with Cyrillic filenames that are absent from the dump.",
        "- Occasional typos in media IDs (spaces inside the id).",
        "",
        "## Missing media",
        "",
    ]
    for mid in sorted(by_media):
        srcs = ", ".join(sorted(set(by_media[mid]))[:5])
        lines.append(f"- `{mid}` (from {srcs})")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"Wrote {report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
