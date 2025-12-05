import unittest
import triangle


class TriangleTest(unittest.TestCase):

    def test_triangle_zero_S(self):
        res = triangle.triangle_S(8, 0)
        self.assertEqual(res, 0)

    def test_triangle_normal_S(self):
        res = triangle.triangle_S(8, 3)
        self.assertEqual(res, 12.0)

    def test_triangle_both_zero_S(self):
        res = triangle.triangle_S(0, 0)
        self.assertEqual(res, 0)

    def test_triangle_negative_S(self):
        with self.assertRaises(ValueError):
            triangle.triangle_S(-4, -2)


    def test_triangle_float_S(self):
        res = triangle.triangle_S(5.5, 2)
        self.assertEqual(res, 5.5)



    def test_triangle_P(self):
        res = triangle.triangle_P(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_zero_P(self):
        with self.assertRaises(ValueError):
            triangle.triangle_P(0, 4, 5)

    def test_triangle_negative_P(self):
        with self.assertRaises(ValueError):
            triangle.triangle_P(2, -3, 4)

    def test_triangle_multiple_negative_P(self):
        with self.assertRaises(ValueError):
            triangle.triangle_P(-3, -4, 5)

    def test_not_a_triangle_P(self):
        with self.assertRaises(ValueError):
            triangle.triangle_P(1, 2, 10)

    def test_triangle_float_P(self):
        res = triangle.triangle_P(2.5, 3.5, 4.0)
        self.assertEqual(res, 10.0)

