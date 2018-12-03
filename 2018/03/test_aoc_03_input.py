import pytest

import aoc_03
import aoc_03_input


@pytest.mark.parametrize(
    "claim_line, claim",
    [
        ("#1 @ 1,3: 4x4", aoc_03.Claim(id=1, x=1, y=3, width=4, height=4)),
        (
            "#1234 @ 103,3000: 129x56",
            aoc_03.Claim(id=1234, x=103, y=3000, width=129, height=56),
        ),
    ],
)
def test_parse_claim(claim_line, claim):
    assert aoc_03_input.parse_claim(claim_line) == claim
