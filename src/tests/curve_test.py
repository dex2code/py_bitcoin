from .. import Curve
from .. import Field
import pytest


def test_point():
    assert Curve.Point(x=-1, y=-1, a=5, b=7)
    with pytest.raises(ValueError):
        Curve.Point(x=-1, y=-2, a=5, b=7)


def test_equality():
    p1 = Curve.Point(x=-1, y=-1, a=5, b=7)
    p2 = Curve.Point(x=-1, y=-1, a=5, b=7)
    assert p1 == p2

    p1 = Curve.Point(x=None, y=None, a=5, b=7)
    p2 = Curve.Point(x=None, y=None, a=5, b=7)
    assert p1 == p2


def test_not_equality():
    p1 = Curve.Point(x=-1, y=-1, a=5, b=7)
    p2 = Curve.Point(x=-1, y=1, a=5, b=7)
    assert not p1 == p2


def test_addition():
    p1 = Curve.Point(x=0, y=0, a=5, b=0)
    p2 = Curve.Point(x=-1, y=-1, a=5, b=7)
    with pytest.raises(TypeError):
        p1 + p2

    p1 = Curve.Point(x=None, y=None, a=3, b=7)
    p2 = Curve.Point(x=18, y=77, a=5, b=7)
    with pytest.raises(TypeError):
        p1 + p2

    p1 = Curve.Point(x=0, y=0, a=3, b=0)
    p2 = Curve.Point(x=-1, y=-1, a=5, b=7)
    with pytest.raises(TypeError):
        p1 + p2

    p1 = Curve.Point(x=0, y=0, a=5, b=0)
    p2 = Curve.Point(x=None, y=None, a=5, b=0)
    assert p1 + p1 == p2
    assert not p1 + p1 == p1

    p1 = Curve.Point(x=-1, y=-1, a=5, b=7)
    p2 = Curve.Point(x=-1, y=1, a=5, b=7)
    p3 = Curve.Point(x=None, y=None, a=5, b=7)
    p4 = Curve.Point(x=-1, y=1, a=5, b=7)
    assert p1 + p2 == p3
    assert not p1 + p2 == p4

    p1 = Curve.Point(x=-1, y=-1, a=5, b=7)
    p2 = Curve.Point(x=18, y=77, a=5, b=7)
    assert p1 + p1 == p2
    assert not p1 + p1 == p1

    p1 = Curve.Point(x=2, y=5, a=5, b=7)
    p2 = Curve.Point(x=-1, y=-1, a=5, b=7)
    p3 = Curve.Point(x=3, y=-7, a=5, b=7)
    assert p1 + p2 == p3
    assert not p1 + p2 == p2