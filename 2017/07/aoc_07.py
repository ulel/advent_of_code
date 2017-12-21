""" aoc_07.py

    Solution for Advent of Code 2017 day 07
"""

import collections

import aoc_07_input


def build_tree(root, nodes):
    ''' build_tree(root, nodes)

        Given the root and a list of nodes, it builds a tree outwards.
    '''
    childrens = root['children']
    root['children'] = []

    for node_name in childrens:
        node = filter(lambda x, n=node_name: x['name'] == n, nodes).__next__()

        nodes.remove(node)
        root['children'].append(node)
        build_tree(node, nodes)


def get_root(nodes):
    ''' get_root(nodes)

        Find the root among all nodes, the one with no parent, and return it.
    '''
    candidates = nodes[:]

    for node in nodes:
        for name in node['children']:
            candidates = [n for n in candidates if n['name'] != name]

    return candidates[0]


def calc_total_weights(tree):
    ''' calc_total_weights(tree)

        Calculate the total weights for all branches in the tree.
    '''
    totals = []

    for children in tree['children']:
        totals.append(children['weight'] +
                      sum(calc_total_weights(children)))

    tree['total'] = tree['weight'] + sum(totals)

    return totals


def find_faulty_node(tree):
    ''' find_faulty_node(tree)

        Find the node with the wrong weight and return what weight it should
        have instead.
    '''

    weight_count = collections.Counter([children['total'] for children
                                        in tree['children']])

    if len(weight_count) == 2:
        weight, _ = weight_count.most_common()[:-2:-1][0]  # The odd one
        odd_node = filter(lambda x: x['total'] == weight,
                          tree['children']).__next__()
        return find_faulty_node(odd_node)

    return tree


def find_imbalance(nodes):
    ''' find_imbalance(nodes)

        Build a tree from the given nodes, then find the imbalance in it and
        return how the weight need to change to fix it.
    '''
    root = get_root(nodes)
    nodes.remove(root)

    build_tree(root, nodes)

    totals = calc_total_weights(root)

    faulty_node = find_faulty_node(root)

    [(common, _), (faulty, _)] = collections.Counter(totals).most_common(2)

    return faulty_node['weight'] + common - faulty


def main():
    ''' main()

        Main function that use the input from Advent of Code and print the
        answer to the problems for day seven.
    '''
    aoc_input = aoc_07_input.get_input()

    print('Part 1: {}'.format(get_root(aoc_input[:])['name']))
    print('Part 2: {}'.format(find_imbalance(aoc_input[:])))


if __name__ == '__main__':
    main()
