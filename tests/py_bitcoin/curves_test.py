import unittest
from py_bitcoin.curves import Point
from py_bitcoin.fields import FieldElement


class CurvesTest(unittest.TestCase):

    def test_point(self):
        self.assertTrue(Point(x=-1, y=-1, a=5, b=7))
        with self.assertRaises(ValueError):
            Point(x=-1, y=-2, a=5, b=7)


    def test_equality(self):
        p1 = Point(x=-1, y=-1, a=5, b=7)
        p2 = Point(x=-1, y=-1, a=5, b=7)
        self.assertTrue(p1 == p2)

        p1 = Point(x=None, y=None, a=5, b=7)
        p2 = Point(x=None, y=None, a=5, b=7)
        self.assertTrue(p1 == p2)


    def test_not_equality(self):
        p1 = Point(x=-1, y=-1, a=5, b=7)
        p2 = Point(x=-1, y=1, a=5, b=7)
        self.assertFalse(p1 == p2)


    def test_addition(self):
        p1 = Point(x=0, y=0, a=5, b=0)
        p2 = Point(x=-1, y=-1, a=5, b=7)
        with self.assertRaises(TypeError):
            p1 + p2

        p1 = Point(x=None, y=None, a=3, b=7)
        p2 = Point(x=18, y=77, a=5, b=7)
        with self.assertRaises(TypeError):
            p1 + p2

        p1 = Point(x=0, y=0, a=3, b=0)
        p2 = Point(x=-1, y=-1, a=5, b=7)
        with self.assertRaises(TypeError):
            p1 + p2

        p1 = Point(x=0, y=0, a=5, b=0)
        p2 = Point(x=None, y=None, a=5, b=0)
        self.assertTrue((p1 + p1) == p2)
        self.assertFalse((p1 + p1) == p1)

        p1 = Point(x=-1, y=-1, a=5, b=7)
        p2 = Point(x=-1, y=1, a=5, b=7)
        p3 = Point(x=None, y=None, a=5, b=7)
        p4 = Point(x=-1, y=1, a=5, b=7)
        self.assertTrue((p1 + p2) == p3)
        self.assertFalse((p1 + p2) == p4)

        p1 = Point(x=-1, y=-1, a=5, b=7)
        p2 = Point(x=18, y=77, a=5, b=7)
        self.assertTrue((p1 + p1) == p2)
        self.assertFalse((p1 + p1) == p1)

        p1 = Point(x=2, y=5, a=5, b=7)
        p2 = Point(x=-1, y=-1, a=5, b=7)
        p3 = Point(x=3, y=-7, a=5, b=7)
        self.assertTrue((p1 + p2) == p3)
        self.assertFalse((p1 + p2) == p1)


if __name__ == "__main__":
    unittest.main()
