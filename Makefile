usage:
	@echo 'make [check|push]'

check:
	safety check
	bandit -r sharky
	pylint --django-settings-module=mysite.settings sharky/*
	python sharky/manage.py check

test: check
	python sharky/manage.py test sharky

push: test
	git push
