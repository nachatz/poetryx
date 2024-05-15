install:
	@poetry install --all-extras --with dev
	poetry lock
	poetry run mypy --install-types

build:
	@poetry build

fmt:
	@poetry run black src tests

mypy:
	@poetry run mypy src tests

check: fmt mypy
	@poetry run pylint --fail-under=10 src/poetryx 

validate: check
	coverage run --source=src -m pytest && \
	coverage report -m 

deploy: build
	@poetry run twine upload dist/*