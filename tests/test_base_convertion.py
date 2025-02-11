from numeralconverter import from_base, to_base
import unittest

class TestBaseConversion(unittest.TestCase):

    # ==========================
    # FROM BASE CONVERSIONS
    # ==========================

    # VALID CONVERSIONS
    def test_valid_conversions(self):
        conversions = [
            (10, 2, "1010"),           # Decimal 10 to Binary
            (10, 8, "12"),             # Decimal 10 to Octal
            (10, 16, "A"),             # Decimal 10 to Hexadecimal
            (255, 16, "FF"),           # Decimal 255 to Hexadecimal
            (255, 10, "255"),          # Decimal 255 to Decimal
            (255, 36, "73"),           # Decimal 255 to Base 36
            (1000, 62, "g8"),          # Decimal 1000 to Base 62
            (1000, 94, "aY"),          # Decimal 1000 to Base 94
            (703, 26, "BBB"),          # Base 26 (A-Z only) - Excel-style
        ]
        for decimal, base, expected in conversions:
            self.assertEqual(to_base(decimal, base), expected)

    # INVALID CONVERSIONS
    def test_invalid_conversions(self):
        invalid_cases = [
            (10, 1),                   # Base too low
            (10, 95),                  # Base too high
            (-10, 10),                 # Negative decimal
            (10, 2.5),                 # Non-integer base
            (10, "A"),                 # Non-integer base
            ("g", 16),                 # Invalid character for base 16
            ("z", 36),                 # Invalid character for base 36
            ("~", 62),                 # Invalid character for base 62
            (" ", 94),                 # Invalid character for base 94
            ("A1", 26),                # Base 26 should only have A-Z
        ]
        for value, base in invalid_cases:
            with self.assertRaises(ValueError):
                if isinstance(value, int):
                    to_base(value, base)
                else:
                    from_base(value, base)

    # EDGE CASES
    def test_edge_cases(self):
        self.assertEqual(to_base(0, 10), '0')  # Edge case for 0
        self.assertEqual(from_base("0", 10), 0)  # Edge case for 0

    def test_leading_zeros(self):
        self.assertEqual(to_base(10, 2), "1010")  # No leading zeros
        self.assertEqual(to_base(8, 8), "10")     # No leading zeros

    def test_large_numbers(self):
        self.assertEqual(to_base(2**63 - 1, 2), "1" * 63)  # Large number in binary
        self.assertEqual(to_base(2**63 - 1, 94), "g99f2RA^oz")    # Large number in base 94

    # ==========================
    # CHARACTER VALIDATION TESTS
    # ==========================

    def test_valid_character_set_in_to_base(self):
        """Ensure that to_base() only uses valid characters for each base."""
        bases_to_test = {
            2: "01",
            8: "01234567",
            10: "0123456789",
            16: "0123456789ABCDEF",
            26: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            36: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            62: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        }
        
        for base, valid_chars in bases_to_test.items():
            for num in range(min(1000, base**2)):  # Test a variety of values
                encoded = to_base(num, base)
                self.assertTrue(all(c in valid_chars for c in encoded), 
                                f"Invalid character in {encoded} for base {base}")

    def test_invalid_characters_raise_value_error(self):
        """Ensure that from_base() raises ValueError for invalid characters."""
        invalid_test_cases = {
            2: "2",          # 2 is not allowed in base 2
            8: "8",          # 8 is not allowed in base 8
            10: "A",         # A is not allowed in base 10
            16: "G",         # G is not allowed in base 16
            26: "1",         # Numbers are not allowed in base 26
            36: "!",         # Punctuation is not allowed in base 36
            62: "~",         # Special characters are not allowed in base 62
        }

        for base, invalid_str in invalid_test_cases.items():
            with self.assertRaises(ValueError, msg=f"Expected ValueError for {invalid_str} in base {base}"):
                from_base(invalid_str, base)


    def test_mixed_case_in_strict_bases(self):
        """Ensure bases with case-sensitive rules enforce them correctly."""
        invalid_cases = [
            ("a", 26),  # Base 26 should only allow uppercase A-Z
            ("a1", 36),  # Base 36 should use uppercase A-Z only
            ("A1`", 62),  # Base 62 allows a-z, but should be consistent
        ]
        for value, base in invalid_cases:
            with self.assertRaises(ValueError):
                from_base(value, base)

    # ==========================
    # TO BASE CONVERSIONS
    # ==========================

    def test_round_trip_consistency(self):
        for base in range(2, 95):
            for num in [0, 1, 10, 255, 1000, 12345, 2**20, 2**63 - 1]:
                encoded = to_base(num, base)  # Ensure the result is a string
                self.assertIsInstance(encoded, str, f"Expected string but got {type(encoded)} for base {base}")

                # Special handling for bases 17 to 26 (A = 0, B = 1, ..., Z = 25)
                if 17 <= base <= 26:
                    expected_num = num
                    decoded_num = from_base(encoded, base)
                    self.assertEqual(decoded_num, expected_num, f"Failed for base {base}: {encoded} -> {decoded_num}")
                else:
                    self.assertEqual(num, from_base(encoded, base))  # Convert back and compare


    def test_performance_large_number(self):
        """Test the function's performance with large numbers."""
        large_num = 10**18
        result = to_base(large_num, 94)
        self.assertEqual(from_base(result, 94), large_num)  # Verify correctness

if __name__ == '__main__':
    unittest.main()
