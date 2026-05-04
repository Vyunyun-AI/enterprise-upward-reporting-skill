# Enterprise Upward Reporting Skill Package (v2)

This package upgrades the original user-provided skill content into a more production-ready agentic skill bundle.

## What's new in v2
- Clearer skill contract and routing logic
- English companion skill (`SKILL_EN.md`)
- JSON input/output schema (`schemas/io_schema.json`)
- Runnable helper script (`scripts/report_optimizer.py`)
- Expanded examples and evaluation cases
- Formal briefing document (`docs/Skill_Package_Briefing.docx`)

## Package layout
- `SKILL.md` — main Chinese skill definition
- `SKILL_EN.md` — English companion skill definition
- `resources/` — structure, rhetoric, output templates
- `schemas/` — machine-readable input/output schema
- `examples/` — sample input/output pairs
- `tests/` — evaluation prompts and acceptance criteria
- `scripts/` — helper script and usage notes
- `docs/` — formal project-style briefing document

## Notes
The helper script is intentionally conservative. It provides scaffolding and heuristics, but does not fabricate metrics or policy references.
