import numpy as np

def fibonacci_matrix(n):
    F = np.matrix([[1, 1], [1, 0]])
    result = []
    for i in range(n):
        fib_i = np.linalg.matrix_power(F, i)[0, 1]
        result.append(fib_i)
    return result

# Example usage:
print(fibonacci_matrix(10))