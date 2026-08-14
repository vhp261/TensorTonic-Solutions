import numpy as np

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    # Write code here
    dz = dh * (1-np.array(cache[2])**2)
    dx_t = np.array(cache[3]).T @ dz
    dh_prev = np.array(cache[4]).T @ dz
    dW = np.outer(dz, np.array(cache[0]))
    dU = np.outer(dz, np.array(cache[1]))
    db = dz
    return (dx_t, dh_prev, dW, dU, db)
    
