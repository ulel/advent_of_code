""" aoc_09_input.py

    Its sole purpose is to return the input of todays problem in a the format
    the solution expects.
"""


def get_input():
    ''' get_input()

        Return the content of the intput as expected by the solver.
    '''
    with open('input') as input_file:
        return input_file.read()
