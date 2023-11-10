import pytest


class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @classmethod
    def of(cls, numerator, denominator) -> 'Fraction':
        return Fraction(numerator, denominator)

    def representation(self) -> str:
        return f"{self._numerator}/{self._denominator}"


@pytest.mark.parametrize("n, d, representation", [
    (1, 2, "1/2"),
    (1, 3, "1/3"),
    (3, 2, "3/2"),
])
def test_represent_fraction(n, d, representation):
    assert Fraction.of(n, d).representation() == representation
