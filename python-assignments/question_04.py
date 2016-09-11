__author__ = 'kishore'

notes = """
    This is to introduce you to think on optimizing the solution by iterating down the code written
"""


#Given a list of numbers, modify the list so that each element has the product of all elements except the number
#ex: Input:[1,2,3,4,5]
#output:[120,60,40,30,24]
#Return the list of products
def product_of_list_elements(lis):
    proleft=[]
    for i in range(0,len(lis)):
        if i==0:
            proleft.append(lis[i])
        else:
            proleft.append(proleft[i-1]*lis[i])
    for i in range(len(lis)-1,-1,-1):
        if i!=len(lis)-1:
            lis[i]=lis[i+1]*lis[i]
    for i in range(len(lis)):
        if i==0:
            lis[i]=lis[i+1]
        elif i==len(lis)-1:
            lis[i]=proleft[i-1]
        else :
            lis[i]=lis[i+1]*proleft[i-1]
    return lis

    pass


#write your own tests covering all the possible cases to your solution
def test_product_of_list_elements():
    assert [120,60,40,30,24]==product_of_list_elements([1,2,3,4,5])
    assert [0,0,0,0,0]==product_of_list_elements([12,0,0,12,34])
    assert [2,0,0]==product_of_list_elements([0,1,2])
    pass
