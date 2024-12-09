import unittest
from mutation3_red import MutatedPolynomial


class TestIntroduceRedundantCode(unittest.TestCase):
    def test_redundancy(self):
        poly = MutatedPolynomial([1, 2, 3])
        result = poly.evaluate(2)
        self.assertEqual(result, MutatedPolynomial([1, 2, 3]).evaluate(2))


if __name__ == '__main__':
    unittest.main()
