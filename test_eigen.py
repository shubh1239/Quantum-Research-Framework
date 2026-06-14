import numpy as np 
A = np.array([[1,2],[2,1]])
eigenvalues , eigenvectors = np.linalg.eig(A)
print("Derived Eigenvalues (The energy scales):", eigenvalues)
print("\nCorresponding Eigenvectors (The stable vectors):\n", eigenvectors)
