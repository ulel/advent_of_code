import pytest

import aoc_02_2


def test_row_5_9_2_8():
    assert(aoc_02_2.calculate_row([5, 9, 2, 8]) == 4)


def test_row_9_4_7_3():
    assert(aoc_02_2.calculate_row([9, 4, 7, 3]) == 3)


def test_row_3_8_6_5():
    assert(aoc_02_2.calculate_row([3, 8, 6, 5]) == 2)


def test_total():
    input_rows = [
                    [ 5, 9, 2, 8 ],
                    [ 9, 4, 7, 3 ],
                    [ 3, 8, 6, 5 ],
                 ]

            
    assert(aoc_02_2.calculate_total(input_rows) == 9)
