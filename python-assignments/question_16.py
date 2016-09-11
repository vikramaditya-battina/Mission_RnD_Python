__author__ = 'Kalyan'

notes = '''
This problem deals with circular single linked lists, the tail of the list points back to head.

For this assignment assume that input list is sorted (ie) smallest element is head.
'''

from listutils import *

#insert a new node into the circular linked list so that the circular list loop sorted invariant holds
def insert_node(head, value):
    node=Node(value)
    if head==None:

        head=node
        head.next=head
        return head
    else:
        print 'cheting'
        temp=head
        while temp.next!=head:
            if node.value>= temp.value and node.value<=temp.next.value:
                temp2=temp.next
                temp.next=node
                node.next=temp2
                break
            temp=temp.next
        else:
            if node.value<=head.value:
                node.next=head
                head=node
                temp.next=head
                return head
            temp2=temp.next
            temp.next=node
            node.next=temp2
        return head






    pass


def check_insertion(input, value, output):
    head = to_circular_list(input)
    head = insert_node(head, value)
    assert output == from_circular_list(head)


def test_insert_node():
    check_insertion([3, 5, 7], 4, [3, 4, 5, 7])
    check_insertion([3, 5, 7], 9, [3, 5, 7, 9])
    check_insertion([3, 5, 7], 1, [1, 3, 5, 7])

    check_insertion([], 1, [1])
    check_insertion([1], 3, [1, 3])
    check_insertion([5], 3, [3,5])
