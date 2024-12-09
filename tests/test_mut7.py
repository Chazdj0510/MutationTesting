# test_swap_indexing.py

import unittest
from mutation7_swap import MutatedPolynomial


class TestSwapIndexing(unittest.TestCase):
    def test_indexing(self):
        poly = MutatedPolynomial([3, 2, 4])
        result_str = str(poly)
        self.assertNotEqual(result_str, MutatedPolynomial([3, 2, 4]).__str__())  # Expect differences


if __name__ == '__main__':
    unittest.main()
