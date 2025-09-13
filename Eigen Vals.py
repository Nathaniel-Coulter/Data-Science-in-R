import numpy as np
# matrix A
A = np.array([[1, 1, 0],
              [1, 2, 3],
              [0, 3, 2]])

# eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# matrix P from the eigenvectors
P = eigenvectors

# inverse of P
P_inv = np.linalg.inv(P)

# Diagonalize matrix A
A_diagonal = P_inv @ A @ P

# trace of the diagonalized matrix
trace_diagonal = np.trace(A_diagonal)

# print it all neat 
print("Eigenvalues of A:")
print(eigenvalues)
print("\nEigenvectors of A:")
print(eigenvectors)
print("\nMatrix P (formed from eigenvectors):")
print(P)
print("\nP^-1 A P (Diagonalized Matrix):")
print(A_diagonal)
print("\nTrace of the diagonalized matrix:")
print(trace_diagonal)

# relationship between trace and eigenvalues
print("\nNotice about the trace and eigenvalues:")
print("The trace of the diagonalized matrix is equal to the sum of the eigenvalues of the original matrix A.")s