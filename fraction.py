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

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"


class DenominatorIsZeroException(Exception):
    pass
