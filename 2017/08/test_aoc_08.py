""" test_aoc_08.py

    Test for Advent of Code 2017 day 08
"""

import operator

import aoc_08

"""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def test_get_op_gt():
    actual = aoc_08.get_op('>')
    expected = operator.gt

    assert actual == expected


def test_get_op_lt():
    actual = aoc_08.get_op('<')
    expected = operator.lt

    assert actual == expected


def test_get_op_eq():
    actual = aoc_08.get_op('==')
    expected = operator.eq

    assert actual == expected


def test_get_op_lte():
    actual = aoc_08.get_op('<=')
    expected = operator.le

    assert actual == expected


def test_get_op_gte():
    actual = aoc_08.get_op('>=')
    expected = operator.ge

    assert actual == expected


def test_get_op_not_equal():
    actual = aoc_08.get_op('!=')
    expected = operator.ne

    assert actual == expected


def test_get_op_dec():
    actual = aoc_08.get_op('dec')
    expected = operator.sub

    assert actual == expected


def test_get_op_inc():
    actual = aoc_08.get_op('inc')
    expected = operator.add

    assert actual == expected


def test_parse_instruction_inc_greater_than():
    input_str = 'b inc 5 if a > 1'
    expected = {'target': 'b',
                'op': operator.add,
                'value': 5,
                'comp': 'a',
                'comp_value': 1,
                'comp_op': operator.gt}

    actual = aoc_08.parse_instruction(input_str)
    
    assert actual == expected


def test_parse_instruction_dec_less_than():
    input_str = 'a dec 1 if b < 5'
    expected = {'target': 'a',
                'op': operator.sub,
                'value': 1,
                'comp': 'b',
                'comp_value': 5,
                'comp_op': operator.lt}

    actual = aoc_08.parse_instruction(input_str)

    assert actual == expected


def test_parse_instruction_inc_equals():
    input_str = 'a inc 7 if b == 8'
    expected = {'target': 'a',
                'op': operator.add,
                'value': 7,
                'comp': 'b',
                'comp_value': 8,
                'comp_op': operator.eq}

    actual = aoc_08.parse_instruction(input_str)

    assert actual == expected


def test_execute_instruction_empty_register():
    aoc_08.REGISTER = {}

    instruction = {'target': 'a',
                   'op': operator.add,
                   'value': 7,
                   'comp': 'b',
                   'comp_value': 0,
                   'comp_op': operator.eq}

    expected = 7

    aoc_08.execute(instruction)

    actual = aoc_08.REGISTER.get('a')

    assert actual == expected


def test_execute_instruction_gt_comp():
    aoc_08.REGISTER = {'a': 7}

    instruction = {'target': 'a',
                   'op': operator.add,
                   'value': 7,
                   'comp': 'a',
                   'comp_value': 6,
                   'comp_op': operator.gt}

    expected = 14

    aoc_08.execute(instruction)

    actual = aoc_08.REGISTER.get('a')

    assert actual == expected


def test_get_highest_value():
    aoc_08.REGISTER = {}

    input_str = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10 """
    
    for line in input_str.strip().split('\n'):
        instruction = aoc_08.parse_instruction(line.strip())
        aoc_08.execute(instruction)

    expected = 1
    actual = aoc_08.get_highest()

    assert actual == expected

