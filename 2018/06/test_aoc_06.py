import pytest

import aoc_06

LOCATIONS_IN_EXAMPLE = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


@pytest.mark.parametrize(
    "cord1, cord2, expected",
    [
        ((2, 3), (2, 3), 0),
        ((1, 1), (3, 3), 4),
        ((1, 1), (1, 6), 5),
        ((-1, -2), (1, 2), 6),
    ],
)
def test_manhattan_distance(cord1, cord2, expected):
    assert aoc_06.manhattan_distance(cord1, cord2) == expected


def test_max_x_and_y():
    assert aoc_06.max_x_and_y(LOCATIONS_IN_EXAMPLE) == (8, 9)


def test_size_of_largest_area():
    assert aoc_06.size_of_largest_area(LOCATIONS_IN_EXAMPLE, max_range=32) == (17, 16)
