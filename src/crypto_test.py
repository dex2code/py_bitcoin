import unittest
from py_bitcoin.fields import FieldElement
from py_bitcoin.curves import Point


class CryptoTest(unittest.TestCase):

    def test_point_on_curve(self):
        prime = 223
        a = FieldElement(num=0, prime=prime)
        b = FieldElement(num=7, prime=prime)

        valid_points = [(192, 105), (17, 56), (1, 193)]
        invalid_points = [(200, 119), (49, 99), (205, 84)]

        for x_raw, y_raw in valid_points:
            x = FieldElement(num=x_raw, prime=prime)
            y = FieldElement(num=y_raw, prime=prime)
            Point(x=x, y=y, a=a, b=b)
        
        for x_raw, y_raw in invalid_points:
            x = FieldElement(num=x_raw, prime=prime)
            y = FieldElement(num=y_raw, prime=prime)
            with self.assertRaises(ValueError):
                Point(x=x, y=y, a=a, b=b)


    def test_add_points_on_curve(self):
        prime = 223
        a = FieldElement(num=0, prime=prime)
        b = FieldElement(num=7, prime=prime)

        left_points = [(170, 142), (47, 71), (143, 98)]
        right_points = [(60, 139), (17, 56), (76, 66)]
        check_points = [(220, 181), (215, 68), (47, 71)]

        for point_left, point_right, point_check in zip(left_points, right_points, check_points):
            x_raw_left = point_left[0]
            y_raw_left = point_left[1]
            x_raw_right = point_right[0]
            y_raw_right = point_right[1]
            x_raw_check = point_check[0]
            y_raw_check = point_check[1]
            
            x_left = FieldElement(num=x_raw_left, prime=prime)
            y_left = FieldElement(num=y_raw_left, prime=prime)
            x_right = FieldElement(num=x_raw_right, prime=prime)
            y_right = FieldElement(num=y_raw_right, prime=prime)
            x_check = FieldElement(num=x_raw_check, prime=prime)
            y_check = FieldElement(num=y_raw_check, prime=prime)

            p_left = Point(x=x_left, y=y_left, a=a, b=b)
            p_right = Point(x=x_right, y=y_right, a=a, b=b)
            p_check = Point(x=x_check, y=y_check, a=a, b=b)

            self.assertTrue((p_left + p_right) == p_check)


if __name__ == "__main__":
    unittest.main()