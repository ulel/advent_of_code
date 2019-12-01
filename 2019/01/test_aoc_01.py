import pytest

import aoc_01

@pytest.mark.parametrize(
    "mass, expected_fuel", [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ]
)
def test_calculate_fuel(mass, expected_fuel):
    """
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    """
    assert aoc_01.calculate_fuel(mass) == expected_fuel

def test_calculate_total_fuel():
    assert aoc_01.calculate_total_fuel([12, 14, 1969, 100756]) == 2 + 2 + 654 + 33583
