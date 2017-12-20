""" test_aoc_04.py

    Test for Advent of Code 2017 day 04
"""

import aoc_05


def test_execute():
    instructions = [0, 3, 0, 1, -3]

    assert aoc_05.execute(instructions) == 5


def test_execute_part_2():
    instructions = [0, 3, 0, 1, -3]

    assert aoc_05.execute(instructions, dec_limit=3) == 10
