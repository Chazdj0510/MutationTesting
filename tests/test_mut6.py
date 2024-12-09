# test_alter_conditional.py

import unittest
from mutation6_cond import MutatedPolynomial


class TestAlterConditionalStatements(unittest.TestCase):
    def test_conditional_logic(self):
        poly = MutatedPolynomial([0, 1, 2])
        self.assertTrue(any(coef != 0 for coef in poly.coefficients))  # Verify mutated condition logic


if __name__ == '__main__':
    unittest.main()
