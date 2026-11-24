from diagnostics.task_a1 import neighbor_gaps


def test_spec_example():
    assert neighbor_gaps([10, 20, 100, 105, 400]) == [10, 80, 5, 295]


def test_empty_input():
    assert neighbor_gaps([]) == []


def test_single_element_has_no_gaps():
    assert neighbor_gaps([5]) == []


def test_two_elements():
    assert neighbor_gaps([3, 10]) == [7]


def test_duplicates_give_zero():
    assert neighbor_gaps([3, 3, 7]) == [0, 4]


def test_length_is_one_less():
    ts = [1, 2, 4, 8, 16, 32]
    assert len(neighbor_gaps(ts)) == len(ts) - 1
