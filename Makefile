install:
	python -m pipenv install --python 3.9 --dev

start:
	rm -f local_dev.db
	sqlite3 local_dev.db < migrations/01_create_tables.sql
	PIPENV_DOTENV_LOCATION=bootstrap.env python -m pipenv run python server_src/main.py

unit-test:
	PYTHONPATH=./server_src pipenv run pytest server_tests/unit

linting-test:
	pipenv run flake8
	@echo "Linting passed"
	pipenv run mypy server_src --config-file tox.ini


integration-test:
	pipenv run pytest tests/integration

e2e-test:
	docker-compose build
	docker-compose up -d
	sleep 10
	PYTHONPATH=./src pipenv run pytest tests/e2e
