__author__ = 'Kalyan'

# assume indexes i and j are non-negative and within bounds of array.
# shift the section [i, j] to the beginning of the array in place
def shuffle(input, i, j):
    pass


def test_shuffle():
    input = [1, 2, 3, 4, 5, 6]
    shuffle(input, 1, 2)
    assert [2, 3, 1, 4, 5, 6] == input

    input = [1, 2, 3, 4, 5, 6]
    shuffle(input, 4, 5)
    assert [5, 6, 1, 2, 3, 4] == input

    input = [1, 2, 3, 4, 5, 6]
    shuffle(input, 0, 3)
    assert [1, 2, 3, 4, 5, 6] == input

    input = [1, 2, 3, 4, 5, 6]
    shuffle(input, 1, 5)
    assert [2, 3, 4, 5, 6, 1] == input




