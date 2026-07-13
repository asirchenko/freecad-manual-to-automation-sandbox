# Week 12 — Junior SME Review

**Dates:** Sep 15 – 21, 2026 (program)  
**Goal:** SME sign-off on Junior track — no new test code required.

## Deliverables for SME

| Item | Path |
|------|------|
| Evidence package | `docs/junior/JUNIOR_EVIDENCE.md` |
| Anti-patterns review | `docs/junior/ANTI_PATTERNS_REVIEW.md` |
| Junior tests | `tests/junior/test_00` … `test_05` (23 tests) |

## Verify before requesting review

```powershell
venv\Scripts\activate
pytest tests/junior/ -v
```

Expected: **23 passed** (FreeCAD GUI required).

## SME message template

```
Hi Ievhenii,

Week 12 — Junior Review — ready for sign-off.

GitLab MR: [URL]
Junior suite: 23 tests (J1–J5 + basics)
Evidence: docs/junior/JUNIOR_EVIDENCE.md

Thanks,
Artem
```

## After SME feedback

- Apply review comments on GitLab MR
- Re-run `pytest tests/junior/ -v`
- Mark Junior track complete; proceed to Middle Week 13
