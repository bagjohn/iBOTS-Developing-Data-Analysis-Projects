

def plot_histogram(data, nbins=20):
    import numpy as np
    import matplotlib.pyplot as plt
    figure, ax = plt.subplots(ncols=1, nrows=1)
    ax.hist(data, bins=nbins);