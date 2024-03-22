"""
test_Delta.py

Currently, these tests are really simple. They may be expanded on later, if needed.
"""

from src.vardelta.Delta import Delta


var: Delta = Delta(0)

# These tests ensure that the method used to retrieve historic values and changes works, and that they are calculating
# properly.
var.change_value(1)
assert var.value == 1
assert var.change == 1

assert var.get_value(0) == 1
assert var.get_value(1) == 0

assert var.get_change(0) == 1

var.change_value(15)
assert var.value == 15
assert var.change == 14

assert var.get_value(0) == 15
assert var.get_value(1) == 1
assert var.get_value(2) == 0

assert var.get_change(0) == 14
assert var.get_change(1) == 1

# This ensures the reset method is working properly.
var.reset()
assert len(var.values) == 1
assert len(var.changes) == 0

# This test ensures that the limit on history works, and it'll properly delete the oldest value if it goes over.
for i in range(0, 50):
    var.change_value(i)

assert len(var.values) <= var.limit
assert len(var.changes) <= var.limit

# Change the limit and run it again.
var.reset()
var.limit = 100

for i in range(0, 100):
    var.change_value(i)

assert len(var.values) <= var.limit
assert len(var.changes) <= var.limit
