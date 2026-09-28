# Consuela

Inspect Python files with TypeSafe's Jev. Consuela reports clean-code judgments as typed probabilities and scores. It reads code and reports judgments; the calling person or agent decides what to change.

Python only for this MVP.

## Install and run

```bash
cd ~/Projects/consuela
uv sync
cp .env.example .env
# Set TYPESAFE_API_KEY in .env.
uv run consuela --help
uv tool install .
```

Run from the repository being reviewed:

```bash
# One request per file; all results in one JSON document.
consuela package/module.py package/other.py

# A directory expands to every .py file inside it, recursively.
consuela src

# Inspect or save the exact requests without calling the API.
consuela package/module.py --dry-run --dump-request requests.json
```

Supply Python files (shell globs work) or directories. A directory expands to every `.py` file beneath it in sorted order, skipping hidden directories such as `.venv`; a directory with no Python files is an error. For one file, `--patch changes.diff` supplies a diff and enables the patch question. Automatic dependency discovery and patch filtering are outside this MVP.

Live commands send the selected evidence and questions to the configured TypeSafe API and consume API credits. `--dry-run` needs no credentials and makes no API calls. Local secrets load from `.env` in the **current working directory**, or `--env-file PATH`; existing environment variables take precedence. Requests/reports can contain source code: choose where to save them. `.env` and local `artifacts/` are ignored.

## Per-file checks

Each audit sends the complete target file in a separate request. It asks the applicable clean-code questions: 29 boolean criteria on ordinary source, plus test and patch criteria when applicable. Scores and the existing function Choice are descriptive; they do not determine acceptance.

[Jev's documented limits](https://docs.typesafe.ai/models) are 64k tokens for the full request and 32k for state plus the longest question. Consuela uses conservative byte guards: 240,000 serialized bytes for the full request and 120,000 for state plus any single question. These assume 4 bytes per token (Python source measures 4.5-4.8 bytes per token) and are **not token counts**; the service remains authoritative about token limits. Oversized requests fail before any API call; reduce the supplied scope explicitly. Consuela does not silently truncate code.

## Results

Standard output is JSON with `audits`, `errors`, and `passed`. A provider/response error stops the batch, identifies the failed request, and preserves completed audits; remaining requests are not executed. Each audit retains the complete typed answers, API usage, mode, source hashes, request hash, request byte count, skipped questions, and boolean acceptance details. Dry runs return `requests`, containing the exact state/question objects sent in live calls. `--dump-request` saves that same request batch before calling the API. The destination must not already exist, so dumping cannot overwrite source or secrets.

For every applicable Noul, yes means a smell. Acceptance requires `P(yes) <= 0.2`, equivalently `P(no smell) >= 0.8`. All requested answers must exist and have the expected type. Each boolean must pass; scores are not averaged. Coordinating the observe → choose → execute cycle counts as one responsibility under the preserved rubric clarification.

Exit 0 means every requested audit passed (or a preview succeeded); exit 1 means a failed audit or operational error; invalid CLI usage exits 2. Reports contain probabilities, not proof of correctness, source-localized findings, or generated explanations. Consumer enforcement policy is separate from inspection.

## Pre-commit

Install Consuela's own deterministic checks:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

They run Ruff (lint and format) and Complexipy with a per-function ceiling of 15. The hook manifest also exposes `consuela` for consumers who explicitly want paid file audits. For a local checkout, an opt-in consumer configuration is:

```yaml
repos:
  - repo: local
    hooks:
      - id: consuela
        name: Consuela file audit
        entry: consuela
        language: system
        types: [python]
        require_serial: true
```

Install the CLI first and supply the consumer's environment/`.env`. Pre-commit passes selected filenames; each gets a complete file audit.

## Development

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run complexipy src tests
uv build
```

Tests are offline. The implementation modules are `cli` (Click and invocation), `request` (evidence and budget), `questions` (rubric), and `report` (typed answers and acceptance). Self-review must check every implementation file independently; auditing a launcher alone does not certify the tool.

Current self-audit results are recorded in [the self-audit report](docs/self-audit.md). Deterministic checks pass; the Jev self-audit gate remains unmet.
