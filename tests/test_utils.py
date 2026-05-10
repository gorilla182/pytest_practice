from src.utils import *
import pytest

@pytest.mark.parametrize("number, boolean_data" ,[(2, True), (2048, True), (3, False), (0.1, False), (-1, False),(-2, True)])
def test_data(number, boolean_data):
    assert is_even(number) == boolean_data