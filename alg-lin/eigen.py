import numpy as np

# Define the matrix
A = np.array([[2, 1],
              [1, 2]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)