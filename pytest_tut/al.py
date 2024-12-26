import pytest

@pytest.mark.parametrize("num,expected", [(2, 4), (3, 9), (4, 16)])
def test_square(num, expected):
    assert num ** 2 == expected

def test_sum():
    assert 2 + 2 == 4
