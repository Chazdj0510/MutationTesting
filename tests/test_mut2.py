# test_mutation_modify_arithmetic.py
import unittest
from mutation2_arith import MutatedPolynomial


class TestMutationArithmetic(unittest.TestCase):
    def test_subtraction_instead_of_addition(self):
        p1 = MutatedPolynomial([3, 0, 2])
        p2 = MutatedPolynomial([1, 2, 3])
        result = p1 + p2
        self.assertNotEqual(result.coefficients, [4, 2, 5], "Mutation should change the computed addition logic.")


if __name__ == "__main__":
    unittest.main()
