""" aoc_07_input.py

    Its sole purpose is to return the input of todays problem in a the format
    the solution expects.
"""


def parse_name_weight(name_weight_str):
    ''' parse_name_weight(name_weight_str)

        Return a dictionary with name, weight and an empty children list.
    '''
    [name, weight_str] = name_weight_str.split()

    weight = int(weight_str[1:-1])
    return {'name': name, 'weight': weight, 'children': []}


def parse_line(line):
    ''' parse_line(line)

        Return a dictionary with name, weight and a filled children list if
        there are any on the line.
    '''
    split_line = line.split(' -> ')

    node = parse_name_weight(split_line[0])

    if len(split_line) == 2:
        node['children'] = split_line[1].split(', ')

    return node


def parse_input_string(input_string):
    ''' parse_input_string(input_string)

        Helper to parse input strings for testing purposes.
    '''
    return list(map(parse_line, input_string.split('\n')))


def get_input():
    ''' get_input()

        Return the content of the intput as expected by the solver.
    '''
    nodes = []
    with open('input') as input_file:
        for line in input_file:
            nodes.append(parse_line(line.strip()))

    return nodes
