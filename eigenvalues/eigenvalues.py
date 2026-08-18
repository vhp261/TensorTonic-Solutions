import numpy as np
import numpy.linalg as la

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix=np.array(matrix)
    except:
        return None
    if matrix.ndim < 2 or matrix.shape[0]!=matrix.shape[1]:
        return None
    eivals, eivecs = la.eig(matrix)
    return eivals