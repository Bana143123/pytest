import pytest
from prime import is_prime

@pytest.mark.parametrize("input, expected",[(1,False),(2,True),(3,True),(4,False),(5,True)])
def test_mul(input,expected):
    assert is_prime(input) == expected



