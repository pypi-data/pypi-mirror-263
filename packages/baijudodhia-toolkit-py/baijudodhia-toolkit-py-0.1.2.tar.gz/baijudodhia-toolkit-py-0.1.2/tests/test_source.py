import pytest
from toolkit.chakra.source import Source


@pytest.fixture
def source():
    return Source({"user": {"details": {"name": "Baiju"}}})


@pytest.fixture
def mock_requests_get(requests_mock):
    requests_mock.get(
        "https://example.com/config.json",
        text='{"example_key": "example_value"}',
    )


def test_get_value_from_source_object_path(source):
    output = source.get_value_from_source(
        {
            "key": "OBJECT",
            "props": {"object": {"key": "user", "path": "$.details.name"}},
        }
    )
    assert output == "Baiju"


def test_get_value_from_source_pattern_email(source):
    output = source.get_value_from_source(
        {
            "key": "PATTERN",
            "props": {"pattern": {"key": "IS_ALPHA"}},
        }
    )
    assert output == "^[a-zA-Z]+$"


def test_get_value_from_source_pattern_custom(source):
    output = source.get_value_from_source(
        {
            "key": "PATTERN",
            "props": {"pattern": {"key": "CUSTOM", "pattern": "^\[0-9\]{5}$"}},
        }
    )
    assert output == "^\[0-9\]{5}$"


def test_get_value_from_source_predefined(source):
    output = source.get_value_from_source(
        {"key": "PREDEFINED", "props": {"predefinedValue": "Baiju"}}
    )
    assert output == "Baiju"


def test_get_value_from_source_remote(
    source,
):
    output = source.get_value_from_source(
        {
            "key": "REMOTE",
            "props": {
                "remote": {
                    "url": "https://jsonplaceholder.typicode.com/todos/1"
                }
            },
        }
    )
    assert output == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False,
    }
