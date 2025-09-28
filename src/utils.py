import os

def ensure_dirs(directories):
    """
    Ensure directories exist.
    """
    for d in directories:
        if not os.path.exists(d):
            os.makedirs(d)
