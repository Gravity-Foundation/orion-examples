# Contributing to Orion examples

Customers copy these files straight into their own repos and assistants. Treat every example as production code someone will run against a live Orion tenant.

## Adding an example

1. Give it a top-level folder with a short, lowercase, hyphenated name, such as `git-snapshots/`.
2. Add a `README.md` in that folder: what it does, what it needs, and the exact steps to get started. Link to [docs.runorion.com](https://docs.runorion.com) for product behavior instead of restating it.
3. Add a row to the catalog table in the root [README](README.md).
4. Mark it `beta` in the catalog if its behavior or coverage may still change.

## Adding or changing a skill

- Skills live in `skills/<name>/SKILL.md`. The frontmatter `name` must match the folder.
- Rebuild the upload bundle whenever the skill changes, or CI fails:

  ```bash
  cd skills && rm -f orion-guide-skill.zip && zip -r orion-guide-skill.zip orion-guide -x '*.DS_Store'
  ```

- Bump the `Version:` date in the skill body.

## Safe to copy

- No credentials, tenant URLs, customer names, or customer data. Use placeholders like `https://your-tenant.runorion.com`.
- Read secrets from environment variables and document which ones are required.
- Scripts start with `set -euo pipefail` and fail loudly instead of writing partial output.
- Example GitHub workflows request the narrowest `permissions` they need.

## Checks

CI runs ShellCheck, actionlint, the skill validator, and a link checker on every pull request. The root [README](README.md#quality-bar) lists the commands to run them locally.

## Style

Direct and plain. Say what the example does and what the reader should do next. No emoji.
