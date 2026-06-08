import numpy as np

matrix_a=np.array([[1,2],
                  [3,4]])

matrix_b=np.array([[[5,6],
                   [7,8]]])

print(matrix_a)
print(matrix_b)

print("\nSum of matrix:\n",matrix_a + matrix_b)

print("\nDifference of matrix:\n",matrix_a - matrix_b)

print("\nMultiplication of matrix:\n",matrix_a @ matrix_b)

print("\nTranspose of matrix A:\n",matrix_a.T)
print("\nTranspose of matrix B:\n",matrix_b.T)

print("\nInverse of matrix A:\n",np.linalg.inv(matrix_a))
print("\nDeterminent of matrix A:\n",np.linalg.det(matrix_a))