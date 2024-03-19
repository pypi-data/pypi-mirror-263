import pytest
from toolkit.chakra.rule import Rule
from toolkit.chakra.source import Source


@pytest.fixture
def source():
    return Source({"user": {"details": {"name": "Baiju"}}})


@pytest.fixture
def data():
    return {"user": {"details": {"name": "Baiju"}}}


@pytest.fixture
def get_rules():
    return [
        {
            "id": "1",
            "key": "OBJECT_PATH_EXISTS",
            "props": {"object": {"key": "user", "path": "details.name"}},
        },
        {
            "id": "2",
            "key": "VALUE_CHECK",
            "props": {
                "value": {
                    "source": {
                        "key": "PREDEFINED",
                        "props": {"predefinedValue": "Example fixed value"},
                    }
                },
                "pattern": {"key": "IS_EMAIL"},
            },
        },
        {
            "id": "3",
            "key": "VALUE_COMPARE",
            "props": {
                "value": {
                    "left": {
                        "source": {
                            "key": "PREDEFINED",
                            "props": {"predefinedValue": "Baiju"},
                        }
                    },
                    "right": {
                        "source": {
                            "key": "REMOTE",
                            "props": {
                                "remote": {
                                    "url": "https://jsonplaceholder.typicode.com/todos/1"
                                }
                            },
                        }
                    },
                }
            },
        },
    ]


def test_run_rule(source, data, get_rules):
    rule_engine = Rule(get_rules, data)
    evaluation_result = rule_engine.mapping()
    assert evaluation_result == {"1": True, "2": False, "3": False}
