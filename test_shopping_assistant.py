import unittest
from shopping_assistant import calculate_discount, compare_prices, is_good_deal, apply_coupon

class TestShoppingAssistant(unittest.TestCase):

    # Discount Tests
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(1000, 10), 900.0)

    def test_invalid_discount(self):
        self.assertEqual(calculate_discount(1000, 110), "Invalid discount")

    # Price Comparison Tests
    def test_compare_prices_cheaper(self):
        self.assertEqual(compare_prices(100, 200), "Product 1 is cheaper")

    def test_compare_prices_equal(self):
        self.assertEqual(compare_prices(100, 100), "Both are equal")

    # Deal Detection Tests
    def test_good_deal(self):
        self.assertEqual(is_good_deal(700, 1000), "Good deal")

    def test_not_good_deal(self):
        self.assertEqual(is_good_deal(950, 1000), "Not a good deal")

    # Coupon Tests
    def test_valid_coupon(self):
        self.assertEqual(apply_coupon(1000, "SAVE10"), 900.0)

    def test_invalid_coupon(self):
        self.assertEqual(apply_coupon(1000, "INVALID"), "Invalid coupon")

if __name__ == '__main__':
    unittest.main()
```

---

### `requirements.txt`
```
pytest
