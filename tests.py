import pytest
from hypothesis import given, strategies

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


def test_multiply_fraction_with_same_numerator_1():
    f1 = Fraction.of(1, 3)
    f2 = Fraction.of(1, 5)

    product = f1 * f2

    assert product.representation() == "1/15"


def test_multiply_fraction_with_same_numerator_2():
    f1 = Fraction.of(1, 3)
    f2 = Fraction.of(1, 7)

    product = f1 * f2

    assert product.representation() == "1/21"


def test_multiply_fraction_with_different_numerator():
    f1 = Fraction.of(3, 2)
    f2 = Fraction.of(5, 7)

    product = f1 * f2

    assert product.representation() == "15/14"


@given(
    strategies.integers(),
    strategies.integers(min_value=1),
    strategies.integers(),
    strategies.integers(min_value=1))
def test_multiply_fractions(n1, d1, n2, d2):
    f1 = Fraction.of(n1, d1)
    f2 = Fraction.of(n2, d2)

    product = f1 * f2

    assert product.representation() == Fraction.of(n1 * n2, d1 * d2).representation()

