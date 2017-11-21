# -*- coding: utf-8 -*-
from coin import utils

import unittest


class UtilsTests(unittest.TestCase):
    def test_decimal_round_int(self):
        result = utils.decimal_round(1)
        self.assertEqual(result, '1.00')

    def test_decimal_rount_type(self):
        result = utils.decimal_round(2.99)
        self.assertEqual(type(result), str)

    def test_currency_eur(self):
        result = utils.currency['eur']
        self.assertEqual(result, '€')

    def test_currency_usd(self):
        result = utils.currency['usd']
        self.assertEqual(result, '$')
