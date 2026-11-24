from diagnostics.task_a2 import count_sessions


def test_spec_example():
    assert count_sessions([10, 20, 100, 105, 400], gap=30) == 3


def test_empty_input_has_no_sessions():
    assert count_sessions([], gap=30) == 0


def test_single_event_is_one_session():
    assert count_sessions([5], gap=10) == 1


def test_gap_equal_to_threshold_does_not_split():
    assert count_sessions([0, 30, 60], gap=30) == 1


def test_gap_one_more_than_threshold_splits():
    assert count_sessions([0, 31], gap=30) == 2


def test_duplicates_stay_in_one_session():
    assert count_sessions([5, 5, 5], gap=0) == 1


def test_gap_zero_splits_every_distinct_time():
    assert count_sessions([1, 2, 2, 3], gap=0) == 3
