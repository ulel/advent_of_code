"""
--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves
are making decent progress, but are still struggling with the suit's size
reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their
problem eventually, you can do better. You scan the chemical composition of the
suit's material and discover that it is formed by extremely long polymers (one
of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each
other such that two adjacent units of the same type and opposite polarity are
destroyed. Units' types are represented by letters; units' polarity is
represented by capitalization. For instance, r and R are units with the same
type but opposite polarity, whereas r and s are entirely different types and do
not react.

For example:

    In aA, a and A react, leaving nothing behind.
    In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
    In abAB, no two adjacent units are of the same type, and so nothing happens.
    In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.

Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.

After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in
this puzzle and others, the input is large; if you copy/paste your input, make
sure you get the whole thing.)
"""

import aoc_05_input

def trigger_reaction(polymer):
    current_unit = None
    result = []

    for next_unit in polymer:
        if not current_unit:
            current_unit = next_unit
            continue

        if current_unit + 32 == next_unit or current_unit - 32 == next_unit:
            current_unit = result.pop() if result else None
        else:
            result.append(current_unit)
            current_unit = next_unit

    if current_unit and current_unit != 10:
        result.append(current_unit)

    return result

def main():

    part_1_result = trigger_reaction(aoc_05_input.get_input())
    part_1 = len(part_1_result)

    print(f'Advent of Code 2018 05 part 1: {part_1}')

if __name__ == '__main__':
    main()
