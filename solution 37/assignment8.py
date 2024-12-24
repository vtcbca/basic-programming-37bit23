def print_alphabet_recursive(n, i=0):
    if i == n:
        return
    
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print increasing part (letters from A to the i-th letter)
    for j in range(i + 1):
        print(chr(65 + j), end=" ")

    # Print decreasing part (letters from (i-1) to A)
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")

    # Move to the next line
    print()

    # Recursive call for the next row
    print_alphabet_recursive(n, i + 1)

# usage:
n = 3
print_alphabet_recursive(n)