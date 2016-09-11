__author__ = 'Kalyan'

def left_binary_search(input, key):
    x=-1
    if input==None :
        return -1
    high=len(input)-1
    if high==-1:
        return -1
    low=0

    while low<=high :
        mid=(low+high)/2
        if input[mid]==key:
            x=mid
            high=mid-1
        elif key>input[mid]:
            low=mid+1
        else:
            high=mid-1
    if x!=-1:
        return x

    return -1
    pass


def test_left_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == left_binary_search(input, value)
        
    assert -1 == left_binary_search(input, -10)
    assert -1 == left_binary_search(input, 100)

    assert -1 == left_binary_search([], 10)
    assert -1 == left_binary_search(None, 10)
    assert 0 == left_binary_search([10], 10)
    assert -1 == left_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 0 == left_binary_search(input, 1)
    assert 2 == left_binary_search(input, 2)
