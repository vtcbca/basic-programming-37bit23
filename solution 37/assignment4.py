from functools import reduce

def reverse_string_reduce(s):
    return reduce(lambda x, y: y + x, s)

# Example usage:
input_string = "hello"
print(reverse_string_reduce(input_string))
