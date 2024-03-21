"""
Delta.py
"""


class Delta:
    def __init__(self, value: float) -> None:
        """
        Creates a value that contains a history of itself to easily keep track of changes.
        :param value: The initial value.
        """
        self.value: float = value
        self.values: list[float] = []
        self.change: float = 0.0
        self.changes: list[float] = []

        self.change_value(value)

    def refresh_values(self) -> None:
        self.value = self.values[-1]

        if len(self.changes) == 0:
            self.change = 0.0
        else:
            self.change = self.changes[-1]

    @staticmethod
    def _convert_to_key(value: int) -> int:
        """
        For ease of use, the functions in this class take "0" to return the most recent value, or the last index of
        self.value. However, since self.value is a list, we need to covert this to the corresponding index. In this
        case, 0 should be -1 since they want the most recent value added, or the current value. 1 is the second most
        recent value, so it would have a key of -2. This function also supports negative numbers. So if the user wants
        the first number, they can do -1.

        This function should only be used to handle arguments and not used to call on a table yourself.
        :param value: The value specified by the user.
        :return: The corresponding index.
        """
        return -1 - value

    def get_value(self, values_ago: int = 0) -> float:
        """
        Retrieves the specified value from the change history.
        :param values_ago: How many values ago to retrieve (0 for most recent, 1 for second most recent, etc.).
        :return: The corresponding value.
        """
        try:
            return self.values[self._convert_to_key(values_ago)]
        except IndexError:
            pass

    def get_change(self, changes_ago: int = 0) -> float:
        """
        Retrieve a specific change x amount of changes ago.
        :param changes_ago: How many changes ago to retrieve. 0 is the most recent change, or the change between the
        current number [0] and the previous number [1].
        :return: The amount the value was changed.
        """
        try:
            return self.changes[self._convert_to_key(changes_ago)]
        except IndexError:
            pass

    def change_value(self, new_value: float) -> float:
        """
        Changes the value to the argument specified and calculates the change accordingly.
        :param new_value: The value to update to.
        :return: The new value (the parameter itself).
        """
        self.values.append(new_value)

        if self.calc_change() != "IndexError":
            self.changes.append(self.calc_change())

        return new_value

    def calc_change(self, first_val: int = 0, second_val: int = 1) -> float | str:
        """
        Calculate the change between two historic values.
        :param first_val: How many values ago the first value is.
        :param second_val: How many values ago the second value is.
        :return: The change between the two values.
        """
        try:
            return self.values[self._convert_to_key(first_val)] - self.values[self._convert_to_key(second_val)]
        except IndexError:
            # I'm not sure if there is a better way to do this. I just don't want self.changes to populate with None.
            return "IndexError"
