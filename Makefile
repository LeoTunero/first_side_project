usage:
	@echo 'make [check|test|build|run|push]'

check:
	safety check
	bandit -r sharky
	pylint --django-settings-module=mysite.settings sharky/*
	python sharky/manage.py check

test: check
	python sharky/manage.py test sharky

build: test
	pipenv lock -r > requirements.txt
	# docker build -t sharky:latest .

run: build
	# docker run --rm -d -p 8000:8000 --name sharky sharky:latest


push: test
	git push
