# Explanation:
Import NumPy: This library provides powerful numerical operations, including linear algebra functions.
Define the Matrix: Create a NumPy array to represent the matrix A.
Find Eigenvalues and Eigenvectors: Use the np.linalg.eig() function to calculate the eigenvalues and eigenvectors of the matrix A.
Print Results: Print the calculated eigenvalues and eigenvectors.

Output:
Eigenvalues: [3. 1.]
Eigenvectors: [[ 0.70710678 -0.70710678]
                [ 0.70710678  0.70710678]]


# Additional Considerations:
Complex Eigenvalues: For matrices with complex eigenvalues, the np.linalg.eig() function will return complex values.
Numerical Stability: For large matrices or matrices with ill-conditioned eigenvalue problems, consider using more advanced numerical methods or libraries like SciPy.
Visualization: You can visualize the eigenvectors as vectors in the 2D plane to gain a better understanding of their geometric interpretation.
By understanding the basic concepts and utilizing powerful libraries like NumPy, you can efficiently compute eigenvalues and eigenvectors in Python.

