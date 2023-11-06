PORT ?= 8000
start_json:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) webserver:app_json_file_DB run

start_debug_json:
	poetry run flask --app webserver:app_json_file_DB --debug run --port 8000

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) webserver:app

start_debug:
	poetry run flask --app webserver:app --debug run --port 8000

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 .

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build

