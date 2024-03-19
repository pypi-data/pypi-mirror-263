def replace_string(string, old, new):
    return string.replace(str(old), str(new))


class Condition:
    def __init__(self, condition, rules_mapping):
        self._condition = (
            condition if condition else "True"
        )  # Default condition is True if not provided
        self._rules_mapping = rules_mapping

    def parse_keys(self, condition, rules_evaluation_mapping):
        for key, value in rules_evaluation_mapping.items():
            condition = replace_string(condition, key, value)
        return condition

    def parse_operators(self, condition):
        return (
            condition.replace("AND", "and")
            .replace("OR", "or")
            .replace("NOT", "not")
            .replace("XOR", "^")
            .replace("NAND", "not &")
            .replace("NOR", "not |")
            .replace("XNOR", "not ^")
            .replace("false ", "False ")
            .replace(" false", " False")
            .replace(" false ", " False ")
            .replace("true", "True")
            .replace(" true", " True")
            .replace(" true ", " True ")
        )

    def evaluate(self):
        self._condition = self.parse_operators(self._condition)
        self._condition = self.parse_keys(self._condition, self._rules_mapping)
        return eval(self._condition)
