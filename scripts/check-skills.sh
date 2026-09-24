#!/usr/bin/env bash
# Validate every skill under skills/: frontmatter is present, the name matches
# its directory, and the downloadable ZIP matches the source exactly.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)/skills"

fail=0
err() { echo "::error file=skills/$1::$2" >&2; fail=1; }

for skill in */SKILL.md; do
  dir=${skill%/SKILL.md}
  before=$fail
  [ "$(head -n 1 "$skill")" = "---" ] || { err "$skill" "Missing YAML frontmatter"; continue; }
  front=$(awk 'NR > 1 && /^---$/ { exit } NR > 1' "$skill")
  name=$(sed -n 's/^name: *//p' <<<"$front")
  desc=$(sed -n 's/^description: *//p' <<<"$front")
  [ "$name" = "$dir" ] || err "$skill" "name '$name' does not match directory '$dir'"
  [ -n "$desc" ] || err "$skill" "Missing description"
  [ "${#desc}" -le 1024 ] || err "$skill" "Description exceeds 1024 characters"

  zip="$dir-skill.zip"
  if [ ! -f "$zip" ]; then
    err "$skill" "Missing $zip; build it with: (cd skills && zip -r $zip $dir)"
    continue
  fi
  expected=$(find "$dir" -type f | sort)
  actual=$(unzip -Z1 "$zip" | grep -v '/$' | sort)
  [ "$expected" = "$actual" ] || err "$zip" "ZIP contents differ from $dir/"
  for f in $expected; do
    unzip -p "$zip" "$f" | cmp -s - "$f" || err "$zip" "$f is stale in the ZIP"
  done
  [ "$fail" != "$before" ] || echo "ok  $dir"
done

exit "$fail"
