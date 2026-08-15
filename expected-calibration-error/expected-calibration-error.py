import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    n = len(y_true)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    starts = np.linspace(0, 1, n_bins, False)
    step_size = 1/n_bins
    ece = 0
    for l in starts:
        indices = (y_pred >= l) & (y_pred < l+step_size)
        bm = indices.sum()
        ece += bm/n * abs(1/bm * y_true[indices].sum() - 1/bm * y_pred[indices].sum())
    return ece