#!/usr/bin/env python3

import unittest

from sample.enums import unit

class TestUnitConvertor(unittest.TestCase):

    def test_unit_convert_in_pounds(self):
        weight_in_kg = 1
        weight_in_lbs = unit.convert(weight_in_kg, unit.Unit.POUNDS)
        self.assertEqual(weight_in_lbs, 2.2046)

    def test_unit_convert_in_kilograms(self):
        weight_in_lbs = 1
        weight_in_kg = unit.convert(weight_in_lbs, unit.Unit.KILOGRAMS)
        self.assertEqual(float(f'{weight_in_kg:.6f}'), 0.453597)

    def test_unit_wrong_unit(self):
        with self.assertRaises(TypeError):
            unit.convert(0, None)

if __name__ == '__main__':
    unittest.main()