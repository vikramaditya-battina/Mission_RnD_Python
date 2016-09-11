__author__ = 'Kalyan'

from listutils import *


def merge_lists(head1, head2):
    resulthead=None
    resulttail=None
    while head1!=None and head2!=None:
        if head1.value>head2.value:
            if resulthead==None:
                resulthead=head2
                resulttail=head2

            else:
                resulttail.next=head2
                resulttail=resulttail.next
            head2=head2.next
            resulttail.next=None


        else:
            if resulthead==None:

                resulthead=head1
                resulttail=head1
            else:
                resulttail.next=head1
                resulttail=resulttail.next
            head1=head1.next
            resulttail.next=None
    if head1==None and head2!=None:
        if resulthead==None:
            return head2
        resulttail.next=head2
    elif head1!=None and head2==None:
        if resulthead==None:
            return head1
        resulttail.next=head1
    return resulthead

    pass


def test_merge_lists():
    head1 = to_linked_list([1, 2, 3])
    head2 = to_linked_list([1, 2, 3, 4, 5])

    result = merge_lists(head1, head2)
    assert [1, 1, 2, 2, 3, 3, 4, 5] == from_linked_list(result)

    head1 = to_linked_list([1, 2, 5])
    head2 = to_linked_list([4, 6, 7])

    result = merge_lists(head1, head2)
    assert [1, 2, 4, 5, 6, 7] == from_linked_list(result)

    head1 = to_linked_list([])
    head2 = to_linked_list([1, 2, 3, 4])

    result = merge_lists(head1, head2)
    assert [1, 2, 3, 4] == from_linked_list(result)

    result = merge_lists(None, None)
    assert [] == from_linked_list(result)


def main():
    head1=to_linked_list([1,2,3])
    head2=to_linked_list([1,2,3,4,5])
    result=merge_lists(head1,head2)
    print from_linked_list(result)

if __name__=='__main__':
    main()

