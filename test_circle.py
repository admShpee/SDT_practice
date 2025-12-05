import unittest
import circle


class GeometryTestCase(unittest.TestCase):


    def test_circle_S(self):
        res = circle.circle_S(2)
        self.assertEqual(res, 12.56)

    def test_circle_zero_S(self):
        res = circle.circle_S(0)
        self.assertEqual(res, 0)

    def test_circle_negative_S(self):
        with self.assertRaises(ValueError):
            circle.circle_S(-3)

    def test_circle_float_S(self):
        res = circle.circle_S(1.5)
        self.assertEqual(res, 7.065)


    def test_circle_P(self):
        res = circle.circle_P(2)
        self.assertEqual(res, 12.56)

    def test_circle_zero_P(self):
        res = circle.circle_P(0)
        self.assertEqual(res, 0)

    def test_circle_negative_P(self):
        with self.assertRaises(ValueError):
            circle.circle_P(-5)

    def test_circle_float_P(self):
        res = circle.circle_P(1.5)
        self.assertEqual(res, 9.42)
