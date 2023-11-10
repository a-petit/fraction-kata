import pytest

from fraction import Fraction, DenominatorIsZeroException


@pytest.mark.parametrize("n, d, representation", [
    (1, 2, "1/2"),
    (1, 3, "1/3"),
    (3, 2, "3/2"),
    (2, 4, "1/2")
])
def test_represent_fraction(n, d, representation):
    assert Fraction.of(n, d).representation() == representation


def test_create_fraction_with_denominator_zero_raise_exception():
    with pytest.raises(DenominatorIsZeroException):
        Fraction.of(1, 0)