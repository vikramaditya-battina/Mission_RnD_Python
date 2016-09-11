__author__ = 'kishore'

notes = """
   This problem is to introduce you to bit manipulations concepts and unit testing.

"""


# zero_ones is a n arbitrary iterable which returns a series of 0's or 1's
# convert it to a python long. So I could pass in a string or list or tuple or generator of 0's and 1's

def binary_to_base10(zero_ones):
    result=0
    for i in zero_ones:
        result=result*2+int(i)
    return result

    pass


#Write tests to test your solution for all possible valid inputs
def test_binary_to_base10():
    assert 17==binary_to_base10('10001')
    assert 17==binary_to_base10(['1','0','0','0','1'])
    assert 17==binary_to_base10((1,0,0,0,1))
    assert 0==binary_to_base10('0')
    pass