import pytest
from toolkit.chakra.condition import Condition
from toolkit.chakra.rule import Rule
from toolkit.chakra.source import Source


def test_run_rule():
    condition = Condition("1 AND 2", {"1": True, "2": False, "3": False})

    evaluation_result = condition.evaluate()
    assert evaluation_result == False
