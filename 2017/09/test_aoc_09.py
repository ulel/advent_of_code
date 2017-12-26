""" test_aoc_09.py

    Test for Advent of Code 2017 day 09
"""

import aoc_09


def test_calculate_score_one_empty_group():
    stream = '{}'
    expected = 1
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_three_nested_groups():
    stream = '{{{}}}'
    expected = 6
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_two_parallel_nested_groups():
    stream = '{{},{}}'
    expected = 5
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_mix_nested_and_parallel():
    stream = '{{{},{},{{}}}}'
    expected = 16
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_one_group_with_garbage():
    stream = '{<a>,<a>,<a>,<a>}'
    expected = 1
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_three_nested_of_garbage():
    stream = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
    expected = 9
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_garbage_with_ignore():
    stream = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    expected = 9
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_calculate_score_garbage_ignore_end():
    stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    expected = 3
    actual, _ = aoc_09.calculate_score(stream)
    assert expected == actual


def test_ignored_garbage_ignore_end():
    stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    expected = 17
    _, actual = aoc_09.calculate_score(stream)
    assert expected == actual
