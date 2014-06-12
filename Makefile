SOURCE_REPO = git://github.com/kennethreitz/kr-sphinx-themes.git
SOURCE_NAME = kr
MODULE_NAME = sphinx_kr_theme

update_subtree: setup_subtree
	git fetch $(SOURCE_NAME)
	git subtree pull --prefix=$(MODULE_NAME) $(SOURCE_NAME) master --squash
.PHONY: update_subtree

setup_subtree:
	@echo "> setup the remote repository..."
	git remote remove $(SOURCE_NAME)
	git remote add $(SOURCE_NAME) $(SOURCE_REPO)
.PHONY: setup_subtree
