# Consuela

Inspect Python files with TypeSafe's Jev. Consuela reports clean-code judgments as typed probabilities and scores. It reads code and reports judgments; the calling person or agent decides what to change.

Python only for this MVP.

## Pre-commit

Install Consuela's own deterministic checks:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

They run Ruff (lint and format) and Complexipy with a per-function ceiling of 15.

## Development

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run complexipy src tests
uv build
```
