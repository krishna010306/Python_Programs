import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for Matrix 1:")
matrix1 = np.array([[int(input()) for _ in range(cols)] for _ in range(rows)])

print("Enter elements for Matrix 2:")
matrix2 = np.array([[int(input()) for _ in range(cols)] for _ in range(rows)])

print("\nMatrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print("\nAddition of matrices:")
print(matrix1 + matrix2)

print("\nSubtraction of matrices:")
print(matrix1 - matrix2)

print("\nElement-wise Multiplication of matrices:")
print(matrix1 * matrix2)

with np.errstate(divide='ignore', invalid='ignore'):
    division = np.divide(matrix1, matrix2)

    division[matrix2 == 0] = 0

print("\nElement-wise Division of matrices:")
print(division)