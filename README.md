# python-template
[![GitHub license](https://img.shields.io/github/license/SamuelNLP/pyhon-template)](https://github.com/SamuelNLP/pyhon-template/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/SamuelNLP/pyhon-template/branch/master/graph/badge.svg?token=5CGG6XOCIW)](https://codecov.io/gh/SamuelNLP/pyhon-template)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9a6c9cdfe8c94c7584b84da80f97ccc8)](https://app.codacy.com/gh/SamuelNLP/pyhon-template?utm_source=github.com&utm_medium=referral&utm_content=SamuelNLP/pyhon-template&utm_campaign=Badge_Grade_Settings)

This is a skeleton repo to be used as a python template for future projects.

**PRO TIP**: Install Ubuntu or whatever Linux-based system you like!

We are using Python 3.14 and [uv](https://docs.astral.sh/uv/) as the Python dependency management tool. All the currently required dependencies are in the `pyproject.toml` file.

To set up the project:
- If you haven't already, install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Sync dependencies and create the environment with `uv sync --all-extras`
- Configure PyCharm to format docstrings with `numpy` style.

## Guidelines

To make things easier, we're also using Python's [ruff](https://github.com/astral-sh/ruff) tool to deal with code formatting, as the code linter, and to sort imports.

[mypy](http://mypy-lang.org/) is used for type hinting.

You can run `make mypy` for type checking, or `make ruff` to run the linter and format the code for you.

When developing code for this repository, please be sure you install the [pre-commit hooks](https://pre-commit.com/#install):

```bash
uv run pre-commit install
```

Afterwards, whenever you try to commit changes, the pre-commit hooks
will run and inform you of possible warnings/errors that must be fixed.

## Utilities

### Profiling with cProfile and snakeviz

```bash
# using cProfile
python -m cProfile -o foo.stats foo.py

sudo pip install snakeviz
snakeviz foo.pstats

# The visualization is opened in the browser in: http://127.0.0.1:8080
```

### Profiling with line_profiles

Decorate the functions to profile with `@profile`:
```python
@profile
def slow_function(a, b, c):
    ...
```

run the `kernprof` command on the script:
```bash
kernprof -l script_to_profile.py
python -m line_profiler script_to_profile.py.lprof
```
