
import unittest
from mutation4_rem_func import MutatedPolynomial


class TestRemoveFunctionality(unittest.TestCase):
    def test_no_evaluation(self):
        poly = MutatedPolynomial([1, 2, 3])
        result = poly.evaluate(5)  # Expected result should be 0
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
