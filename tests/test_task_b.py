COLUMNS = ["user_id", "streak_days", "streak_start"]

# Known result from DIAGNOSTIC_TASKS.md.
KNOWN_RESULT = [
    (1, 3, "2026-11-01"),
    (2, 4, "2026-10-30"),
    (3, 2, "2026-11-10"),
    (4, 1, "2026-11-20"),
]

EXTRA_RESULT = [
    (5, 2, "2026-12-31"),
    (6, 1, "2027-03-01"),
    (7, 3, "2027-02-03"),
]


def _normalize(rows):
    return [(int(u), int(d), str(s)) for u, d, s in rows]


def test_known_result(logins_db, run_sql):
    cols, rows = run_sql(logins_db, "task_b.sql")
    assert [c.lower() for c in cols] == COLUMNS
    assert _normalize(rows) == KNOWN_RESULT


def test_extra_edge_cases(extra_logins_db, run_sql):
    cols, rows = run_sql(extra_logins_db, "task_b.sql")
    assert [c.lower() for c in cols] == COLUMNS
    assert _normalize(rows) == EXTRA_RESULT
