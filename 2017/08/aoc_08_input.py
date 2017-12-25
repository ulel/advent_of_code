""" aoc_08_input.py

    Its sole purpose is to return the input of todays problem in a the format
    the solution expects.
"""

import aoc_08


def get_input():
    ''' get_input()

        Return the content of the intput as expected by the solver.
    '''
    with open('input') as input_file:
        return list(map(aoc_08.parse_instruction, input_file.readlines()))
