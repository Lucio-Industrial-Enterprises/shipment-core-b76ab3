import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        """Passing service="standard" must match the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------
    def test_express_local(self):
        """Express local = standard local + $7."""
        standard = shipping_quote(2, "local")
        express = shipping_quote(2, "local", service="express")
        self.assertAlmostEqual(express - standard, 7.0)
        self.assertEqual(express, 15.0)

    def test_express_regional(self):
        """Express regional = standard regional + $7."""
        standard = shipping_quote(2, "regional")
        express = shipping_quote(2, "regional", service="express")
        self.assertAlmostEqual(express - standard, 7.0)
        self.assertEqual(express, 18.0)

    def test_express_weight_scaling(self):
        """Weight-based component is still applied for express."""
        self.assertEqual(shipping_quote(10, "local", service="express"), 27.0)

    # ------------------------------------------------------------------
    # Unknown service rejection
    # ------------------------------------------------------------------
    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
