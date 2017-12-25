""" aoc_08.py

    Solution for Advent of Code 2017 day 08
"""

import operator
from functools import reduce

import aoc_08_input


REGISTER = {}


def get_op(op_string):
    ''' get_op(op_string)

        Get operator from string.
    '''
    return {'>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
            'dec': operator.sub,
            'inc': operator.add}.get(op_string)


def parse_instruction(string):
    ''' parse_instruction(string)

        Parse a string with instruction and return dict with everything needed
        to execute the instruction in the machine.
    '''
    [target, instr, value, _, comp, comp_op, comp_value] = string.split(' ')

    return {'target': target,
            'op': get_op(instr),
            'value': int(value),
            'comp': comp,
            'comp_value': int(comp_value),
            'comp_op': get_op(comp_op)}


def execute(instruction):
    ''' execute(instruction)

        Executes the provided instruction and stores the result in
        aoc_08.REGISTER.
    '''
    target = REGISTER.get(instruction['target'], 0)
    comp = REGISTER.get(instruction['comp'], 0)

    if instruction['comp_op'](comp, instruction['comp_value']):
        target = instruction['op'](target, instruction['value'])
        REGISTER[instruction['target']] = target

    return target


def get_highest():
    ''' get_highest()

        Return the highest value in the register.
    '''

    return reduce(lambda x, y: x if x > y else y, REGISTER.values())


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer to the problems for day six.
    '''
    aoc_input = aoc_08_input.get_input()
    highest_ever = 0

    for instruction in aoc_input:
        last = execute(instruction)
        if last > highest_ever:
            highest_ever = last

    print('Part 1: {}'.format(get_highest()))
    print('Part 2: {}'.format(highest_ever))


if __name__ == '__main__':
    main()
