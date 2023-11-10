from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @classmethod
    def of(cls, numerator, denominator) -> 'Fraction':
        if denominator == 0:
            raise DenominatorIsZeroException

        d = gcd(numerator, denominator)
        return Fraction(numerator // d, denominator // d)

    def __mul__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            return Fraction.of(self._numerator * other._numerator, self._denominator * other._denominator)

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"


class DenominatorIsZeroException(Exception):
    pass
