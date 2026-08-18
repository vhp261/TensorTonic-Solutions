import numpy as np
import numpy.linalg as la

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    return la.trace(A)
