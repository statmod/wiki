.PHONY: convert convert-pages verify build serve

SOURCE ?= ../wikidata

convert:
	python3 scripts/convert_dokuwiki.py --source $(SOURCE) --dest .

convert-pages:
	python3 scripts/convert_dokuwiki.py --source $(SOURCE) --dest . --skip-media

verify:
	python3 scripts/verify_links.py --docs docs --allow-missing-media --report conversion-report.md

build:
	mkdocs build

serve:
	mkdocs serve
