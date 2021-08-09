usage:
	@echo 'make [check|push]'

check:
	python sharky/manage.py check

push: check
	git push
