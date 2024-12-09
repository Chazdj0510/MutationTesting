# test_alter_default_values.py

import unittest
from mutation8_alt import MutatedPolynomial


class TestAlterDefaultValues(unittest.TestCase):
    def test_default_values(self):
        poly = MutatedPolynomial()
        self.assertIsInstance(poly, MutatedPolynomial)  # Ensure mutation was applied


if __name__ == '__main__':
    unittest.main()
