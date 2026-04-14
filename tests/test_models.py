"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
import pytest

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

def test_daily_mean_floats():
    """Test that mean function works for an array of positive floats."""

    test_input = np.array([[1.5, 2.5],
                           [3.5, 4.5],
                           [5.5, 6.5]])
    test_result = np.array([3.5, 4.5])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_mixed():
    """Test that mean function works for an array of mixed integers and floats."""

    test_input = np.array([[1, 2.5],
                           [3, 4.5],
                           [5, 6.5]])
    test_result = np.array([3, 4.5])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_negatives():
    """Test that mean function works for an array of negative integers."""

    test_input = np.array([[-1, -2],
                           [-3, -4],
                           [-5, -6]])
    test_result = np.array([-3, -4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize("test_input, test_result", [
    (np.array([[1, 2], [3, 4], [5, 6]]), np.array([3, 4])),
    (np.array([[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]]), np.array([3.5, 4.5])),
    (np.array([[1, 2.5], [3, 4.5], [5, 6.5]]), np.array([3, 4.5])),
    (np.array([[-1, -2], [-3, -4], [-5, -6]]), np.array([-3, -4]))
])
def test_daily_mean_parametrize(test_input, test_result):
    """Test that mean function works for a variety of inputs using parametrize."""

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)     


