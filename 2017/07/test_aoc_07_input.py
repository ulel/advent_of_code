""" test_aoc_07_input.py

    Test for Advent of Code 2017 input for day 07
"""

import aoc_07_input


def test_parse_line_name_weight():
    result = aoc_07_input.parse_line('ebii (61)') 
    expected = {'name': 'ebii', 'weight': 61, 'children': []}
    assert result == expected


def test_parse_line_name_weight_children():
    result = aoc_07_input.parse_line('padx (45) -> pbga, havc, qoyq') 
    expected = {'name': 'padx', 'weight': 45, 
                'children': ['pbga', 'havc', 'qoyq']}
    assert result == expected
