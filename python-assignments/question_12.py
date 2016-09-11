__author__ = 'Kalyan'

# rotate the input list by number times in place.
# don't use any new intermediate lists if possible.

def rotate_right(a ,n):
    if len(a)==0: return
    n=n%len(a)
    i=0
    j=0
    x=a[0]
    while i<n:
        j=(j+n)%len(a)
        y=a[j]
        a[j]=x
        x=y
        if j<n:
            i=i+1
            x=a[i]
            j=j+1




    pass

def test_rotate():
    input = range(1,7)
    rotate_right(input, 2)
    assert [5,6,1,2,3,4] == input

    input = range(1,7)
    rotate_right(input, 3)
    assert [4,5,6,1,2,3] == input

    input = range(1,7)
    rotate_right(input, 1)
    assert [6,1,2,3,4,5] == input




