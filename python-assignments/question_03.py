__author__ = 'kishore'

notes = """
    This is to make you familiar with in place usage of lists.
"""


#numbers is list of 0's 1's and 2's ina random order.
#Your job is to modify the list in place to sort in increasing order
#Don't use any builtin functions on lists
def sort_0_1_2(lis):
    i=0
    j=len(lis)-1  #sorting of zeros and all values
    while i<j:
        if lis[i]==0:
            i=i+1
        elif lis[j]==1 or lis[j]==2:
            j=j-1
        else :
            temp=lis[i]
            lis[i]=lis[j]
            lis[j]=temp
    j=len(lis)-1
    if lis[i]==0:
        i=i+1

    while i<j:
        if lis[i]==1:
            i=i+1
        elif lis[j]==2:
            j=j-1
        else:
            temp=lis[i]
            lis[i]=lis[j]
            lis[j]=temp
    return lis

    pass


#write tests to test your solution.
def test_sort_0_1_2():
    assert [0,0,1,1,2,2]==sort_0_1_2([1,1,2,2,0,0])
    assert [0,0,2] == sort_0_1_2([0,2,0])
    assert [0,0,0,0,0,1,1,2,2,2]==sort_0_1_2([0,0,0,2,2,1,1,0,0,2])
    pass