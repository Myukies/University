import numpy as np

print("Basic Matrix Operations:")
print()

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[9, 8],
              [6, 5]])

matrix_addition = A + B
matrix_subtraction = A - B
matrix_multiplication = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nMatrix Addition:\n", matrix_addition)
print("\nMatrix Subtraction:\n", matrix_subtraction)
print("\nMatrix Multiplication:\n", matrix_multiplication)

print()
print()

def is_invertible(matrix):
    return np.linalg.det(matrix) != 0

def calculate_inverse(matrix):
    return np.linalg.inv(matrix)

if is_invertible(A):
    inverse_A = calculate_inverse(A)
    print("Matrix A is invertible.")
    print("Inverse of matrix A:")
    print(inverse_A)
else:
    print("Matrix A is not invertible.")


