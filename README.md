# StatMod Wiki

MkDocs Material site converted from the DokuWiki dump formerly at `statmod.ru/wiki`.

**Live URL:** https://statmod.github.io/wiki/

For a custom domain later (e.g. `wiki.statmod.ru`), change only `site_url` in `mkdocs.yml` and configure GitHub Pages DNS/CNAME. All in-page links are relative.

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

## Re-convert from DokuWiki dump

```bash
# Full convert (pages + media copy)
python3 scripts/convert_dokuwiki.py --source ../wikidata --dest .

# Pages only (keep existing docs/assets)
python3 scripts/convert_dokuwiki.py --source ../wikidata --dest . --skip-media

# Verify internal links (page links must be clean; media gaps allowed)
python3 scripts/verify_links.py --docs docs --allow-missing-media
```

## Layout

- `docs/` — converted Markdown + `assets/` (media files)
- `scripts/convert_dokuwiki.py` — conversion pipeline
- `scripts/verify_links.py` — link checker
- `conversion-report.md` — missing media and conversion notes
- `.github/workflows/deploy.yml` — GitHub Pages deploy

Excluded from conversion: stock DokuWiki `wiki/` and `playground/` namespaces, plus page history (`attic/`).
