import pytest

import aoc_04


@pytest.mark.parametrize(
    "password, valid", [(111111, True), (223450, False), (123789, False)]
)
def test_is_valid_password_part_1(password, valid):
    """
    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).
    """
    assert aoc_04.is_valid_password(password) == valid


@pytest.mark.parametrize(
    "password, valid",
    [
        (112233, True),
        (123444, False),
        (111122, True),
        (122112, False),
        (122345, True),
        (112333, True),
        (111244, True),
        (168888, False),
    ],
)
def test_is_valid_password_part_2(password, valid):
    """
    112233 meets these criteria because the digits never decrease and all
        repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger
        group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it
        still contains a double 22).
    """
    assert aoc_04.is_valid_password_part_2(password) == valid
