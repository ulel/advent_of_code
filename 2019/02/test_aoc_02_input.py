from unittest.mock import mock_open, patch
import pytest

import aoc_02_input


def test_parse_input():

    open_mock = mock_open(read_data="2, 1, 1, 4, 99, 1, 2, 3")

    with patch("aoc_02_input.open", open_mock):
        assert aoc_02_input.get_instructions() == [2, 1, 1, 4, 99, 1, 2, 3]
        open_mock.assert_called_once_with("input", "r")
