#!/usr/bin/env python3
"""Verify internal Markdown links and media references under docs/."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Set, Tuple
from urllib.parse import unquote, urlparse

LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_SRC_RE = re.compile(
    r"""(?i)<(?:img|a|source|iframe)\b[^>]*?\b(?:src|href)=["']([^"']+)["']"""
)


def normalize_url(url: str) -> str:
    url = url.strip()
    # Pandoc autolink form: <http://...>
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1]
    return url.strip()


def is_external(url: str) -> bool:
    url = normalize_url(url)
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return True
    if url.startswith("BROKEN:"):
        return False
    parsed = urlparse(url)
    return bool(parsed.scheme) or url.startswith("//")


def resolve(from_file: Path, url: str) -> Path:
    url = normalize_url(url)
    url = unquote(url.split("#")[0].split("?")[0]).strip()
    if not url:
        return from_file
    return (from_file.parent / url).resolve()


def check_docs(docs_root: Path) -> Tuple[List[str], List[str]]:
    broken: List[str] = []
    broken_media: List[str] = []
    docs_root = docs_root.resolve()

    for md in docs_root.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        urls = []
        for m in LINK_RE.finditer(text):
            urls.append(m.group(2))
        for m in IMG_RE.finditer(text):
            urls.append(m.group(2))
        for m in HTML_SRC_RE.finditer(text):
            urls.append(m.group(1))

        for url in urls:
            raw = url
            url = normalize_url(url)
            if "BROKEN:" in url:
                broken.append(f"{md.relative_to(docs_root)}: unresolved {url}")
                continue
            if is_external(url):
                continue
            target = resolve(md, url)
            try:
                target.relative_to(docs_root)
            except ValueError:
                broken.append(f"{md.relative_to(docs_root)}: outside docs: {raw}")
                continue

            candidates = [target]
            if target.suffix == "":
                candidates.extend([Path(str(target) + ".md"), target / "index.md"])
            found = next((c for c in candidates if c.is_file()), None)
            if found:
                continue

            msg = f"{md.relative_to(docs_root)}: missing {raw}"
            asset_like = "/assets/" in raw.replace("\\", "/") or target.suffix.lower() in {
                ".pdf",
                ".zip",
                ".png",
                ".jpg",
                ".jpeg",
                ".gif",
                ".txt",
                ".gz",
                ".doc",
                ".docx",
                ".rtf",
                ".xls",
                ".tex",
                ".djvu",
                ".rar",
                ".csv",
                ".r",
                ".py",
            }
            if asset_like:
                broken_media.append(msg)
            else:
                broken.append(msg)

    return broken, broken_media


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--docs",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "docs",
    )
    ap.add_argument(
        "--allow-missing-media",
        action="store_true",
        help="Exit 0 even if media files are missing (legacy dump gaps)",
    )
    ap.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Append summary to this markdown report",
    )
    args = ap.parse_args()
    docs = args.docs
    if not docs.is_dir():
        print(f"docs not found: {docs}", file=sys.stderr)
        return 1

    broken, broken_media = check_docs(docs)
    print(f"Broken page links: {len(broken)}")
    for b in broken[:40]:
        print(f"  {b}")
    if len(broken) > 40:
        print(f"  ... and {len(broken) - 40} more")

    print(f"Missing media refs: {len(broken_media)}")
    for b in broken_media[:40]:
        print(f"  {b}")
    if len(broken_media) > 40:
        print(f"  ... and {len(broken_media) - 40} more")

    if args.report:
        with args.report.open("a", encoding="utf-8") as f:
            f.write("\n## Link verification\n\n")
            f.write(f"- Broken page links: {len(broken)}\n")
            f.write(f"- Missing media refs: {len(broken_media)}\n")
            if broken:
                f.write("\n### Broken page links\n\n")
                for b in broken:
                    f.write(f"- `{b}`\n")
            if broken_media:
                f.write("\n### Missing media (legacy / absent from dump)\n\n")
                for b in broken_media:
                    f.write(f"- `{b}`\n")

    if broken:
        return 1
    if broken_media and not args.allow_missing_media:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
