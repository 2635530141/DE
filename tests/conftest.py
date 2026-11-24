from pathlib import Path

import duckdb
import pytest

ROOT = Path(__file__).resolve().parent.parent

# Task B data, copied word for word from DIAGNOSTIC_TASKS.md.
SPEC_LOGINS = """
CREATE TABLE logins (user_id INTEGER, login_date DATE);
INSERT INTO logins VALUES
  (1, '2026-11-01'), (1, '2026-11-02'), (1, '2026-11-02'), (1, '2026-11-03'), (1, '2026-11-06'),
  (2, '2026-10-30'), (2, '2026-10-31'), (2, '2026-11-01'), (2, '2026-11-02'), (2, '2026-11-07'),
  (3, '2026-11-10'), (3, '2026-11-11'), (3, '2026-11-14'), (3, '2026-11-15'),
  (4, '2026-11-20');
"""

# Extra edge cases, not in the spec: a streak across a year boundary, a tie
# (earlier streak wins), and a user whose only day is logged twice.
EXTRA_LOGINS = """
CREATE TABLE logins (user_id INTEGER, login_date DATE);
INSERT INTO logins VALUES
  (5, '2026-12-31'), (5, '2027-01-01'), (5, '2027-01-05'), (5, '2027-01-06'),
  (6, '2027-03-01'), (6, '2027-03-01'),
  (7, '2027-02-01'), (7, '2027-02-03'), (7, '2027-02-04'), (7, '2027-02-05');
"""


def _db(ddl):
    con = duckdb.connect(":memory:")
    con.execute(ddl)
    return con


@pytest.fixture
def logins_db():
    con = _db(SPEC_LOGINS)
    yield con
    con.close()


@pytest.fixture
def extra_logins_db():
    con = _db(EXTRA_LOGINS)
    yield con
    con.close()


@pytest.fixture
def run_sql():
    """Run a .sql file from diagnostics/ and return (column names, rows)."""

    def _run(con, filename):
        sql = (ROOT / "diagnostics" / filename).read_text()
        body = "\n".join(l for l in sql.splitlines() if not l.strip().startswith("--")).strip()
        if not body:
            pytest.fail(f"diagnostics/{filename} has no query yet")
        cur = con.execute(sql)
        cols = [d[0] for d in cur.description]
        return cols, cur.fetchall()

    return _run
