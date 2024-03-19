from toolkit.chakra.patterns import PATTERNS
from toolkit.chakra.source import Source
import re
import jsonpath_ng

class Rule:
    def __init__(self, rules, obj):
        self._rules = rules
        self._obj = obj

    def evaluate(self, rule):
        rule_type = rule["key"]
        rule_evaluation_status = False
        source = Source(self._obj)

        if rule_type == "OBJECT_PATH_EXISTS":
            object_key = rule['props']['object']['key']
            object_path = rule['props']['object']['path']

            if object_key in self._obj:
                jsonpath_expr = jsonpath_ng.parse(object_path)
                matches = jsonpath_expr.find(self._obj[object_key])
                if matches:
                    rule_evaluation_status = True

        elif rule_type == "VALUE_CHECK":
            value_source = rule["props"]["value"]["source"]
            pattern_key = rule["props"]["pattern"]["key"]
            pattern_pattern = rule["props"]["pattern"].get("pattern", "")

            value = source.get_value_from_source(value_source)

            print(value)

            if pattern_key == "CUSTOM":
                pattern = re.compile(pattern_pattern)
            else:
                pattern = re.compile(PATTERNS[pattern_key])

            if pattern.match(value):
                rule_evaluation_status = True

        elif rule_type == "VALUE_COMPARE":
            left_value_source = rule["props"]["value"]["left"]["source"]
            right_value_source = rule["props"]["value"]["right"]["source"]

            left_value = source.get_value_from_source(left_value_source)
            right_value = source.get_value_from_source(right_value_source)

            if left_value == right_value:
                rule_evaluation_status = True

        return rule_evaluation_status

    def mapping(self):
        rules_evaluation_mapping = {}

        for rule in self._rules:
            rule_evaluation_status = self.evaluate(rule)
            rules_evaluation_mapping[rule['id']] = rule_evaluation_status

        return rules_evaluation_mapping