PHONY: all
all: venv test ## Default target, runs both venv and test.

venv: ## Setup python virtualenv and install testing requirements.
	@echo "Setting up virtualenv to run tests..."
	python3 -m venv ./venv
	./venv/bin/pip install -r requirements-dev.txt
	@echo "Setup complete!"

.PHONY: test
test: ## Run repo tests.
	./venv/bin/pytest -vvv

.PHONY: help
help: ## Prints help for targets with comments
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
