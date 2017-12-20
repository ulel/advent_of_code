""" test_aoc_04.py

    Test for Advent of Code 2017 day 04
"""

import aoc_04


def test_valid_password():
    assert aoc_04.valid('aa bb cc dd ee') == True


def test_invalid_password_repeated_word():
    assert aoc_04.valid('aa bb cc dd aa') == False


def test_valid_password_similar_word():
    assert aoc_04.valid('aa bb cc dd aaa') == True


def test_invalid_password_anagram():
    assert aoc_04.valid_part_2('abcde xyz ecdab') == False
