import pytest
from ..task.source import compute_inversion


def test_simple_cases():
    assert compute_inversion([1, 3, 5, 2, 4, 6])[0] == 3
    assert compute_inversion([8, 7, 6, 5, 4, 3, 2, 1])[0] == 28


def test_txt_input():
    with open('test.txt', 'r') as input_file:
        data = input_file.read().split()
        data = list(map(lambda x: int(x), data))
        assert compute_inversion(data)[0] == 28
