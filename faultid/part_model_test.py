import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from unittest.mock import MagicMock, patch
from models.part_model import PartModel


@pytest.fixture
def mock_client():
    return MagicMock()


@pytest.fixture
def mock_query_master():
    return MagicMock()


@pytest.fixture
def mock_observer_model():
    mock = MagicMock()
    mock.attach = MagicMock()
    return mock


@pytest.fixture
def part_model(mock_client, mock_query_master, mock_observer_model):
    return PartModel(mock_client, mock_query_master, mock_observer_model)


def test_initialization(part_model, ):
    assert part_model.serials == []
    assert part_model.locations == []
    assert part_model.timeframes is None
    assert part_model.plot_timeframe == 8
    assert part_model.limit_threshold == 0.05
    assert part_model.outlier_sensitivity_levels_input == 1.5
    assert part_model.outlier_sensitivity_levels_other == 1.5


def test_get_limit_threshold(part_model):
    assert part_model.get_limit_threshold() == 0.05


def test_get_plot_timeframe(part_model):
    assert part_model.get_plot_timeframe() == 8


def test_get_outlier_sensitivity_levels_input(part_model):
    assert part_model.get_outlier_sensitivity_levels_input() == 1.5


def test_get_outlier_sensitivity_levels_other(part_model):
    assert part_model.get_outlier_sensitivity_levels_other() == 1.5


def test_set_serials(part_model):
    serials = ['12345', '67890']
    part_model.set_serials(serials)
    assert part_model.serials == serials


def test_setup_locations(part_model, mock_client, mock_query_master):
    serials = ['12345', '67890']
    part_model.set_serials(serials)
    mock_query_master.get_stations_query.return_value = 'query'
    mock_client.execute_query.return_value = pd.DataFrame(
        {'name': ['Station1', 'Station2']})

    part_model.setup_locations()

    assert part_model.locations == ['Station1', 'Station2']


def test_get_parameters(part_model, mock_client, mock_query_master):
    serials = ['12345', '67890']
    station = 'Station1'
    mock_query_master.get_parameters_query.return_value = 'query'
    mock_client.execute_query.return_value = pd.DataFrame({
        'name': ['Param1', 'Param2'],
        'value': [1.0, 2.0],
        'lower_limit': [0.5, 1.5],
        'upper_limit': [1.5, 2.5],
        'unit_serial_number': ['12345', '67890']
    })

    result = part_model.get_parameters(serials, station)
    assert not result.empty


def test_pivot_table_for_matrix(part_model):
    data = pd.DataFrame({
        'name': ['Param1', 'Param2'],
        'value': [1.0, 2.0],
        'lower_limit': [0.5, 1.5],
        'upper_limit': [1.5, 2.5],
        'unit_serial_number': ['12345', '67890']
    })
    pivoted_data = part_model.pivot_table_for_matrix(data)
    assert not pivoted_data.empty


def test_pivot_table_for_scatter_plot(part_model):
    data = pd.DataFrame({
        'unit_serial_number': ['12345', '67890'],
        'name': ['Param1', 'Param2'],
        'value': [1.0, 2.0],
        'created_at': [datetime.now(), datetime.now()]
    })
    scatter_plot_data = part_model.pivot_table_for_scatter_plot(data)
    assert not scatter_plot_data.empty


def test_calculate_mahalanobis_distances(part_model):
    blue_points = np.array([[1, 2], [3, 4], [5, 6], [6, 8], [7, 9]])
    red_outlier_points = np.array([[2, 3], [4, 5], [5, 7]])

    distances = part_model.calculate_mahalanobis_distances(
        blue_points, red_outlier_points)
    assert distances.shape == (len(blue_points), len(red_outlier_points))

# Add more tests for other methods


if __name__ == '__main__':
    pytest.main()
