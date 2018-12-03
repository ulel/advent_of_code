import re

import aoc_03

CLAIM_REGEXP = re.compile("#(\\d*) @ (\\d*),(\\d*): (\\d*)x(\\d*)")


def parse_claim(claim_line):
    claim_match = CLAIM_REGEXP.match(claim_line)

    claim_id = int(claim_match[1])
    claim_x = int(claim_match[2])
    claim_y = int(claim_match[3])
    claim_width = int(claim_match[4])
    claim_height = int(claim_match[5])

    return aoc_03.Claim(
        id=claim_id, x=claim_x, y=claim_y, width=claim_width, height=claim_height
    )


def get_input():
    """Return input for Advent of Code 2018 day 3 in proper format."""
    with open("input", "r") as claim_file:
        for claim_line in claim_file:
            yield parse_claim(claim_line)
