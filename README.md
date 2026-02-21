# langlearn-types

Shared interfaces and data models for LangLearn tooling.

## Status (2026-02-21)
- Core request/result models for image, audio, and deck workflows are implemented.
- Provider protocols for image, audio, and deck backends are implemented.
- EvaluationResult and PromptBundle contracts are available for orchestrator use.

## Roadmap
See ROADMAP.md.

## Install

```bash
uv tool install punt-langlearn-types
```

## CLI

```bash
langlearn-types --help
langlearn-types --json version
langlearn-types doctor
langlearn-types serve
```

## MCP

```bash
langlearn-types install
langlearn-types serve
```

## Development

```bash
uv sync --all-extras
uv run ruff check .
uv run ruff format --check .
uv run mypy src/ tests/
uv run pyright src/ tests/
uv run pytest
```
