from diagnostics.task_a import sessionize


def test_spec_example():
    assert sessionize([100, 10, 20, 105, 400], gap=30) == [(10, 20), (100, 105), (400, 400)]


def test_empty_input():
    assert sessionize([], gap=30) == []


def test_single_event_is_one_session():
    assert sessionize([5], gap=10) == [(5, 5)]


def test_unsorted_input():
    assert sessionize([400, 105, 20, 10, 100], gap=30) == [(10, 20), (100, 105), (400, 400)]


def test_duplicates_stay_in_one_session():
    assert sessionize([10, 10, 10], gap=0) == [(10, 10)]


def test_unsorted_with_duplicates():
    assert sessionize([50, 0, 50, 10], gap=15) == [(0, 10), (50, 50)]


def test_gap_equal_to_threshold_does_not_split():
    assert sessionize([0, 30, 60], gap=30) == [(0, 60)]


def test_gap_one_more_than_threshold_splits():
    assert sessionize([0, 31], gap=30) == [(0, 0), (31, 31)]


def test_gap_zero_splits_every_distinct_time():
    assert sessionize([3, 1, 2], gap=0) == [(1, 1), (2, 2), (3, 3)]


def test_everything_in_one_session():
    assert sessionize([1, 5, 9, 2], gap=100) == [(1, 9)]


def test_returns_tuples():
    result = sessionize([1, 2], gap=5)
    assert all(isinstance(s, tuple) for s in result)
