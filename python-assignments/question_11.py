__author__ = 'Kalyan'

def right_binary_search(inpu, key):
    x=-1
    if inpu==None :
        return -1
    high=len(inpu)-1
    if high==-1:
        return -1
    low=0

    while low<=high :

        mid=(low+high)/2
        if inpu[mid]==key:
            x=mid
            low=mid+1
        elif key>inpu[mid]:
            low=mid+1
        else:
            high=mid-1
    if x!=-1:
        return x

    return -1

    pass


def test_right_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == right_binary_search(input, value)
        
    assert -1 == right_binary_search(input, -10)
    assert -1 == right_binary_search(input, 100)

    assert -1 == right_binary_search([], 10)
    assert -1 == right_binary_search(None, 10)
    assert 0 == right_binary_search([10], 10)
    assert -1 == right_binary_search([10], 5)

    input = [1,1,2,2,2]

    assert 1 == right_binary_search(input, 1)
    assert 4 == right_binary_search(input, 2)
