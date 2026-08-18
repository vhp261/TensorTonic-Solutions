import numpy as np
import numpy.linalg as la

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    if la.det(A)==0:
        return None
    return la.inv(A)