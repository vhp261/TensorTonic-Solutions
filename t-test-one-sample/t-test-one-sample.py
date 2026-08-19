import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    n=len(x)
    x = np.array(x)
    x_hat = x.mean()
    x = (x-x_hat)**2
    s = np.sqrt(1/(n-1)*x.sum())
    t = (x_hat-mu0)/(s/np.sqrt(n))
    return t