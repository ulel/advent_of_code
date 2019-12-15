import pytest

import aoc_04


@pytest.mark.parametrize(
    "password, valid", [(111111, True), (223450, False), (123789, False)]
)
def test_is_valid_password(password, valid):
    """
    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).
    """
    assert aoc_04.is_valid_password(password) == valid
