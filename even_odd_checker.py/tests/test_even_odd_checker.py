import pytest

from even_odd_checker import is_even


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(n, expected):
    assert is_even(n) is expected
