# langlearn-types

Shared interfaces and data models for LangLearn tooling.

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
