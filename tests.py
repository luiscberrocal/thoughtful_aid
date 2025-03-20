import pytest

from main import DispatchType, sort


@pytest.mark.parametrize(
    "width, height, length, mass, expected",
    [
        (10, 10, 10, 1, DispatchType.STANDARD),
        (200, 10, 10, 1, DispatchType.SPECIAL),
        (10, 10, 10, 25, DispatchType.SPECIAL),
        (200, 10, 10, 25, DispatchType.REJECTED),
        (150, 150, 150, 19, DispatchType.SPECIAL),
        (10, 10, 10, 20, DispatchType.SPECIAL),
        (150, 150, 150, 20, DispatchType.REJECTED),
    ],
)
def test_sort(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected

@pytest.mark.parametrize(
    "width, height, length, mass, expected_exception",
    [
        (10, 10, 10, 1, None),
        (200, 10, 10, 1, None),
        (10, 10, 10, 25, None),
        (200, 10, 10, 25, None),
        (150, 150, 150, 19, None),
        (10, 10, 10, 20, None),
        (150, 150, 150, 20, None),
        (-10, 10, 10, 1, ValueError),
        (10, -10, 10, 1, ValueError),
        (10, 10, -10, 1, ValueError),
        (None, 10, 10, 1, ValueError),
        (10, None, 10, 1, ValueError),
        (10, 10, None, 1, ValueError),
    ],
)
def test_sort(width, height, length, mass, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            sort(width, height, length, mass)
    else:
        assert sort(width, height, length, mass) is not None
