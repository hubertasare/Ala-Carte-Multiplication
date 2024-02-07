def ala_carte_multiplication(a, b):
    # Check the signs of the multiplicands and multipliers
    sign_a = 1 if a >= 0 else -1
    sign_b = 1 if b >= 0 else -1

    # Take the absolute values for the calculation
    abs_a = abs(a)
    abs_b = abs(b)

    # Perform the Ala Carte multiplication
    result = 0
    while abs_b > 0:
        if abs_b % 2 == 1:
            result += abs_a
        abs_a <<= 1  # Left shift is equivalent to multiplying by 2
        abs_b >>= 1  # Right shift is equivalent to dividing by 2

    # Apply the signs to the result
    result *= sign_a * sign_b

    return result


# Test cases
print("Test Case 1:", ala_carte_multiplication(7000, 7294))
print("Test Case 2:", ala_carte_multiplication(25, 5038385))
print("Test Case 3:", ala_carte_multiplication(-59724, 783))
print("Test Case 4:", ala_carte_multiplication(8516, -82147953548159344))
print("Test Case 5:", ala_carte_multiplication(
    45952456856498465985, 98654651986546519856))
print("Test Case 6:",
      ala_carte_multiplication(-45952456856498465985, -98654651986546519856))
