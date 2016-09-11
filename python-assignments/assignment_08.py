__author__ = 'Kalyan'

from placeholders import *

# write a class Person with attributes name, age, weight (kgs), height (ft) and takes
# them through the constructor and exposes a method get_bmi_result()
# which returns one of "underweight", "healthy", "obese"
# http://en.wikipedia.org/wiki/Body_mass_index

class Person:
    pass


def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
