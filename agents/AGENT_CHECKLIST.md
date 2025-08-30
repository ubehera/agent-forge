# Agent Addition/Update Checklist

Use this checklist before opening a PR for any agent in `agents/`.

## File & Location
- [ ] File lives in `agents/`
- [ ] Filename is `kebab-case.md` (e.g., `api-platform-engineer.md`)

## YAML Frontmatter
- [ ] Present at top with `---` fences
- [ ] Includes `name` (kebab-case, unique)
- [ ] Includes concise, specific `description` (drives routing)
- [ ] Optional `tools` declared and minimal (only what’s needed)

## Content Quality
- [ ] Short, actionable guidance; avoids generic filler
- [ ] Practical examples or commands where helpful
- [ ] No secrets or sensitive data

## Validation
- [ ] Install locally for current user or project:
  ```bash
  cp agents/*.md ~/.claude/agents/ \
  || (mkdir -p .claude/agents && cp agents/*.md .claude/agents/)
  ```
- [ ] Restart Claude Code to load changes
- [ ] Test prompts that should trigger the agent and confirm selection
- [ ] Verify tool restrictions behave as intended

## Documentation
- [ ] Update `agents/README.md` (matrix/triggers) if adding/renaming
- [ ] Update `CLAUDE.md` if standards or workflows change
- [ ] Confirm `AGENTS.md` remains accurate

## Configuration & Security
- [ ] Review `.mcp.json` if adding servers; no credentials committed
- [ ] Prefer minimal `tools` to reduce permissions and improve performance
