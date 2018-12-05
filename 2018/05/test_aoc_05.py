import pytest

import aoc_05

@pytest.mark.parametrize("polymer, expected",
        [(b'aA', []),
         (b'abBA', []),
         (b'abAB', [ord(char) for char in 'abAB']),
         (b'aabAAB', [ord(char) for char in 'aabAAB']),
         (b'dabAcCaCBAcCcaDA', [ord(char) for char in 'dabCBAcaDA'])])
def test_trigger_reaction(polymer, expected):
    """
    In aA, a and A react, leaving nothing behind.
    In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
    In abAB, no two adjacent units are of the same type, and so nothing happens.
    In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
    """
    assert aoc_05.trigger_reaction(polymer) == expected
