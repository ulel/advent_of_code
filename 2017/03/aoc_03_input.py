""" aoc_03_input.py

    Its sole purpose is to return the input of todays problem in a the format
    the solution expects.
"""

def get_input():
    ''' get_input()

        Return the content of the intput file as an int.
    '''
    with open('input') as input_file:
        return int(input_file.readline().strip())
