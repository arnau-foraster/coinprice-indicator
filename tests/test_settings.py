# -*- coding: utf-8 -*-
from coin import settings
from coin import utils

import unittest


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.settings = settings.Settings()

    def test_decimal_round_int(self):
        result = utils.decimal_round(1)
        self.assertEqual(result, '1.00')
