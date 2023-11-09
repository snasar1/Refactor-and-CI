def nth_bit_adder(a, b):
    result = []  # Initialize the result as an empty list
    carry = 0  # Initialize the carry as 0

    max_len = max(len(a), len(b))  # Find the maximum length of the input strings
    a = a.zfill(max_len)  # Zero-fill 'a' to match the maximum length
    b = b.zfill(max_len)  # Zero-fill 'b' to match the maximum length

    # Iterate through each bit (from right to left)
    for i in range(max_len - 1, -1, -1):
        carry, bit = adder(int(a[i]), int(b[i]), carry)
        result.insert(0, bit)  # Insert the bit at the beginning of the result

    if carry:
        result.insert(0, carry)  # If there's a final carry, insert it at the beginning

    return result

def adder(a, b, carry=0):
    # Implement the one-bit adder logic here
    total = a ^ b ^ carry
    carry_out = (a & b) | (b & carry) | (a & carry)
    return carry_out, total
