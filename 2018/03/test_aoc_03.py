import pytest

import aoc_03


@pytest.fixture
def claims():
    """
    The problem is that many of the claims overlap, causing two or more claims to
    cover part of the same areas. For example, consider the following claims:
    """
    return [
        aoc_03.Claim(id=1, x=1, y=3, width=4, height=4),
        aoc_03.Claim(id=2, x=3, y=1, width=4, height=4),
        aoc_03.Claim(id=3, x=5, y=5, width=2, height=2),
    ]


def test_calculate_overlapping_squares(claims):
    """
    Visually, these claim the following areas:

    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........

    The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
    while adjacent to the others, does not overlap either of them.)
    """

    (
        non_overlapping,
        number_of_overlapping_squares,
    ) = aoc_03.calculate_overlapping_squares(claims)
    assert non_overlapping == 3
    assert number_of_overlapping_squares == 4
