import numpy as np

def multiply_matrices(A, B):
    # Get the dimensions of matrices A and B
    m, n = A.shape
    n, k = B.shape
    # Initialize the result matrix E with zeros
    E = np.zeros((m, k))
    # Loop through each element of the resulting matrix
    for i in range(m):
        for j in range(k):
            # Compute the dot product of the i-th row of A and j-th column of B
            for l in range(n):
                E[i, j] += A[i, l] * B[l, j]
    return E

# Example usage
A = np.array([[1, 2], [3, 4]])  # Define matrix A
B = np.array([[5, 6], [7, 8]])  # Define matrix B
E = multiply_matrices(A, B)     # Call the function to multiply matrices
print(E)                        # Print the result
