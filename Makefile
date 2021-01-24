install:
	python -m pipenv install --python 3.9 --dev

bootstrap_db:
	rm -f local_dev.db
	sqlite3 local_dev.db < migrations/01_gyro_sides_table.sql
	sqlite3 local_dev.db < migrations/02_gyro_logs_table.sql

start: bootstrap_db
	ENVIRONMENT=development python -m pipenv run python server_src/main.py

unit-test:
	PYTHONPATH=./server_src pipenv run pytest server_tests/unit

linting-test:
	pipenv run flake8
	@echo "Linting passed"
	pipenv run mypy server_src --config-file tox.ini


integration-test:
	PYTHONPATH=./server_src pipenv run pytest server_tests/integration

e2e-test:
	ENVIRONMENT=development pipenv run python server_src/main.py > /dev/null 2>&1 & echo "$$!" > server.pid

	PYTHONPATH=./server_src pipenv run pytest server_tests/e2e
	kill -15 $$(cat server.pid)
	rm server.pid

test: unit-test linting-test integration-test e2e-test
