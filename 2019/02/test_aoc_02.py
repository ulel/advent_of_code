import operator

import pytest

import aoc_02


@pytest.mark.parametrize(
    "op_code, expected_operator", [(1, operator.add), (2, operator.mul)]
)
def test_get_operator(op_code, expected_operator):
    assert aoc_02.get_operator(op_code) == expected_operator


@pytest.mark.parametrize(
    "program, result",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
    ],
)
def test_run_program(program, result):
    """
    1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
    """
    assert aoc_02.run_program(program) == result


def test_restore_program():
    assert aoc_02.restore_program([1, 2, 3, 4, 5]) == [1, 12, 2, 4, 5]
