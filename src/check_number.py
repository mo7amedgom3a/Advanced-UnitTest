def is_even(n):
    if type(n) != int:
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be non-zero 🥵")
    return n % 2 == 0

def is_odd(n):
    if type(n) != int:
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be non-zero 🥵")

    return n % 2 != 0
