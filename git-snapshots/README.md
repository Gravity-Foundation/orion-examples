# Git snapshots (Beta)

Export supported Orion definitions and selected tenant configuration to Git for version history and pull-request review.

- [orion-export.sh](orion-export.sh) creates a snapshot and commits changes in your Git checkout.
- [orion-export.yml](orion-export.yml) runs the script on a schedule using GitHub Actions and opens a pull request.

This export is **in beta** and runs one way, from Orion to Git. Merging or reverting a snapshot does not update Orion. Pull requests review changes that have already taken effect in Orion.

## Get started

Read the [setup guide, export coverage, and limitations](https://docs.runorion.com/version-control/sync-to-git) before running the examples.

1. Copy `orion-export.sh` into your destination repository as `scripts/orion-export.sh`.
2. If using GitHub Actions, copy `orion-export.yml` to `.github/workflows/orion-export.yml`. Set your tenant URL and repository secrets as described in the guide.
3. Commit the files before running. Use Bash, `curl`, `jq`, and `git` in a clean checkout. Reserve `orion-snapshots/` for generated output.
4. Supply `ORION_URL`, `ORION_USER`, and `ORION_PASSWORD` through your runner's environment and secret configuration. Optionally set `PROJECT_IDS` to limit project definitions and governance rules; other exports remain tenant-wide.
5. Run `bash scripts/orion-export.sh` and review the exported coverage before scheduling it.

The script requires an Orion Admin account with password authentication. Restrict access to the destination repository to people authorized to read the exports. Keep credentials and tenant exports out of this examples repository.

Generated artifacts and other content are excluded; see the guide for full coverage. The GitHub Actions configuration is provided as an example and does not run in this repository.
