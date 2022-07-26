# A Self-Documenting Makefile: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

SHELL = /bin/bash
OS = $(shell uname | tr A-Z a-z)

.PHONY: test
test: ## Run tests
	poetry run pytest --cov-report term:skip-covered --cov-report term-missing --cov=patterns tests/


.PHONY: clean
clean: ## Cleans project folder mainly cache
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -f coverage.xml
	rm -rf build
	find tests patterns -empty -type d -delete

.PHONY: new-pattern
new-pattern: ## Creates folder to implement new pattern
	poetry run python scripts/gen_new_pattern.py

.PHONY: lint
lint: ## Checks code linting
	poetry run black --check . --line-length 79
	poetry run isort --check-only . --line-length 79
	poetry run flake8 .
	make lint-types

.PHONY: format
format: ## Formats code
	poetry run black . --line-length 79
	poetry run isort . --profile black --line-length 79
	poetry run flake8 .

.PHONY: lint-types
lint-types: ## Lint project types
	poetry run mypy . 


.PHONY: help
.DEFAULT_GOAL := help
help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
