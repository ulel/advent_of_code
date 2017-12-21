""" test_aoc_07.py

    Test for Advent of Code 2017 day 07
"""

import aoc_07
import aoc_07_input

TEST_INPUT = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def test_find_root():
    nodes = aoc_07_input.parse_input_string(TEST_INPUT)

    expected = 'tknk'
    root = aoc_07.get_root(nodes)

    assert root['name'] == expected


def test_find_imbalance():
    nodes = aoc_07_input.parse_input_string(TEST_INPUT)

    expected = 60
    actual = aoc_07.find_imbalance(nodes)

    assert actual == expected
