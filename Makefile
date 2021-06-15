SITE_DEST_DIR=dist

start: start-site

build: build-site

build-site:
	mkdocs build -d $(SITE_DEST_DIR)

start-site:
	mkdocs serve -a 0.0.0.0:8000

clean: clean-site

clean-site:
	rm -rf $(SITE_DEST_DIR)