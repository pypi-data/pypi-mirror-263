class Formula:
    def __init__(self, variables, formula):
        self._variables = variables
        self._formula = formula

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, value):
        self._variables = value

    @property
    def formula(self):
        return self._formula

    @formula.setter
    def formula(self, value):
        self._formula = value

    def evaluate(self):
        keys = list(self._variables.keys())
        values = list(self._variables.values())

        expression = f"return {self._formula}"
        fn = eval("lambda " + ",".join(keys) + ":" + expression)

        return fn(*values)
