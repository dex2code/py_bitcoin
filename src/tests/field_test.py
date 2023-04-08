from .. import Field
import pytest


def test_valid_points():
    assert Field.FieldElement(num=3, prime=7)
    assert Field.FieldElement(num=7, prime=11)


def test_invalid_points():
    with pytest.raises(ValueError):
        Field.FieldElement(num=-3, prime=7)
        Field.FieldElement(num=13, prime=7)


def test_equality():
    e1 = Field.FieldElement(11, 13)
    e2 = Field.FieldElement(11, 13)
    assert e1 == e2


def test_not_equality():
    e1 = Field.FieldElement(11, 13)
    e2 = Field.FieldElement(7, 13)
    assert not e1 == e2


def test_addition():
    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(7, 13)
    e3 = Field.FieldElement(10, 13)
    e4 = Field.FieldElement(1, 13)
    assert (e1 + e2) == e3
    assert not (e1 + e2) == e4

    e1 = Field.FieldElement(11, 13)
    e2 = Field.FieldElement(7, 13)
    e3 = Field.FieldElement(5, 13)
    e4 = Field.FieldElement(8, 13)
    assert (e1 + e2) == e3
    assert not (e1 + e2) == e4

    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(7, 11)
    with pytest.raises(TypeError):
        e3 = e1 + e2


def test_subtraction():
    e1 = Field.FieldElement(7, 13)
    e2 = Field.FieldElement(3, 13)
    e3 = Field.FieldElement(4, 13)
    e4 = Field.FieldElement(1, 13)
    assert (e1 - e2) == e3
    assert not (e1 - e2) == e4

    e1 = Field.FieldElement(7, 13)
    e2 = Field.FieldElement(11, 13)
    e3 = Field.FieldElement(9, 13)
    e4 = Field.FieldElement(8, 13)
    assert (e1 - e2) == e3
    assert not (e1 - e2) == e4

    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(7, 11)
    with pytest.raises(TypeError):
        e3 = e1 - e2


def test_multiplication():
    e1 = Field.FieldElement(5, 17)
    e2 = Field.FieldElement(3, 17)
    e3 = Field.FieldElement(15, 17)
    e4 = Field.FieldElement(10, 17)
    assert (e1 * e2) == e3
    assert not (e1 * e2) == e4

    e1 = Field.FieldElement(7, 13)
    e2 = Field.FieldElement(11, 13)
    e3 = Field.FieldElement(12, 13)
    e4 = Field.FieldElement(8, 13)
    assert (e1 * e2) == e3
    assert not (e1 * e2) == e4

    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(7, 11)
    with pytest.raises(TypeError):
        e3 = e1 * e2


def test_division():
    e1 = Field.FieldElement(3, 31)
    e2 = Field.FieldElement(24, 31)
    e3 = Field.FieldElement(4, 31)
    e4 = Field.FieldElement(10, 31)
    assert (e1 / e2) == e3
    assert not (e1 / e2) == e4

    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(5, 13)
    e3 = Field.FieldElement(11, 13)
    e4 = Field.FieldElement(8, 13)
    assert (e1 / e2) == e3
    assert not (e1 / e2) == e4

    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(7, 11)
    with pytest.raises(TypeError):
        e3 = e1 / e2
    
    e1 = Field.FieldElement(3, 13)
    e2 = Field.FieldElement(0, 13)
    with pytest.raises(ZeroDivisionError):
        e3 = e1 / e2


def test_exponentiation():
    e1 = Field.FieldElement(7, 17)
    e2 = Field.FieldElement(11, 17)
    e3 = Field.FieldElement(3, 17)
    assert (e1**5) == e2
    assert not (e1**5) == e3

    e1 = Field.FieldElement(17, 31)
    e2 = Field.FieldElement(29, 31)
    e3 = Field.FieldElement(3, 31)
    assert (e1**-3) == e2
    assert not (e1**-3) == e3
