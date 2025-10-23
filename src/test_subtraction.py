from subtraction import subtract

# wave


def test_subtract_positive():
    assert subtract(10, 3) == 7


def test_subtract_negative():
    assert subtract(3, 10) == -7


def test_subtract_zero():
    assert subtract(0, 5) == -5
