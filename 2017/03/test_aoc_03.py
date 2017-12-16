""" test_aoc_03.py

    Test for Advent of Code 2017 day 03
"""

import aoc_03


def test_layer_size_0():
    ''' test_layer_size_0()

        Test that the middle layer, 0, is 1 square in size.
    '''
    assert aoc_03.layer_size(0) == 1


def test_layer_size_1():
    ''' test_layer_size_1()

        Test that the second layer, 1, is 8 squares in size.
    '''
    assert aoc_03.layer_size(1) == 8


def test_layer_size_2():
    ''' test_layer_size_2()

        Test that the third layer, 2, is 8 squares in size.
    '''
    assert aoc_03.layer_size(2) == 16


def test_layer_1():
    ''' test_layer_1()

        Test that 1 is in the middle layer, 0, and the last in layer is 1.
    '''
    assert aoc_03.layer_no(1) == (0, 1, 1)


def test_layer_2():
    ''' test_layer_2()

        Test that 1 is in the second layer, 1, and the last in layer is 9.
    '''
    assert aoc_03.layer_no(2) == (1, 8, 9)


def test_layer_12():
    ''' test_layer_12()

        Test that 12 is in the third layer, 2, and the last in layer is 25.
    '''
    assert aoc_03.layer_no(12) == (2, 16, 25)


def test_layer_25():
    ''' test_layer_2()

        Test that 25 is in the third layer, 2.
    '''
    assert aoc_03.layer_no(25) == (2, 16, 25)


def test_layer_26():
    ''' test_layer_2()

        Test that 26 is in the fourth layer, 3.
    '''
    assert aoc_03.layer_no(26) == (3, 24, 49)


def test_cord_1():
    ''' test_cord_1()

        Test that 1 is in the middle, 0:0
    '''
    assert aoc_03.cord(1) == (0, 0)


def test_cord_2():
    ''' test_cord_2()

        Test that 2 is at 1:0
    '''
    assert aoc_03.cord(2) == (1, 0)


def test_cord_3():
    ''' test_cord_2()

        Test that 3 is at 1:1
    '''
    assert aoc_03.cord(3) == (1, 1)


def test_distance_1():
    ''' test_distance_1()

        Test that the distance to 1 is 0.
    '''
    assert aoc_03.distance(1) == 0


def test_12():
    ''' test_distance_12()

        Test that the distance to 12 is 3.
    '''
    assert aoc_03.distance(12) == 3


def test_23():
    ''' test_distance_23()

        Test that the distance to 23 is 2.
    '''
    assert aoc_03.distance(23) == 2


def test_1024():
    ''' test_distance_1024()

        Test that the distance to 1024 is 31.
    '''
    assert aoc_03.distance(1024) == 31
