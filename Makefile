# some common operations

clean_dist:
	rm -rf dist *.egg-info

clean_tests:
	rm -rf .pytest_cache .tox .coverage htmlcov test_report_36.xml
	py3clean .

clean_mypy:
	rm -rf .mypy_cache

clean_notebooks:
	rm -rf .ipynb_checkpoints

clean: clean_dist clean_mypy clean_tests clean_notebooks

test:
	poetry run pytest -n 4 -p no:cacheprovider

test_w_coverage:
	poetry run pytest -v -n 3 --junitxml=test_report.xml --cov-report html --cov=module tests/

package: clean_dist
	python setup.py sdist

mypy:
	poetry run mypy . --ignore-missing-imports

isort:
	poetry run isort .

format: isort
	poetry run black .

install_jupyter:
	pip install jupyterlab
