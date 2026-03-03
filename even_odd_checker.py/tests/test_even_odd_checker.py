import pytest

from even_odd_checker import is_even, analyze_range


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(n, expected):
    assert is_even(n) is expected


def test_analyze_range():
    # simple forward range
    summary = analyze_range(1, 4)  # 1,2,3,4 -> two evens, two odds
    assert summary == {"even": 2, "odd": 2}

    # backwards range should still work
    summary = analyze_range(4, 1)
    assert summary == {"even": 2, "odd": 2}

    # single number range
    assert analyze_range(5, 5) == {"even": 0, "odd": 1}

    # include negative numbers
    assert analyze_range(-2, 2) == {"even": 3, "odd": 2}
