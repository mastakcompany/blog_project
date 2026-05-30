MANAGE = uv run manage.py

.PHONY: run lint makemigrations migrate createsuperuser

run:
	$(MANAGE) runserver

lint:
	uv run pre-commit run --all-files

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser
