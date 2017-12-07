""" test_aoc_01.py

    Tests for Advent of Code 2017 day 01
"""

import aoc_01


def test_part_1_1122_3():
    ''' test_part_1_1122_3()
        Test that the input 1122 give 3 for part 1
    '''
    assert aoc_01.solve_part_1('1122') == 3


def test_part_1_1111_4():
    ''' test_part_1_1111_4()
        Test that the input 1111 give 4 for part 1
    '''
    assert aoc_01.solve_part_1('1111') == 4


def test_part_1_1234_0():
    ''' test_part_1_1234_0()
        Test that the input 1234 give 0 for part 1
    '''
    assert aoc_01.solve_part_1('1234') == 0


def test_part_1_91212129_9():
    ''' test_part_1_91212129_9()
        Test that the input 91212129 give 9 for part 1
    '''
    assert aoc_01.solve_part_1('91212129') == 9


def test_part_2_1212_6():
    ''' test_1212_6()
        Test that the input 1212 give 6 for part 2
    '''
    assert aoc_01.solve_part_2("1212") == 6


def test_part_2_1221_0():
    ''' test_1221_0()
        Test that the input 1221 give 0 for part 2
    '''
    assert aoc_01.solve_part_2('1221') == 0


def test_part_2_123425_4():
    ''' test_123425_4()
        Test that the input 123425 give 4 for part 2
    '''
    assert aoc_01.solve_part_2('123425') == 4


def test_part_2_123123_12():
    ''' test_123123_12()
        Test that the input 123123 give 12 for part 2
    '''
    assert aoc_01.solve_part_2('123123') == 12


def test_part_2_12131415_4():
    ''' test_12131415_4()
        Test that the input 12131415 give 4 for part 2
    '''
    assert aoc_01.solve_part_2('12131415') == 4
