"""
test_Delta.py

Currently, these tests are really simple. They may be expanded on later, if needed.
"""

from src.vardelta.Delta import Delta


my_value: Delta = Delta(1)
my_value.change_value(5)
assert my_value.get_change(0) == 4

print(my_value.changes)
print(my_value.values)
