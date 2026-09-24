# Orion examples

Examples for working with [Orion](https://docs.runorion.com).

## Git snapshots (Beta)

The [snapshot export script](git-snapshots/orion-export.sh) exports supported Orion definitions and selected tenant configuration into a Git checkout. The [GitHub Actions example](git-snapshots/orion-export.yml) schedules exports and opens a pull request.

Follow the [setup instructions, coverage, and limitations](https://docs.runorion.com/version-control/sync-to-git) before running either example.

1. Copy `git-snapshots/orion-export.sh` into your destination repository as `scripts/orion-export.sh`.
2. If using GitHub Actions, copy `git-snapshots/orion-export.yml` to `.github/workflows/orion-export.yml` and configure the tenant URL and repository secrets as described in the docs.
3. Commit the files before running. Use Bash, curl, jq, and git in a clean checkout. Reserve `orion-snapshots/` for generated output.
4. Supply `ORION_URL`, `ORION_USER`, and `ORION_PASSWORD` through your runner's secret/environment configuration. Optionally set `PROJECT_IDS` to limit project definitions and governance rules; other exports remain tenant-wide.
5. Run `bash scripts/orion-export.sh` and review the exported coverage before scheduling it.

The script needs an Orion Admin account with password authentication. Use a separate repository with access appropriate for the exported tenant information. Never commit credentials or customer exports to this examples repository.

This workflow is **in beta** and exports one way, from Orion to Git. Merging or reverting a snapshot does not update Orion or approve changes before they take effect there. Generated artifacts and several other surfaces are excluded; see the documentation for details.

The workflow YAML is an example file, not an active workflow in this repository.

## Maintaining the docs embed

This repository is the source of truth. The docs embed public Gist mirrors for the [shell script](https://gist.github.com/noahgcook/6a55a32a090a133c10b4aad1ff98a0d1) and [workflow](https://gist.github.com/noahgcook/370eb8fd810f48de98f8843bcc01de00), owned by `noahgcook` and pinned to reviewed revisions. Updating this repository alone does not change either embed.

After reviewing a change, a maintainer with access can update the corresponding Gist:

```bash
gh gist edit 6a55a32a090a133c10b4aad1ff98a0d1 --filename orion-export.sh git-snapshots/orion-export.sh
gh gist edit 370eb8fd810f48de98f8843bcc01de00 --filename orion-export.yml git-snapshots/orion-export.yml
```

Then update the Gist revision and matching repository commit links in `orion-docs/version-control/sync-to-git.mdx` together and verify the rendered preview. Keep credentials and tenant snapshots out of both the Gist and this repository.
