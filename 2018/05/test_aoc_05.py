import pytest

import aoc_05


@pytest.mark.parametrize(
    "polymer, expected",
    [
        (b"aA", []),
        (b"abBA", []),
        (b"abAB", [ord(char) for char in "abAB"]),
        (b"aabAAB", [ord(char) for char in "aabAAB"]),
        (b"dabAcCaCBAcCcaDA", [ord(char) for char in "dabCBAcaDA"]),
    ],
)
def test_trigger_reaction(polymer, expected):
    """
    In aA, a and A react, leaving nothing behind.
    In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
    In abAB, no two adjacent units are of the same type, and so nothing happens.
    In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
    """
    assert aoc_05.trigger_reaction(polymer) == expected


def test_get_shortest():
    """
    For example, again using the polymer dabAcCaCBAcCcaDA from above:

    Removing all A/a units produces dbcCCBcCcD.
        Fully reacting this polymer produces dbCBcD, which has length 6.
    Removing all B/b units produces daAcCaCAcCcaDA.
        Fully reacting this polymer produces daCAcaDA, which has length 8.
    Removing all C/c units produces dabAaBAaDA.
        Fully reacting this polymer produces daDA, which has length 4.
    Removing all D/d units produces abAcCaCBAcCcaA.
        Fully reacting this polymer produces abCBAc, which has length 6.

    In this example, removing all C/c units was best, producing the answer 4.
    """
    polymer = b"dabAcCaCBAcCcaDA"

    assert aoc_05.get_shortest(polymer) == 4
