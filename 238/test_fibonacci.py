import pytest

from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
def test_fib_negative_number():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_zero():
    assert fib(0) == 0


def test_fib_six():
    assert fib(6) == 8


def test_fib_large_number():
    assert fib(25) == 75025
