import unittest
import square


class SquareTest(unittest.TestCase):


    def test_square_zero_S(self):
        res = square.square_S(0)
        self.assertEqual(res, 0)

    def test_square_normal_S(self):
        res = square.square_S(5)
        self.assertEqual(res, 25)

    def test_square_float_S(self):
        res = square.square_S(2.5)
        self.assertEqual(res, 6.25)

    def test_square_negative_S(self):
        with self.assertRaises(ValueError):
            square.square_S(-4)


    def test_square_P(self):
        res = square.square_P(6)
        self.assertEqual(res, 24)

    def test_square_zero_P(self):
        res = square.square_P(0)
        self.assertEqual(res, 0)

    def test_square_float_P(self):
        res = square.square_P(2.5)
        self.assertEqual(res, 10.0)

    def test_square_negative_P(self):
        with self.assertRaises(ValueError):
            square.square_P(-3)
