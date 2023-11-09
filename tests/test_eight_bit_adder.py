from my_package.logic_gates.eight_bit_adder import eight_bit_adder

def test_eight_bit_adder():
    # Test case 1: Adding two zeros
    result = eight_bit_adder("00000000", "00000000")
    assert result == [0, 0, 0, 0, 0, 0, 0, 0]

    # Test case 2: Adding two ones
    result = eight_bit_adder("11111111", "11111111")
    assert result == [1, 1, 1, 1, 1, 1, 1, 1]

    # Test case 3: Adding 5 and 3 (binary: 0101 + 0011)
    result = eight_bit_adder("00000101", "00000011")
    assert result == [0, 0, 0, 0, 0, 1, 0, 0]

    # Add more test cases here

if __name__ == "__main__":
    test_eight_bit_adder()
