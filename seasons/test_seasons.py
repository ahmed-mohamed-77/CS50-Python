from seasons import *


def test_isleap_year():
    assert is_leap_year(2024) is True
    assert is_leap_year(2028) is True
    assert is_leap_year(2000) is True
    assert is_leap_year(1972) is True
    assert is_leap_year(1971) is False


def test_count_leap_year():
    assert count_leap_year(2000, 2024) == 7
