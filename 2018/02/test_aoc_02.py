import aoc_02
import pytest

import aoc_02


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
    """
        abcdef contains no letters that appear exactly two or three times.
        bababc contains two a and three b, so it counts for both.
        abbcde contains two b, but no letter appears exactly three times.
        abcccd contains three c, but no letter appears exactly two times.
        aabcdd contains two a and two d, but it only counts once.
        abcdee contains two e.
        ababab contains three a and three b, but it only counts once.
    """
    assert aoc_02.have_two_or_three_same(box_id) == expected


def test_calculate_checksum():
    """
    Of these box IDs, four of them contain a letter which appears exactly twice,
    and three of them contain a letter which appears exactly three times.
    Multiplying these together produces a checksum of 4 * 3 = 12.
    """
    box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    expected = 12

    assert aoc_02.calculate_checksum(box_ids) == 12


def test_get_prototype_boxes():
    """
    The boxes will have IDs which differ by exactly one character at the same
    position in both strings. For example, given the following box IDs:
    """
    box_ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

    """
    The IDs abcde and axcye are close, but they differ by two characters (the
    second and fourth). However, the IDs fghij and fguij differ by exactly one
    character, the third (h and u). Those must be the correct boxes.
    """
    expected = ("fghij", "fguij")

    assert aoc_02.get_prototype_boxes(box_ids) == expected


@pytest.mark.parametrize(
    "box1, box2, expected",
    [("abcde", "abcde", False), ("baced", "abcde", False), ("fghij", "fguij", True)],
)
def test_diff_by_one(box1, box2, expected):
    assert aoc_02.diff_by_one(box1, box2) == expected


def test_get_common_letters():
    """
    What letters are common between the two correct box IDs? (In the example above,
    this is found by removing the differing character from either ID, producing
    fgij.)
    """
    assert aoc_02.get_common_letters("fghij", "fguij") == "fgij"
