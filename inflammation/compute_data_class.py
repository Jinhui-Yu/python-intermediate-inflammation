"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class CSVDataSource:
    """Data source for loading inflammation data from CSV files."""

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")

        data = [models.load_csv(path) for path in data_file_paths]
        return data


def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets."""
    data = data_source.load_inflammation_data()

    means_by_day = [models.daily_mean(dataset) for dataset in data]
    means_by_day_matrix = np.stack(means_by_day)

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)


def main():
    data_dir = "data"
    data_source = CSVDataSource(data_dir)
    analyse_data(data_source)


if __name__ == "__main__":
    main()