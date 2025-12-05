import unittest
import rectangle


class RectangleTest(unittest.TestCase):
    def test_rectangle_zero_S(self):
        res = rectangle.rectangle_S(8, 0)
        self.assertEqual(res, 0)

    def test_rectangle_square_S(self):
        res = rectangle.rectangle_S(2, 2)
        self.assertEqual(res, 4)

    def test_rectangle_normal_S(self):
        res = rectangle.rectangle_S(4, 9)
        self.assertEqual(res, 36)

    def test_rectangle_negative_S(self):
        with self.assertRaises(ValueError):
            rectangle.rectangle_S(-5, -3)


    def test_rectangle_P(self):
        res = rectangle.rectangle_P(4, 7)
        self.assertEqual(res, 22)

    def test_rectangle_zero_P(self):
        res = rectangle.rectangle_P(8, 0)
        self.assertEqual(res, 16)

    def test_rectangle_negative_P(self):
        with self.assertRaises(ValueError):
            rectangle.rectangle_P(2, -3)

    def test_rectangle_float_P(self):
        res = rectangle.rectangle_P(2.5, 4.0)
        self.assertEqual(res, 13.0)

    def test_rectangle_float_S(self):
        res = rectangle.rectangle_S(2.5, 4)
        self.assertEqual(res, 10.0)