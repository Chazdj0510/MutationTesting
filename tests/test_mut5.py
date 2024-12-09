# test_change_loop_logic.py

import unittest
from mutation5_loop import MutatedPolynomial


class TestChangeLoopLogic(unittest.TestCase):
    def test_loop_logic_error(self):
        poly = MutatedPolynomial([3, 2, 4])
        result = poly.evaluate(2)  # The loop logic has been mutated
        self.assertNotEqual(result, MutatedPolynomial([3, 2, 4]).evaluate(2))


if __name__ == '__main__':
    unittest.main()
