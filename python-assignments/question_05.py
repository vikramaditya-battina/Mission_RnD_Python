__author__ = 'kishore'
from listutils import *
notes = """
    This is to introduce you to create data structures of your own without help of built-in structures.
"""


#Convert a number into linked list such that each digit is in a node and pointing to node having next digit.
#The function should return head of the linked list.
#Do not use built-in functions.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def numtolinkedlist(num):
    if num<0:
        head=Node('-')
        num=num*-1
        head2=None
        head2=numtolinked(head2,num)
        head.next=head2
        return head
    else:
        head=None
        head=numtolinked(head,num)
        return head


def numtolinked(head,num):
    if num==0:
        return head
    else:
        temp=Node()
        temp.value=num%10
        temp.next=None
        temp.next=head
        head=temp
        return numtolinked(head,num/10)
    pass


#write down tests covering all possible cases to your solution
#Hint: Here tests can use built-in functions
def test_number_to_LinkedList():#no handled negative numbers
    head=None
    head=numtolinkedlist(1230)
    assert [1,2,3,0]==from_linked_list(head)
    head=None
    head=numtolinkedlist(1)
    assert [1]==from_linked_list(head)
    head=None
    head=numtolinkedlist(-12)
    assert ['-',1,2]==from_linked_list(head)


    pass