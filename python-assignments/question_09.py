__author__ = 'Kalyan'


def binary_search(input, key):
    if type(input).__name__!='list':
        raise TypeError,'expecting the list as the input'
    for i in input:
        if (type(i).__name__!='int'):
            raise TypeError,'expecting the list elements as the integers'
    for i in range(len(input)-1):
        if input[i]>input[i+1]:
            raise ValueError,'values should be in sorted order'
    if input==None :
        return -1
    high=len(input)-1
    if high==-1:
        return -1
    low=0
    mid=(low+high)/2
    while low<=high :
        mid=(low+high)/2
        if input[mid]==key:
            return mid
        elif key>input[mid]:
            low=mid+1
        else:
            high=mid-1

    return -1


    pass



def test_binary_search():
    input = range(10)
    for index, value in enumerate(input):
        assert index == binary_search(input, value)

    assert -1 == binary_search(input, -10)
    assert -1 == binary_search(input, 100)

    assert -1 == binary_search([], 10)
    assert -1 == binary_search(None, 10)
    assert 0 == binary_search([10], 10)
    assert -1 == binary_search([10], 5)
    assert -1==binary_search([1,2,3,4,5,6,7],10)
    assert -1==binary_search([1],2)
    assert -1==binary_search([1],-1)
    assert -1==binary_search([1],2)
    assert -1==binary_search([],1)
    assert 0==binary_search([1,2,3,4,5,6,7],1)
    assert 6==binary_search([1,2,3,4,5,6,7],7)
    assert -1==binary_search([1,2],3)
    assert -1==binary_search([1,2],0)




