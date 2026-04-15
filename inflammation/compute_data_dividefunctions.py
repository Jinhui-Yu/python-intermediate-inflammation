"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

def load_inflammation_data(data_dir):
    """Load inflammation data from all matching CSV files in a directory.

    Parameters
    ----------
    data_dir : str
        Path to the directory containing inflammation CSV files.

    Returns
    -------
    list of numpy.ndarray
        A list of 2D NumPy arrays, one per inflammation CSV file.
    """
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")

    data = [models.load_csv(path) for path in data_file_paths]
    return data


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means.
    """
    data = load_inflammation_data(data_dir)

    means_by_day = [models.daily_mean(dataset) for dataset in data]
    means_by_day_matrix = np.stack(means_by_day)

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)


def main():
    pass