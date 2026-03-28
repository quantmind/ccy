---
name: ccy-instructions
description: 'Instructions for ccy'
applyTo: '/**'
---


# Ccy Instructions


## Development

* Always run `make lint` after code changes — runs taplo, isort, black, ruff, and mypy
* Never edit `readme.md` directly — it is generated from `docs/index.md` via `make docs`
* To run all tests use `make test` — runs all tests in the `tests/` directory using pytest
* To run a specific test file, use `uv run pytest tests/path/to/test_file.py`


## Documentation

* The documentation for ccy is available at `https://ccy.quantmid.com`
* Documentation is built using [mkdocs](https://www.mkdocs.org/) and stored in the `docs/` directory. The documentation source files are written in markdown format.
* Do not use em dashes (—) in documentation files or docstrings. Use colons, parentheses, or restructure the sentence instead.
* To link to a class or function in documentation, use the mkdocstrings cross-reference notation: `[ClassName][module.path.ClassName]` (e.g. `[TradingCentre][ccy.tradingcentres.TradingCentre]`)
