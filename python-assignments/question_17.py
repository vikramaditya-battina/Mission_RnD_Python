__author__ = 'Kalyan'

notes = '''
This problem deals with circular linked lists. The circular list is sorted, but the head does not point to the lowest
element, it can point to a random element.
'''

from listutils import *

# insert into a sorted linked list so that the resulting list is still sorted. head does *NOT* point to the minimum node.
# do not modify head unless required.
def insert_sorted(head, value):
    temp=head
    node=Node(value)
    if head==None:
        head=node
        head.next=head
        return head
    while temp.next!=head:
        if temp.value<= node.value and temp.next.value>=node.value:
            print 'vikram'
            break
        if temp.value>temp.next.value:
            if node.value>= temp.value or node.value<=temp.next.value:
                print 'aditya'
                break

        temp=temp.next
    temp2=temp.next
    temp.next=node
    node.next=temp2
    return head





    pass


def check_insertion(input, value, output):
    head = to_circular_list(input)
    head = insert_sorted(head, value)
    assert output == from_circular_list(head)



def test_insert_sorted():
    check_insertion([11, 13, 5, 7, 9], 15, [11,13, 15, 5, 7, 9])
    check_insertion([11, 13, 5, 7, 9], 10, [11, 13, 5, 7, 9, 10])
    check_insertion([11, 13, 5, 7, 9], 3, [11, 13, 3,  5, 7, 9])
    check_insertion([11, 13, 5, 7, 9], 6, [11, 13,  5, 6, 7, 9])

    check_insertion([5], 10, [5,10])
    check_insertion([5], 1, [5,1])
    check_insertion([], 10, [10])
    check_insertion([5, 8], 7, [5,7,8])

