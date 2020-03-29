# some common operations

clean_dist:
	rm -rf dist *.egg-info

clean_tests:
	rm -rf .pytest_cache .tox
	py3clean .

clean_mypy:
	rm -rf .mypy_cache

clean: clean_dist clean_mypy clean_tests

test:
	tox

package: clean_dist
	python setup.py sdist

vulture:
	vulture module/

isort:
	isort -rc .

unused_imports:
	importchecker .

format: isort unused_imports
	black .

export_reqs:
	pip-chill --no-version > requirements.txt

install_reqs:
	pip install -r requirements.txt
