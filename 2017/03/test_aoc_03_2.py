""" test_aoc_03.py

    Test for Advent of Code 2017 day 03
"""

import aoc_03_2


def test_get_square_1():
    assert aoc_03_2.get_square(1) == {'cord': (0,0), 'value': 1}


def test_get_square_2():
    assert aoc_03_2.get_square(2) == {'cord': (1, 0), 'value': 1}


def test_get_square_3():
    assert aoc_03_2.get_square(3) == {'cord': (1, -1), 'value': 2}


def test_get_square_3():
    assert aoc_03_2.get_square(3) == {'cord': (1, -1), 'value': 2}


def test_next_direction_down_to_right():
    assert aoc_03_2.next_direction((0, 1)) == (1, 0)
    

def test_next_direction_right_to_up():
    assert aoc_03_2.next_direction((1, 0)) == (0, -1)


def test_next_direction_up_to_left():
    assert aoc_03_2.next_direction((0, -1)) == (-1, 0)


def test_next_direction_left_to_down():
    assert aoc_03_2.next_direction((-1, 0)) == (0, 1)


def test_direction_at_0_0():
    spiral = {(0, 0): 1}

    assert aoc_03_2.get_direction((0, 0), (0, 1), spiral) == (1, 0)


def test_direction_at_1_0():
    spiral = {(0, 0): 1,
              (1, 0): 1}

    assert aoc_03_2.get_direction((1, 0), (1, 0), spiral) == (0, -1)


def test_direction_at_1_minus_1():
    spiral = {(0, 0): 1,
              (1, 0): 1,
              (1, -1): 1}

    assert aoc_03_2.get_direction((1, -1), (0, -1), spiral) == (-1, 0)


def test_direction_at_0_minus_1():
    spiral = {(0, 0): 1,
              (1, 0): 1,
              (1, -1): 1}

    assert aoc_03_2.get_direction((0, -1), (-1, 0), spiral) == (-1, 0)


def test_direction_at_minus_1_minus_1():
    spiral = {(0, 0): 1,
              (1, 0): 1,
              (1, -1): 1,
              (-1, -1): 1}

    assert aoc_03_2.get_direction((-1, -1), (-1, 0), spiral) == (0, 1)


def test_value_0_0():
    spiral = {}

    assert aoc_03_2.value((0, 0), spiral) == 1


def test_value_one_neighbour():
    spiral = {(0, 0): 1}

    assert aoc_03_2.value((1, 0), spiral) == 1


def test_value_two_neighbours():
    spiral = {(0, 0): 1,
              (1, 0): 1}

    assert aoc_03_2.value((1, -1), spiral) == 2
