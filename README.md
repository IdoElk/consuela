# Consuela

Inspect Python files with TypeSafe's Jev. Consuela reports clean-code judgments as typed probabilities and scores. It reads code and reports judgments; the calling person or agent decides what to change.

Python only for this MVP.

## Development

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv build
```
