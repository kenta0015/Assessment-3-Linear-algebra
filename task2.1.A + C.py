import numpy as np

def add_matrices(A, C):
    # Get the dimensions of matrix A
    m, n = A.shape
    # Initialize the result matrix D with zeros
    D = np.zeros((m, n))
    # Loop through each element of the matrices
    for i in range(m):
        for j in range(n):
            # Add corresponding elements of A and C
            D[i, j] = A[i, j] + C[i, j]
    return D

# Example usage
A = np.array([[1, 2], [3, 4]])  # Define matrix A
C = np.array([[5, 6], [7, 8]])  # Define matrix C
D = add_matrices(A, C)          # Call the function to add matrices
print(D)                        # Print the result
