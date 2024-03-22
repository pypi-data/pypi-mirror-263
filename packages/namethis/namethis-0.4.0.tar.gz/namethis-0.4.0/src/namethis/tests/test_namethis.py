import pytest
import json
from unittest.mock import patch, MagicMock
from namethis import fetch_environment_variables, load_resource_definition, generate_resource_name

@pytest.fixture
def mock_files():
    with patch('importlib.resources.files') as mock_files:
        mock_path = mock_files.return_value.joinpath.return_value
        mock_path.read_text.return_value = '[{"name": "testResource", "slug": "test", "max_length": 10, "dashes": false, "scope": "global"}]'
        yield

def test_fetch_environment_variables_valid():
    with patch.dict('os.environ', {'LZID': '1234', 'ENVIRONMENT': 'prod', 'LOCATION_SHORT': 'usw'}):
        lzid, environment, location_short = fetch_environment_variables()
        assert lzid == '1234'
        assert environment == 'prod'
        assert location_short == 'usw'

def test_fetch_environment_variables_invalid_lzid():
    with patch.dict('os.environ', {'LZID': 'abc'}), pytest.raises(SystemExit) as pytest_wrapped_e:
        fetch_environment_variables()
    assert pytest_wrapped_e.type == SystemExit

@pytest.mark.parametrize("slug, max_length, supports_dashes, scope, lzid, environment, location_short, expected", [
    ("vm", 15, True, "global", "1234", "dev", "use", "vm-dev-1234"),
    ("aks", 20, False, "regional", "5678", "qa", "eun", "akseunqa5678"),
])
def test_generate_resource_name(slug, max_length, supports_dashes, scope, lzid, environment, location_short, expected):
    assert generate_resource_name(slug, max_length, supports_dashes, scope, lzid, environment, location_short) == expected
