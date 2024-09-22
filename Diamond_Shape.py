def print_diamond(n):
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return

    # Top half including the middle row
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

    # Bottom half
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


# Example usage
n = int(input("Enter an odd integer: "))
print_diamond(n)