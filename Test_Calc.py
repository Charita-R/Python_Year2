import mathlib

def test_calc_total():
    total = mathlib.calc_total(5,5)
    assert total == 10

def test_calc_multiply():
    total = mathlib.calc_multiply(5,5)
    assert total == 25