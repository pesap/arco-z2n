# arco-z2n

arco implementation of zonal to nodal

## Development

```bash
uv sync --all-groups
just hooks-install
just verify
```

## Automated Forge Updates

This repository includes `.github/workflows/forge-update.yaml`, which runs weekly and opens a PR with Forge-managed infrastructure updates from `forge update --path .`. Forge reads the project configuration from `[tool.forge]` in `pyproject.toml` and does not use a separate status file.

Use these commands for local maintenance:

```bash
forge update --path . --dry-run
forge update --path . --check
forge update --path .
uv lock
```

Run `uv lock` when Forge reports it as a next step after changing managed options or other `pyproject.toml` metadata.

## Forge Metadata

This project was generated with `forge` blueprint `python-library`.
