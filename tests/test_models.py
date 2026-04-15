"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, patient_normalise

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_patient_normalise():
    """Test that normalisation function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([[-1.225, -1.225],
                            [0, 0],
                            [1.225, 1.225]])

# x mean=μ: 3, x standard deviation=σ: 1.63299316


    # Need to use Numpy testing functions to compare arrays
    # npt.assert_array_equal(patient_normalise(test_input), test_result)
    npt.assert_allclose(patient_normalise(test_input), test_result, rtol=1e-3)