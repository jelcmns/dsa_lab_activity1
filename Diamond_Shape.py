def print_diamond(n):
    # Ask the user to input an odd interger, if n is even, print a message and exit the function
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return

    # Top half including the middle row of the diamond
    for i in range(n // 2 + 1):
        # Print spaces to center the stars, then print stars in increasing numbers
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

    # Bottom half of the diamond
    for i in range(n // 2 - 1, -1, -1):
        # Print spaces to center the stars, then print stars in decreasing numbers
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


# Example usage. Prompt user for input
n = int(input("Enter an odd integer: "))
print_diamond(n)