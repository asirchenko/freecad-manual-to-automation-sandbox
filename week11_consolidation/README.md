# Week 11 — Junior Consolidation

**Deliverable:** PR «Junior cleanup» — polished README, evidence package, anti-patterns review.

## Checklist

- [x] Junior tests J1–J5 complete (`tests/junior/test_00` … `test_05`)
- [x] [docs/junior/JUNIOR_EVIDENCE.md](../docs/junior/JUNIOR_EVIDENCE.md) — evidence package
- [x] [docs/junior/ANTI_PATTERNS_REVIEW.md](../docs/junior/ANTI_PATTERNS_REVIEW.md) — self-review
- [x] [README.md](../README.md) — run instructions, strategy, doc links
- [ ] PR opened on GitHub (see below)

## Verify before PR

```powershell
venv\Scripts\activate
pytest tests/junior/ -v
pytest tests/junior/test_00_basics.py tests/junior/test_04_tolerance_check.py -v
```

## Open PR «Junior cleanup»

```powershell
git checkout -b feature/week11-junior-consolidation
git add .
git status
git commit -m "Week 11: Junior consolidation — README, evidence, anti-patterns review"
git push -u origin feature/week11-junior-consolidation
gh pr create --title "Week 11: Junior consolidation" --body-file docs/junior/PR_BODY_WEEK11.md
```

Use [PR_BODY_WEEK11.md](../docs/junior/PR_BODY_WEEK11.md) as the PR description template.

## Next week

**Week 12:** Junior Review & Sign-off — SME review on the Junior PR.

Progress: [docs/PROGRESS.md](../docs/PROGRESS.md)
