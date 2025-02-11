from numeralconverter.roman_convertion import from_roman, to_roman
import unittest

ROMAN_NUMERALS = {
'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
}   
class TestRomanConversion(unittest.TestCase):

    def test_single_numerals(self):
        # Basic numerals
        self.assertEqual(from_roman('I'), 1, "Failed on 'I'")
        self.assertEqual(from_roman('V'), 5, "Failed on 'V'")
        self.assertEqual(from_roman('X'), 10, "Failed on 'X'")
        self.assertEqual(from_roman('L'), 50, "Failed on 'L'")
        self.assertEqual(from_roman('C'), 100, "Failed on 'C'")
        self.assertEqual(from_roman('D'), 500, "Failed on 'D'")
        self.assertEqual(from_roman('M'), 1000, "Failed on 'M'")

    def test_repeating_numerals(self):
        # Repeating numerals (valid scenarios)
        self.assertEqual(from_roman('III'), 3, "Failed on 'III'")
        self.assertEqual(from_roman('XXX'), 30, "Failed on 'XXX'")
        self.assertEqual(from_roman('CCC'), 300, "Failed on 'CCC'")
        self.assertEqual(from_roman('MMM'), 3000, "Failed on 'MMM'")

    def test_subtractive_notation(self):
        # Subtractive combinations
        self.assertEqual(from_roman('IV'), 4, "Failed on 'IV'")
        self.assertEqual(from_roman('IX'), 9, "Failed on 'IX'")
        self.assertEqual(from_roman('XL'), 40, "Failed on 'XL'")
        self.assertEqual(from_roman('XC'), 90, "Failed on 'XC'")
        self.assertEqual(from_roman('CD'), 400, "Failed on 'CD'")
        self.assertEqual(from_roman('CM'), 900, "Failed on 'CM'")

    def test_combined_numerals(self):
        # Combinations of numerals
        self.assertEqual(from_roman('XIII'), 13, "Failed on 'XIII'")
        self.assertEqual(from_roman('XXIV'), 24, "Failed on 'XXIV'")
        self.assertEqual(from_roman('XCIX'), 99, "Failed on 'XCIX'")
        self.assertEqual(from_roman('DCCC'), 800, "Failed on 'DCCC'")
        self.assertEqual(from_roman('MCMXCIV'), 1994, "Failed on 'MCMXCIV'")
        self.assertEqual(from_roman('MMXXIV'), 2024, "Failed on 'MMXXIV'")

    def test_large_numerals(self):
        # Larger numbers
        with self.assertRaises(ValueError, msg="Failed on 'MMMM'"):
            from_roman('MMMM')
        with self.assertRaises(ValueError, msg="Failed on 'MMMMCMXCIX"):
            from_roman('MMMMCMXCIX')

    def test_large_input_efficiency(self):
        with self.assertRaises(ValueError, msg="Failed on edge case: VALUE TOO BIG"):
            from_roman('MMMMCMXCIX')

    def test_single_digit(self):
        # Testing single digits
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(5), "V")
        self.assertEqual(to_roman(9), "IX")

    def test_two_digits(self):
        # Testing two-digit numbers
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(50), "L")
        self.assertEqual(to_roman(90), "XC")

    def test_three_digits(self):
        # Testing three-digit numbers
        self.assertEqual(to_roman(100), "C")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(500), "D")
        self.assertEqual(to_roman(900), "CM")

    def test_combined_numbers(self):
        # Testing numbers with mixed Roman numeral rules
        self.assertEqual(to_roman(6), "VI")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(44), "XLIV")
        self.assertEqual(to_roman(99), "XCIX")
        self.assertEqual(to_roman(399), "CCCXCIX")

    def test_large_numbers(self):
        # Testing large numbers
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(1987), "MCMLXXXVII")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    # ERROR TESTING
    def test_large_input(self):
    # Testing large Roman numerals to check performance
        long_roman = 'M' * 1000  # 1000 times 'M'
        with self.assertRaises(ValueError, msg="Failed on edge case: VALUE TOO BIG"):
            from_roman(long_roman)

    def test_valid_subtractive_pairs(self):
        # Test valid subtractive pairs
        valid_pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        answers = [4, 9, 40, 90, 400, 900]
        for pos, pair in enumerate(valid_pairs):
            self.assertEqual(from_roman(pair),answers[pos] ,f"Failed on valid pair: {pair}")

    def test_invalid_subtractive_pairs(self):
        # Test invalid subtractive pairs
        invalid_pairs = ['IC', 'IL', 'ID', 'IM', 'VV', 'LL', 'DD', 'IIII', 'IIIIII']
        for pair in invalid_pairs:
            with self.assertRaises(ValueError, msg=f"Failed on invalid pair: {pair}"):
                from_roman(pair)

    def test_edge_cases(self):
        # Test edge cases
        self.assertTrue(from_roman('III'), "Failed on valid case: III should be valid")
        with self.assertRaises(ValueError, msg="Failed on edge case: VV should not be valid"):
            from_roman('VV')
        self.assertTrue(from_roman('IX'), "Failed on valid pair: IX")
        self.assertTrue(from_roman('XL'), "Failed on valid pair: XL")
        with self.assertRaises(ValueError, msg="Failed on invalid case: IC should be invalid"):
            from_roman('IC')

    def test_long_valid_roman_numerals(self):
        # Test longer valid Roman numerals
        self.assertTrue(from_roman('MCMXCIV'), "Failed on valid case: MCMXCIV should be valid")
        self.assertTrue(from_roman('MMMDCCCLXXXVIII'), "Failed on valid case: MMMDCCCLXXXVIII should be valid")

    def test_non_subtractive_numerals(self):
        # Test non-subtractive numerals
        self.assertTrue(from_roman('VII'), "Failed on valid case: VII should be valid")
        self.assertTrue(from_roman('XIV'), "Failed on valid case: XIV should be valid")

    def test_invalid_order(self):
        # Test invalid Roman numerals in order
        with self.assertRaises(ValueError, msg="Failed on invalid case: IXI should be invalid"):
            from_roman('IXI')
        with self.assertRaises(ValueError, msg="Failed on invalid case: VV should be invalid"):
            from_roman('VV')

    # EDGE CASES
    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Failed on empty string input"):
            from_roman('')
    def test_zero(self):
        with self.assertRaises(ValueError, msg="Failed on zero input"):
            from_roman('0')
    def test_negative_numbers(self):
        with self.assertRaises(ValueError, msg="Failed on negative number input"):
            from_roman('-IX')
    def test_invalid_characters(self):
        with self.assertRaises(ValueError, msg="Failed on invalid character input"):
            from_roman('AIV')
    def test_large_roman_numerals(self):
        with self.assertRaises(ValueError, msg="Failed on invalid large Roman numeral input"):
            from_roman('MMMMMMMM')
    def test_very_large_input(self):
        # Test a Roman numeral that is very large, e.g., a string of 1000 'M's.
        long_roman = 'M' * 1000
        with self.assertRaises(ValueError, msg="Failed on performance test for large input"):
            from_roman(long_roman)
    def test_invalid_subtractive_mixed(self):
        with self.assertRaises(ValueError, msg="Failed on invalid subtractive notation input"):
            from_roman('IC')
    def test_to_roman_invalid(self):
        with self.assertRaises(ValueError, msg="Failed on invalid input for to_roman"):
            to_roman(-1)  # Negative number
        with self.assertRaises(ValueError, msg="Failed on invalid input for to_roman"):
            to_roman(0)   # Zero
    def test_to_roman_zero(self):
        with self.assertRaises(ValueError, msg="Failed on zero input for to_roman"):
            to_roman(0)
    def test_large_number_to_roman(self):
        self.assertEqual(to_roman(3999), 'MMMCMXCIX', msg="Failed on large number conversion")
    def test_multiple_invalid_characters(self):
        with self.assertRaises(ValueError, msg="Failed on invalid Roman numeral 'VV'"):
            from_roman('VV')
    def test_mixed_order(self):
        with self.assertRaises(ValueError, msg="Failed on mixed order 'IXI'"):
            from_roman('IXI')
    def test_boundary_case_IIII(self):
        with self.assertRaises(ValueError, msg="Failed on invalid Roman numeral 'IIII'"):
            from_roman('IIII')
    def test_decimal_values(self):
        with self.assertRaises(ValueError, msg="Failed on invalid Roman numeral 'IIII'"):
            to_roman(3.14)

if __name__ == '__main__':
    unittest.main()