""" aoc_05_input.py

    Its sole purpose is to return the input of todays problem in a the format
    the solution expects.
"""


def get_input():
    ''' get_input()

        Return the content of the intput file as a list of strings.
    '''
    with open('input') as input_file:
        return list(map(int, input_file.readlines()))
