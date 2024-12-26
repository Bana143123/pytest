from fac import fact
import pytest

def test_fact():
    assert fact(5)==120
    assert fact(4)==24
    assert fact(3)==6

def test_fac_zero():
    assert fact(0)==1


def test_fac_one():
    assert fact(1)==0

def test_factorial_negative_number():
    with pytest.raises(ValueError, match="Factorial is not supported for negative numbers."):
        fact(-5)
