from toolkit.chakra.condition import Condition


class Action:
    def __init__(self, action, rule_mapping, obj, take_action):
        self._action = action
        self._rule_mapping = rule_mapping
        self._object = obj
        self._take_action = take_action

    async def execute(self):
        # Create a new condition based on the action's condition
        condition = Condition(self._action.get("condition"), self._rule_mapping)
        # Evaluate the condition
        action_success = condition.evaluate()

        # If the condition is met, execute the action
        if action_success:
            return await self._take_action(self._action, self._object)
