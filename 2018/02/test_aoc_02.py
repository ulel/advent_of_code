import aoc_02
import pytest

import aoc_02


"""
    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
"""


@pytest.mark.parametrize(
    "box_id, expected",
    [
        ("abcdef", (0, 0)),
        ("bababc", (1, 1)),
        ("abbcde", (1, 0)),
        ("abcccd", (0, 1)),
        ("aabcdd", (1, 0)),
        ("abcdee", (1, 0)),
        ("ababab", (0, 1)),
    ],
)
def test_have_two_or_three_letters(box_id, expected):
    assert aoc_02.have_two_or_three_same(box_id) == expected


"""
Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.
Multiplying these together produces a checksum of 4 * 3 = 12.
"""


def test_calculate_checksum():
    box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    expected = 12

    assert aoc_02.calculate_checksum(box_ids) == 12
