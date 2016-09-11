__author__ = 'Kalyan'

notes = '''
This is assignment covers functions and nested functions.
Read the comments and fill up the code. If the spec is not clear, read the tests below.
'''

from placeholders import *


# Fill up the higher order function below to return a function which
# can be used to test whether a number is greatherThan the specified
# value
def greater_than(value):
    pass

# Fill up the negate function which returns a function that negates the output of the passed
# in function. The passed in function can take arbitrary number of
# positional args and returns True or False
def negate(func):
    pass

def test_greater_than():
    g8 = greater_than(8)

    assert True == g8(9)
    assert False == g8(5)
    assert False == g8(8)

    g5 = greater_than(5)
    assert True == g5(100)
    assert False == g5(-1)
    assert False == g5(5)


def test_negate():
    def greater(a, b):
        return a > b

    result = negate(greater)

    assert False == result(10, 9)
    assert True == result(10, 10)
    assert True == result(10, 11)

    def equal(a, b):
        return a == b

    notequal = negate(equal)

    assert False == notequal([10], [10])
    assert False == notequal("hello", "hello")
    assert True == notequal([], [10])

    not_any = negate(any)

    assert True == not_any([])
    assert True == not_any([None, None])
    assert False == not_any([10, ""])
    assert False == not_any("hello")


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
