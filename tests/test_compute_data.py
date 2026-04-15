"""Tests for compute_data_class.py."""

import numpy as np
from unittest.mock import Mock, patch

from inflammation.compute_data_class import analyse_data


def test_analyse_data():
    """Test that analyse_data runs correctly when passed a data source."""

    mock_data_source = Mock()

    mock_data_source.load_inflammation_data.return_value = [
        np.array([[1, 2, 3],
                  [4, 5, 6]]),
        np.array([[1, 2, 3],
                  [4, 5, 6]])
    ]

    with patch("inflammation.compute_data_class.views.visualize") as mock_visualize:
        analyse_data(mock_data_source)

        mock_data_source.load_inflammation_data.assert_called_once()
        mock_visualize.assert_called_once()