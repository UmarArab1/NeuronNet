import numpy as np

def generate_random_data(n_samples, n_features):
    return np.random.randn(n_samples, n_features)

def generate_random_labels(n_samples, n_outputs):
    return np.random.randn(n_samples, n_outputs)
