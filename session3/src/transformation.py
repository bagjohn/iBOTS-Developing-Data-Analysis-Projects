import numpy as np

def normalize(a):
    return (a-np.min(a))/(np.max(a)-np.min(a))

def standardize(a):
    return (a - np.mean(a)) / np.std(a)