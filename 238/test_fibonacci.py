from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_


def test_base_case():

    for i in (0,1):
        assert fib(i) == i


def test_exception():

    with pytest.raises(ValueError) as v:
        fib(-1)


def test_simple():


    assert fib(3) == 2


