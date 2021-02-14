install:
	python -m pipenv install --python 3.7.3 --dev

deploy-server:
	PIPENV_VENV_IN_PROJECT=1 python3 -m pipenv install --system --deploy
	sudo cp server/deployment/gyro_server.service /etc/systemd/system/gyro_server.service
	sudo systemctl enable gyro_server
	sudo systemctl daemon-reload
	sudo systemctl restart gyro_server

bootstrap_db:
	rm -f local_dev.db
	sqlite3 local_dev.db < migrations/01_gyro_sides_table.sql
	sqlite3 local_dev.db < migrations/02_gyro_logs_table.sql

server-start: bootstrap_db
	ENVIRONMENT=development pipenv run python server/src/main.py

server-unit-test:
	PYTHONPATH=./server/src pipenv run pytest server/tests/unit

server-linting-test:
	pipenv run flake8
	@echo "Linting passed"
	pipenv run mypy server/src --config-file tox.ini


server-integration-test:
	PYTHONPATH=./server/src pipenv run pytest server/tests/integration

server-e2e-test:
	ENVIRONMENT=development pipenv run python server/src/main.py > /dev/null 2>&1 & echo "$$!" > server.pid

	PYTHONPATH=./server/src pipenv run pytest server/tests/e2e
	kill -15 $$(cat server.pid)
	rm server.pid

server-test: server-unit-test server-linting-test server-integration-test server-e2e-test

client:
	rm client/gyro_client/*
	for file in client/src/*; \
		do envsubst < "client/src/$$(basename $$file)" > "client/gyro_client/$$(basename $$file)"; \
	done
