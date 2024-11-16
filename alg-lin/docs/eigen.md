**Example Exam Question: Eigenvalues and Eigenvectors**

**Problem:**

Consider the matrix:

```
A = [[2, 1],
     [1, 2]]
```

1. **Find the eigenvalues of A.**
2. **For each eigenvalue, find a basis for the corresponding eigenspace.**
3. **Diagonalize A, if possible. If not, explain why.**

**Solution:**

1. **Finding Eigenvalues:**
   To find the eigenvalues, we need to solve the characteristic equation det(A - λI) = 0.
   
   ```
   det(A - λI) = det([[2-λ, 1],
                       [1, 2-λ]])
                   = (2-λ)^2 - 1
                   = λ^2 - 4λ + 3
                   = (λ-1)(λ-3)
   ```
   
   So, the eigenvalues are λ₁ = 1 and λ₂ = 3.

2. **Finding Eigenspaces:**
   
   * **For λ₁ = 1:**
     Solve the equation (A - I)v = 0:
     ```
     [[1, 1],
      [1, 1]] * [[x],
                  [y]] = [[0],
                           [0]]
     ```
     This leads to the equation x + y = 0. 
     A basis for the eigenspace corresponding to λ₁ = 1 is {(1, -1)}.

   * **For λ₂ = 3:**
     Solve the equation (A - 3I)v = 0:
     ```
     [[-1, 1],
      [1, -1]] * [[x],
                    [y]] = [[0],
                             [0]]
     ```
     This leads to the equation -x + y = 0. 
     A basis for the eigenspace corresponding to λ₂ = 3 is {(1, 1)}.

3. **Diagonalizing A:**
   Since A has two distinct eigenvalues and we found a basis for each eigenspace, A is diagonalizable. 
   We can diagonalize A as follows:
   
   ```
   A = PDP^(-1)
   ```
   
   where:
   
   * P = [[1, 1],
         [-1, 1]] (matrix of eigenvectors)
   * D = [[1, 0],
         [0, 3]] (diagonal matrix of eigenvalues)
   
   You can verify this by calculating P^(-1)AP.

**Additional Tips for Exam Preparation:**

* **Practice, Practice, Practice:** Solve numerous problems from textbooks and online resources.
* **Understand the Concepts:** Don't just memorize formulas. Understand the underlying concepts.
* **Learn Matrix Operations:** Be proficient in matrix addition, subtraction, multiplication, and inversion.
* **Master Determinant Calculation:** Practice calculating determinants of various sizes.
* **Review Linear Systems:** Understand how to solve linear systems of equations.
* **Study Diagonalization:** Know the conditions for diagonalization and how to find the diagonalizing matrix.
* **Utilize Technology:** Use software like MATLAB or Python to check your answers and visualize concepts.

By following these guidelines and practicing consistently, you can excel in your linear algebra exam.
