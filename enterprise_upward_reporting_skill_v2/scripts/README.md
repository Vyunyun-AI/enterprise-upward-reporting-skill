# Script Notes

`report_optimizer.py` is a lightweight helper for packaging rough Chinese drafts into a more formal SOE reporting skeleton.

## Usage
```bash
python report_optimizer.py --input draft.txt --mode auto
python report_optimizer.py --input draft.txt --mode rectification --output result.txt
```

## Modes
- `auto`
- `status`
- `rectification`
- `inspection`

## Important
This script is a heuristic formatter. It must not be used to fabricate facts, KPIs, names, policy references, or dates.
