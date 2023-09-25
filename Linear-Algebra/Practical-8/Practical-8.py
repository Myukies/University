import numpy as np

a = np.mat("3 -2; 1 0")
print("Matrix a:")
print()
print(a)

eigenvalues = np.linalg.eigvals(a)
print("\nEigenvalues of a:", eigenvalues)

eigenvalues, eigenvectors = np.linalg.eig(a)
print("\nEigenvectors of a:")
print(eigenvalues, eigenvectors)

