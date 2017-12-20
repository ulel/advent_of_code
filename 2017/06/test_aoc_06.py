""" test_aoc_06.py

    Test for Advent of Code 2017 day 06
"""

import aoc_06

def test_find_max():
    memory_bank = [0, 2, 7, 0]

    assert aoc_06.find_max(memory_bank) == (7, 2)

def test_find_max_last_item():
    memory_bank = [0, 2, 7, 9]

    assert aoc_06.find_max(memory_bank) == (9, 3)

def test_redistribute_1():
    memory_bank = [0, 0]

    aoc_06.redistribute(1, 1, memory_bank)
    assert memory_bank == [0, 1]

def test_redistribute_2():
    assert aoc_06.redistribute(2, 1, [0, 0, 0]) == [0, 1, 1]

def test_redistribute_3_wrop_around():
    assert aoc_06.redistribute(3, 1, [0, 0, 0]) == [1, 1, 1]

def test_first_example():
    memory_bank = [0, 2, 7, 0]

    assert aoc_06.debug(memory_bank) == 5
