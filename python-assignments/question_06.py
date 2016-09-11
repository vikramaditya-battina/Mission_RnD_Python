__author__ = 'hemavishnu'

from listutils import *
#
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#given the head of a list,
# reverse the list and return the head of the reversed list
def reversing(head,headnext):
    if headnext.next==None:
         head.next=headnext.next
         headnext.next=head

         return headnext
    else:
        temp=reversing(head.next , headnext.next)
        head.next = headnext.next
        headnext.next = head
        return temp

def reverse_linked_list(head):
    if head==None:
        return
    elif head.next==None:
        return head
    else:
        return reversing(head,head.next)
    pass


#write test cases covering all cases for your solution
def test_reverse_linked_list():
    head=to_linked_list([1,2,3,4])
    head=reverse_linked_list(head)
    assert [4,3,2,1]==from_linked_list(head)
    head=to_linked_list([1,2])
    head=reverse_linked_list(head)
    assert [2,1]==from_linked_list(head)
    head=to_linked_list([1])
    head=reverse_linked_list(head)
    assert [1]==from_linked_list(head)
    head=to_linked_list([])
    head=reverse_linked_list(head)
    assert []==from_linked_list(head)
    pass