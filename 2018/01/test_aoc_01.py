import pytest

import aoc_01


@pytest.mark.parametrize(
    "changes, expected_frequency", [([1, 1, 1], 3), ([1, 1, -2], 0), ([-1, -2, -3], -6)]
)
def test_frequence_adjustments(changes, expected_frequency):
    assert aoc_01.calibrate(changes) == expected_frequency
