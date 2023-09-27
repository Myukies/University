import numpy as np

a = np.mat("7 3; 3 -1")
print("Matrix a:")
print()
print(a)

eigenvalues = np.linalg.eigvals(a)
print("\nEigenvalues of a:", eigenvalues)

eigenvalues, eigenvectors = np.linalg.eig(a)
print("\nEigenvectors of a:")
print(eigenvalues, eigenvectors)

