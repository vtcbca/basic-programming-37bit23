def print_triangle_map_join(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Create the sequence of numbers for this row using map and join
        print(" ".join(map(str, range(1, 2 * i))), end="")
        print()  # Move to the next line

# Example
print_triangle_map_join(3)
