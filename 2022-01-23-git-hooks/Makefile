.PHONY: lint
lint:
	flake8 --max-line-length 80 ./src/

.PHONY: format
format:
	black ./src/

.PHONY: check-format
check-format:
	black --check ./src/

.PHONY: run
run:
	python src/main.py