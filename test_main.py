import unittest
from main import calculate_repayment


class TestDebtCalculator(unittest.TestCase):
    def test_without_interest(self):
        result = calculate_repayment(1000, 0, 200)
        self.assertEqual(result, (5, 0, 1000))

    def test_payment_is_too_low(self):
        result = calculate_repayment(1000, 12, 10)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
