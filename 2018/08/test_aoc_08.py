import aoc_08

import pytest

"""
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

In this example, each node of the tree is also marked with an underline
starting with a letter for easier identification. In it, there are four nodes:

    A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
    B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
    C, which has 1 child node (D) and 1 metadata entry (2).
    D, which has 0 child nodes and 1 metadata entry (99).

The first check done on the license file is to simply add up all of the
metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.
"""


@pytest.fixture
def example_input():
    return [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


def test_calculate_sum_no_child_no_metadata():
    node_input = [0, 0]
    expected = (0, [])
    assert aoc_08.calculate_sum(node_input) == expected


def test_calculate_sum_no_child_with_metadata():
    node_input = [0, 3, 1, 2, 3]
    expected = (6, [])
    assert aoc_08.calculate_sum(node_input) == expected


def test_calculate_sum_one_child_no_metadata():
    node_input = [1, 0, 0, 0]
    expected = (0, [])
    assert aoc_08.calculate_sum(node_input) == expected


def test_calculate_sum(example_input):
    expected = (138, [])

    assert aoc_08.calculate_sum(example_input) == expected
