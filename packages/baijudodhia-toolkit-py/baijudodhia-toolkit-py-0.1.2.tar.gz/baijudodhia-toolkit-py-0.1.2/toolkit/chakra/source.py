import os

import requests

from toolkit.chakra.patterns import PATTERNS

from jsonpath_ng import jsonpath, parse


class Source:
    def __init__(self, object=None):
        """Initialize the source with an optional object."""
        self._object = object or {}

    @property
    def object(self):
        """Object property getter."""
        return self._object

    @object.setter
    def object(self, value):
        """Object property setter."""
        self._object = value

    def get_value_from_object(self, key, path):
        """Retrieve a value from an object based on a key and path using JSONPath."""
        # Check if the key exists in the object and if it does, apply the JSONPath query to it
        if key in self._object:
            jsonpath_expression = parse(path)
            match = jsonpath_expression.find(self._object[key])
            if match:
                return [m.value for m in match][
                    0
                ]  # Returns a list of matched elements
            else:
                return ""
        else:
            return ""

    def get_value_from_remote(self, url):
        """Fetch a value from a remote endpoint."""
        try:
          response = requests.get(url)
          if response.status_code == 200:
              return response.json()
          else:
              return {}
        except Exception as e:
          return {}

    def get_value_from_pattern(self, pattern_key, pattern=""):
        """Retrieve a value based on a pattern."""
        if pattern_key == "CUSTOM" and pattern is not None:
            return pattern
        elif pattern_key != "" and pattern_key != None:
            try:
                return PATTERNS[pattern_key]  # Placeholder for demonstration
            except Exception as e:
                return pattern
        else:
            return pattern

    def get_value_from_environment_variable(self, var_name):
        """Retrieve a value from environment variables."""
        return os.environ.get(var_name, "")

    def get_value_from_predefined(self, value):
        """Return a predefined fixed value."""
        return value

    def get_value_from_source(self, source):
        """Dispatch method to retrieve a value from a specified source type."""
        source_type = source["key"]
        if source_type == "OBJECT":
            return self.get_value_from_object(
                source["props"]["object"]["key"],
                source["props"]["object"]["path"],
            )
        elif source_type == "REMOTE":
            return self.get_value_from_remote(source["props"]["remote"]["url"])
        elif source_type == "PATTERN":
            return self.get_value_from_pattern(
                source["props"]["pattern"]["key"],
                source["props"]["pattern"].get("pattern", ""),
            )
        elif source_type == "PREDEFINED":
            return self.get_value_from_predefined(source["props"]["predefinedValue"])
        else:
            return ""
