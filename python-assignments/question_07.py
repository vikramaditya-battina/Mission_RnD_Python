__author__ = 'hemavishnu'

from listutils import *
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#given you a list 1->2->3->4->5 swap alternate elements and return the new head
#the new list head should result out 2->1->4->3->5
def swap_alternate_nodes_of_list(head):
    if head==None:
        return head
    elif head.next==None:
        return head
    else:
        temp=swap_alternate_nodes_of_list((head.next).next)
        temp1=head.next
        temp1.next=head
        head.next=temp
        return temp1

    pass


#write test cases covering all cases for your solution
def test_swap_alternate_nodes_of_list():
    head=to_linked_list([1,2,3,4])
    assert [2,1,4,3]==from_linked_list(swap_alternate_nodes_of_list(head))
    head=to_linked_list([1,2,3,4,5])
    assert [2,1,4,3,5]==from_linked_list(swap_alternate_nodes_of_list(head))
    head=to_linked_list([1])
    assert [1]==from_linked_list(swap_alternate_nodes_of_list(head))

    head=to_linked_list([1,2])
    assert [2,1]==from_linked_list(swap_alternate_nodes_of_list(head))
    head=to_linked_list([])
    assert []==from_linked_list(swap_alternate_nodes_of_list(head))
    pass