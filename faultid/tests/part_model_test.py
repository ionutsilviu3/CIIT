import pytest
from unittest.mock import Mock
import pandas as pd
from ..models.part_model import PartModel

@pytest.fixture
def mock_objects():
    client = Mock()
    query_master = Mock()
    observer_model = Mock()
    return client, query_master, observer_model

@pytest.fixture
def part_model(mock_objects):
    client, query_master, observer_model = mock_objects
    return PartModel(client, query_master, observer_model)

def test_initialization(part_model):
    assert part_model.serials == []
    assert part_model.locations == []
    assert part_model.timeframes is None
    assert part_model.plot_timeframe == 8
    assert part_model.limit_threshold == 0.05
    assert part_model.outlier_sensitivity_levels_input == 1.5
    assert part_model.outlier_sensitivity_levels_other == 1.5
    assert not part_model.is_cache_invalid

def test_get_limit_threshold(part_model):
    assert part_model.get_limit_threshold() == 0.05

def test_get_plot_timeframe(part_model):
    assert part_model.get_plot_timeframe() == 8

def test_update(part_model, mock_objects):
    client, query_master, observer_model = mock_objects
    observer_model.settings = {
        "input_priority": "normal",
        "other_priority": "high",
        "limit_sensitivity": 10,
        "timeframe": 12
    }
    part_model.update(observer_model)
    assert part_model.outlier_sensitivity_levels_input == 2
    assert part_model.outlier_sensitivity_levels_other == 2.25
    assert part_model.limit_threshold == 0.1
    assert part_model.plot_timeframe == 12
    assert part_model.is_cache_invalid

def test_set_serials(part_model):
    serials = ['12345', '67890']
    part_model.set_serials(serials)
    assert part_model.serials == serials

def test_get_locations(part_model):
    assert part_model.get_locations() == []

def test_setup_locations(part_model, mock_objects):
    client, query_master, observer_model = mock_objects
    serials = ['12345', '67890']
    part_model.set_serials(serials)
    stations_data = pd.DataFrame({'name': ['Station1', 'Station2']})
    query_master.get_stations_query.return_value = 'query'
    client.execute_query.return_value = stations_data

    part_model.setup_locations()
    assert part_model.locations == ['Station1', 'Station2']

def test_get_parameters(part_model, mock_objects):
    client, query_master, observer_model = mock_objects
    serials = ['12345', '67890']
    station = 'Station1'
    parameters_data = pd.DataFrame({
        'unit_serial_number': serials,
        'value': [10, 20],
        'name': ['param1', 'param2']
    })
    query_master.get_parameters_query.return_value = 'query'
    client.execute_query.return_value = parameters_data

    result = part_model.get_parameters(serials, station)
    pd.testing.assert_frame_equal(result, parameters_data)

def test_divide_dataframe(part_model):
    df = pd.DataFrame({'A': range(100)})
    chunks = part_model.divide_dataframe(df, chunk_size=20)
    assert len(chunks) == 5
    assert len(chunks[0]) == 20

# Run pytest
if __name__ == "__main__":
    pytest.main()
