# Math operators
# 3 + 4
# 7 - 4
# 3 * 2
# 6 / 3     # Division which results to a float data type
# 2 ** 2    # Exponents 2^2

# Order of operations is PEMDAS
# ( ) Paranthesis
# **  Exponents
# *   Multiplication
# /   Division
# +   Addition
# -   Subtraction

result = 3 - 3 * (1 + 2 ** 2) / 5 + 2
# PEMDAS
# result = 3 - 3 * (1 + 2 ** 2) / 5 + 2
# result = 3 - 3 * (1 + 4) / 5 + 2
# result = 3 - 3 * 5 / 5 + 2
# result = 3 - 15 / 5 + 2
# result = 3 - 3.0 + 2  Note: Division results to float
# result = 3 - 5.0
# result = 3 - 1.0
# result = 2.0

print(result)

# Change so it outputs 3.0 instead of 7.0
# 7.0 --> print(3 * 3 + 3 / 3 - 3)
print(3 * ( 3 + 3 ) / 3 - 3)