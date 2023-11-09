def eight_bit_adder(a, b):
    total = [0] * 8  # Initialize the result as an eight-element list of zeros
    carry = 0  # Initialize the carry as 0

    # Iterate through each bit (from right to left)
    for i in range(7, -1, -1):
        carry, total[i] = adder(int(a[i]), int(b[i]), carry)

    return carry, total
