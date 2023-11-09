from math import gcd

import pytest


class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @classmethod
    def of(cls, numerator, denominator):
        d = gcd(numerator, denominator)
        return Fraction(numerator // d, denominator // d)

    def representation(self):
        return f"{self._numerator}/{self._denominator}"


@pytest.mark.parametrize("n, d, display", [
    (1, 2, "1/2"),
    (3, 2, "3/2"),
    (1, 3, "1/3"),
    (2, 4, "1/2"),
])
def test_display_fraction(n, d, display):
    assert Fraction.of(n, d).representation() == display
