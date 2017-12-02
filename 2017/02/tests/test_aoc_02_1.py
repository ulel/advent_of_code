import pytest

import aoc_02_1


def test_row_5_1_9_5():
    assert(aoc_02_1.calculate_row([5, 1, 9, 5]) == 8)


def test_row_7_5_3():
    assert(aoc_02_1.calculate_row([7, 5, 3]) == 4)


def test_row_2_4_6_8():
    assert(aoc_02_1.calculate_row([2, 4, 6, 8]) == 6)


def test_total():
    input_rows = [
                     [5, 1, 9, 5],
                     [7, 5, 3],
                     [2, 4, 6, 8]
                 ]

            
    assert(aoc_02_1.calculate_total(input_rows) == 18)
