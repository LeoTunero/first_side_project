usage:
	@echo 'make [check|test|push]'

check:
	safety check
	bandit -r sharky
	pylint --django-settings-module=mysite.settings sharky/*
	python sharky/manage.py check

test: check
	python sharky/manage.py test sharky

build:
	pipenv lock -r > requirements.txt

push: test
	git push
