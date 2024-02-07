def rectangular_multiplication(a, b):
    # Convert multiplicands to strings for easy iteration
    a_str = str(abs(a))
    b_str = str(abs(b))

    # Initialize the grid with zeros
    grid = [[0] * (len(b_str) + len(a_str) - 1) for _ in range(len(a_str))]

    # Populate the grid with products of individual digits
    for i in range(len(a_str)):
        for j in range(len(b_str)):
            grid[i][i + j] = int(a_str[i]) * int(b_str[j])

    # Sum the diagonals to get the result
    result = [sum(row[i] for row in grid if i < len(row))
              for i in range(len(grid[0]))]

    # Handle carries
    carry = 0
    for i in range(len(result) - 1, -1, -1):
        temp_sum = result[i] + carry
        result[i] = temp_sum % 10
        carry = temp_sum // 10

    # Handle the last carry
    while carry:
        result.insert(0, carry % 10)
        carry //= 10

    result_str = ''.join(map(str, result)).lstrip('0') or '0'

    # Determine the sign of the result
    result_sign = '-' if (a < 0) ^ (b < 0) else ''

    return result_sign + result_str


# Test cases
test_cases = [
    (7000, 7294),
    (25, 5038385),
    (-59724, 783),
    (8516, -82147953548159344),
    (45952456856498465985, 98654651986546519856),
    (-45952456856498465985, -98654651986546519856)
]

for case in test_cases:
    result = rectangular_multiplication(case[0], case[1])
    print(f"{case[0]} * {case[1]} = {result}")
