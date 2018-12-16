import pytest

import aoc_07

import aoc_07_input

step_lines = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
]

parsed_steps = [
    ("C", "A"),
    ("C", "F"),
    ("A", "B"),
    ("A", "D"),
    ("B", "E"),
    ("D", "E"),
    ("F", "E"),
]


@pytest.mark.parametrize("step_line, expected", zip(step_lines, parsed_steps))
def test_parse_step(step_line, expected):
    assert aoc_07_input._parse_step(step_line) == expected


def test_get_order():
    """
    Visually, these requirements look like this:


      -->A--->B--
     /    \      \
    C      -->D----->E
     \           /
      ---->F-----

    Your first goal is to determine the order in which the steps should be
    completed. If more than one step is ready, choose the step which is first
    alphabetically. In this example, the steps would be completed as follows:

        Only C is available, and so it is done first.
        Next, both A and F are available. A is first alphabetically, so it is done
            next.
        Then, even though F was available earlier, steps B and D are now also
            available, and B is the first alphabetically of the three.
        After that, only D and F are available. E is not available because only
            some of its prerequisites are complete. Therefore, D is completed next.
        F is the only choice, so it is done next.
        Finally, E is completed.

    So, in this example, the correct order is CABDFE.
    """

    assert aoc_07.get_order(parsed_steps) == ["C", "A", "B", "D", "F", "E"]
