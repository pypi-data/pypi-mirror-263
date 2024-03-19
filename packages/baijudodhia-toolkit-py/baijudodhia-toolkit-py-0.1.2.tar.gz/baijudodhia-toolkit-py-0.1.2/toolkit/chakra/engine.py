from toolkit.chakra.action import Action
from toolkit.chakra.condition import Condition
from toolkit.chakra.rule import Rule


class Engine:
    def __init__(self, obj, take_action):
        self._object = obj
        self._take_action = take_action

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        self._object = value

    async def run(self, validations):
        rules = validations.get("rules", [])
        actions = validations.get("actions", [])

        rules_mapping = Rule(rules, self._object).mapping()

        for action in actions:
            condition_evaluation = Condition(
                action.get("condition"), rules_mapping
            ).evaluate()

            if condition_evaluation:
                await Action(
                    action, rules_mapping, self._object, self._take_action
                ).execute()
