import pandas as pd

import numpy.testing as npt

from inflammation.models import load_csv
import pytest
def test_daily_mean():
    """Test that mean function works for an array."""
    test_input = pd.DataFrame([[0, 0],
                               [3, 40],
                               [0, 5]])
    test_result = np.array([1, 15])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(load_csv(test_input), test_result)