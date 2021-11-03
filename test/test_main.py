from leap_year_check import *
# from leap_year_check import leap_year_check


# Leap Year if:
def test_divide_by_four_but_not_100():
    assert leap_year_check(2004)
    assert leap_year_check(408)
    assert leap_year_check(8)
    assert leap_year_check(108)
    assert leap_year_check(2000)


def test_divide_by_400():
    assert leap_year_check(400)
    assert leap_year_check(800)
    assert leap_year_check(2000)
    assert leap_year_check(3200)


# Not Leap Year if:
def test_divide_by_100_but_not_400():
    assert not leap_year_check(100)
    assert not leap_year_check(200)
    assert not leap_year_check(700)
    assert not leap_year_check(3300)
    assert not leap_year_check(1700)
    assert not leap_year_check(1800)
    assert not leap_year_check(1900)
    assert not leap_year_check(2100)


def test_not_divisible_by_4():
    assert not leap_year_check(5)
    assert not leap_year_check(17)
    assert not leap_year_check(290)
    assert not leap_year_check(2713)
