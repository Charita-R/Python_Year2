import pytest
def calc_total(a,b):
    return a+b


def test_total():
    total = calc_total(2, 3)
    assert total == 5