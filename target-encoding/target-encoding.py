import numpy as np 

def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code 
    categories = np.array(categories)
    out = np.zeros(len(categories))
    targets = np.array(targets)
    for c in categories:
        mask = categories==c
        avg = targets[mask].mean()
        out[mask]=avg
    return out.tolist()