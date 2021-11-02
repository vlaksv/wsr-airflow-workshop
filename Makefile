.PHONY: deploy-dag help
.DEFAULT_GOAL := help

export PYTHONPATH := src

help: ## Show this help
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[34m%-20s\033[0m %s\n", $$1, $$2}'

black: ## run formatter with black
	black --line-length 100 dags

lint: ## check style with black and flake8
	black --line-length 100  --check dags
	flake8 --max-line-length 100 dags

requirements: ## install requirements
	pip install -r requirements.txt

test: # run test
	python dags/diversity_in_tech_example.py

tests: ## run tests
	for file_name in dags/*.py; do \
		python $${file_name};\
	done
