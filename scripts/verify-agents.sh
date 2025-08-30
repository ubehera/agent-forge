#!/bin/bash
set -e

AGENTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/../agents && pwd)"

pass=0; warn=0; fail=0

echo "Verifying agents in: $AGENTS_DIR"

for file in "$AGENTS_DIR"/*.md; do
  [[ -f "$file" ]] || continue
  base=$(basename "$file")
  case "$base" in
    README.md|TESTING.md|AGENT_CHECKLIST.md)
      continue
      ;;
  esac

  name=$(sed -n '1,20p' "$file" | awk -F: '/^name:/ {gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2; exit}')
  desc_ok=$(sed -n '1,40p' "$file" | grep -q '^description:' && echo ok || echo no)
  tools=$(sed -n '1,40p' "$file" | awk -F: '/^tools:/ {sub(/^ /, "", $2); print $2; exit}')

  errs=()
  [[ $(head -n1 "$file") == "---" ]] || errs+=("missing frontmatter start ---")
  [[ -n "$name" ]] || errs+=("missing name")
  [[ "$desc_ok" == ok ]] || errs+=("missing description")

  # name should match filename (without .md)
  expected="${base%.md}"
  if [[ -n "$name" && "$name" != "$expected" ]]; then
    errs+=("name '$name' != filename '$expected'")
  fi

  # warn if both WebSearch and WebFetch are in tools
  if echo "$tools" | grep -q "WebSearch" && echo "$tools" | grep -q "WebFetch"; then
    echo "[WARN] $base: tools include both WebSearch and WebFetch"
    ((warn++))
  fi

  if ((${#errs[@]})); then
    echo "[FAIL] $base: ${errs[*]}"
    ((fail++))
  else
    echo "[OK]   $base"
    ((pass++))
  fi
done

echo "\nSummary: $pass ok, $warn warnings, $fail failures"
exit $fail

