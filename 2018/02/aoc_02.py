"""

--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the
device. "Destination reached. Current Year: 1518. Current Location: North Pole
Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure
either. But now that so many people have chimneys, maybe he could sneak in that
way?" Another voice responds, "Actually, we've been working on a new kind of
suit that would let him fit through tight spaces like that. But, I heard that a
few days ago, they lost the prototype fabric, the design plans, everything!
Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse?
They'd be stored together, so the box IDs should be similar. Too bad it would
take forever to search the warehouse for two similar box IDs..." They walk too
far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes
you could cause if you were discovered - and use your fancy wrist device to
quickly scan every box and produce a list of the likely candidates (your puzzle
input).

To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare it
to what your device predicts.

For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.
Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""

import collections

import aoc_02_input


def have_two_or_three_same(box_id):
    """
    Return a tuple with first field being a 1 if box_id counts at least one
    pair and second field being the same for triplet.
    """
    result = (0, 0)

    for (_, count) in collections.Counter(box_id).items():
        if count == 2:
            result = (1, result[1])
        if count == 3:
            result = (result[0], 1)

    return result


def calculate_checksum(box_ids):
    """Calculate checksum according to instructions for Advent of Code 2018 02."""
    number_with_pairs = 0
    number_with_triplets = 0

    for (pair, triplet) in map(have_two_or_three_same, box_ids):
        number_with_pairs += pair
        number_with_triplets += triplet

    return number_with_pairs * number_with_triplets


def main():
    """Print out the answers to Advent of Code 2018 day 2."""
    part_1 = calculate_checksum(aoc_02_input.get_input())
    print(f"Advent of Code 2018 02 part 1: {part_1}")


if __name__ == "__main__":
    main()
