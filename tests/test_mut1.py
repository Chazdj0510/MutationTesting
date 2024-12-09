import unittest
from mutation1_coe import MutatedPolynomial


class TestMutatedPolynomial(unittest.TestCase):
    def test_change_coefficient(self):
        """
        Test whether mutation changes impact polynomial evaluation.
        """
        p1 = MutatedPolynomial([3, 0, 2])  # Change applied at index 1
        result = p1.evaluate(1)
        self.assertNotEqual(result, 3 + 0 * 1 + 2 * (1**2), "Mutation should change the result of the polynomial evaluation.")


if __name__ == "__main__":
    unittest.main()
