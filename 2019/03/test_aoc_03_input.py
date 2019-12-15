from unittest.mock import mock_open, patch
import pytest

import aoc_03_input


@pytest.mark.parametrize(
    "instruction_string, expected_instruction",
    [("U20", (0, 20)), ("D20", (0, -20)), ("R20", (20, 0)), ("L20", (-20, 0)),],
)
def test_translate_instruction(instruction_string, expected_instruction):
    assert (
        aoc_03_input._translate_instruction(instruction_string) == expected_instruction
    )


@pytest.mark.parametrize(
    "input_instructions, expected_instructions",
    [
        ("D2001", [[(0, -2001)]]),
        ("R10001,U10", [[(10001, 0), (0, 10)]]),
        ("L5,R30,D10,D20,U18", [[(-5, 0), (30, 0), (0, -10), (0, -20), (0, 18)]]),
        ("U15\nU16", [[(0, 15)], [(0, 16)]]),
        ("U15,D30\nU16,R10,L20", [[(0, 15), (0, -30)], [(0, 16), (10, 0), (-20, 0)]]),
    ],
)
def test_get_cable_instructions(input_instructions, expected_instructions):
    open_mock = mock_open(read_data=input_instructions)

    with patch("aoc_03_input.open", open_mock):
        assert aoc_03_input.get_cable_instructions() == expected_instructions
        open_mock.assert_called_once_with("input", "r")
