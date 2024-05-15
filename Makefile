install:
	@poetry install --all-extras --with dev
	poetry lock

build:
	@poetry build

fmt:
	black src tests

mypy:
	mypy src tests

check: fmt mypy
	pylint  --fail-under=10 src/poetryx 

validate: check
	coverage run --source=src -m pytest && \
	coverage report -m 
