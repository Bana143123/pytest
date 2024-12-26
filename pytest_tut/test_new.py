# Demonstrate dynamic parameterization using the pytest_generate_tests hook.

import pytest

@pytest.mark.parametrize("input,expected",[(1,9),(2,4),(3,6),(4,8)])
def test_mul(input,expected):
    res = input * 2
    assert res == expected