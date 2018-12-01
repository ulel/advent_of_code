import pytest

import aoc_01


@pytest.mark.parametrize(
    "changes, expected_frequency", [([1, 1, 1], 3), ([1, 1, -2], 0), ([-1, -2, -3], -6)]
)
def test_frequence_adjustments(changes, expected_frequency):
    assert aoc_01.calibrate(changes) == expected_frequency


def running_input(changes):
    while True:
        for change in changes:
            yield change


@pytest.mark.parametrize(
    "changes, expected_frequency",
    [
        ([+1, -1], 0),
        ([+3, +3, +4, -2, -4], 10),
        ([-6, +3, +8, +5, -6], 5),
        ([+7, +7, -2, -7, -4], 14),
    ],
)
def test_find_first_repeating_frequency(changes, expected_frequency):
    assert aoc_01.find_first_duplicate(running_input(changes)) == expected_frequency
