# Import necessary modules and classes
import unittest
from my_package.logic_gates.nth_bit_adder import nth_bit_adder

class TestNthBitAdder(unittest.TestCase):
    def test_addition(self):
        # Test cases for binary addition

        # Test adding two binary numbers of the same length
        result = nth_bit_adder("1101", "1011")
        self.assertEqual(result, [1, 1, 1, 0, 0], "Incorrect addition for equal-length binary numbers")

        # Test adding two binary numbers of different lengths
        result = nth_bit_adder("110", "10101")
        self.assertEqual(result, [1, 1, 0, 0, 0, 1], "Incorrect addition for different-length binary numbers")

        # Test adding binary numbers with a final carry
        result = nth_bit_adder("1111", "1111")
        self.assertEqual(result, [1, 1, 1, 1, 1], "Incorrect addition with a final carry")

    def test_zero_fill(self):
        # Test zero-filling behavior

        # Test zero-filling for numbers of different lengths
        result = nth_bit_adder("101", "11")
        self.assertEqual(result, [1, 0, 1, 0], "Zero-filling behavior is incorrect")

if __name__ == '__main__':
    unittest.main()
