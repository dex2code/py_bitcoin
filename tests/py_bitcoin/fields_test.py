import unittest
from py_bitcoin.fields import FieldElement


class FieldsTest(unittest.TestCase):

    def test_valid_points(self):
        self.assertTrue(FieldElement(num=3, prime=7))
        self.assertTrue(FieldElement(num=7, prime=11))


    def test_invalid_points(self):
        with self.assertRaises(ValueError):
            FieldElement(num=-3, prime=7)
        with self.assertRaises(ValueError):
            FieldElement(num=13, prime=7)


    def test_equality(self):
        e1 = FieldElement(11, 13)
        e2 = FieldElement(11, 13)
        self.assertTrue(e1 == e2)


    def test_not_equality(self):
        e1 = FieldElement(11, 13)
        e2 = FieldElement(7, 13)
        self.assertFalse(e1 == e2)


    def test_addition(self):
        e1 = FieldElement(3, 13)
        e2 = FieldElement(7, 13)
        e3 = FieldElement(10, 13)
        e4 = FieldElement(1, 13)
        self.assertTrue((e1 + e2) == e3)
        self.assertFalse((e1 + e2) == e4)

        e1 = FieldElement(11, 13)
        e2 = FieldElement(7, 13)
        e3 = FieldElement(5, 13)
        e4 = FieldElement(8, 13)
        self.assertTrue((e1 + e2) == e3)
        self.assertFalse((e1 + e2) == e4)

        e1 = FieldElement(3, 13)
        e2 = FieldElement(7, 11)
        with self.assertRaises(TypeError):
            e1 + e2


    def test_subtraction(self):
        e1 = FieldElement(7, 13)
        e2 = FieldElement(3, 13)
        e3 = FieldElement(4, 13)
        e4 = FieldElement(1, 13)
        self.assertTrue((e1 - e2) == e3)
        self.assertFalse((e1 - e2) == e4)

        e1 = FieldElement(7, 13)
        e2 = FieldElement(11, 13)
        e3 = FieldElement(9, 13)
        e4 = FieldElement(8, 13)
        self.assertTrue((e1 - e2) == e3)
        self.assertFalse((e1 - e2) == e4)

        e1 = FieldElement(3, 13)
        e2 = FieldElement(7, 11)
        with self.assertRaises(TypeError):
            e1 - e2


    def test_multiplication(self):
        e1 = FieldElement(5, 17)
        e2 = FieldElement(3, 17)
        e3 = FieldElement(15, 17)
        e4 = FieldElement(10, 17)
        self.assertTrue((e1 * e2) == e3)
        self.assertFalse((e1 * e2) == e4)

        e1 = FieldElement(7, 13)
        e2 = FieldElement(11, 13)
        e3 = FieldElement(12, 13)
        e4 = FieldElement(8, 13)
        self.assertTrue((e1 * e2) == e3)
        self.assertFalse((e1 * e2) == e4)

        e1 = FieldElement(3, 13)
        e2 = FieldElement(7, 11)
        with self.assertRaises(TypeError):
            e1 * e2


    def test_division(self):
        e1 = FieldElement(3, 31)
        e2 = FieldElement(24, 31)
        e3 = FieldElement(4, 31)
        e4 = FieldElement(10, 31)
        self.assertTrue((e1 / e2) == e3)
        self.assertFalse((e1 / e2) == e4)

        e1 = FieldElement(3, 13)
        e2 = FieldElement(5, 13)
        e3 = FieldElement(11, 13)
        e4 = FieldElement(8, 13)
        self.assertTrue((e1 / e2) == e3)
        self.assertFalse((e1 / e2) == e4)

        e1 = FieldElement(3, 13)
        e2 = FieldElement(7, 11)
        with self.assertRaises(TypeError):
            e1 / e2
        
        e1 = FieldElement(3, 13)
        e2 = FieldElement(0, 13)
        with self.assertRaises(ZeroDivisionError):
            e1 / e2


    def test_exponentiation(self):
        e1 = FieldElement(7, 17)
        e2 = FieldElement(11, 17)
        e3 = FieldElement(3, 17)
        self.assertTrue((e1**5) == e2)
        self.assertFalse((e1**5) == e3)

        e1 = FieldElement(17, 31)
        e2 = FieldElement(29, 31)
        e3 = FieldElement(3, 31)
        self.assertTrue((e1**-3) == e2)
        self.assertFalse((e1**-3) == e3)


if __name__ == "__main__":
    unittest.main()
