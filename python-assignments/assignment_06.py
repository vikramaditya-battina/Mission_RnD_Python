__author__ = 'Kalyan'

from placeholders import *

# instead of returning a list of tuples like zip, generate it incrementally (refer to the generators and iterators lessons)
# a tuple at a time. Use exception control flow to write elegant code.
def generator_zip(seq1, seq2, *more_seqs):
    result=[seq1,seq2]
    result2=[]
    x=0
    for i in more_seqs:
        result.append(i)
    while 1:
        try:
            tupple=[]
            for t in result:
                tupple.append(t[x])
            tupple=tuple(tupple)
            x=x+1
            yield tupple
        except IndexError:
            raise StopIteration





    pass


def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1,5), "abc", [1,2])
    assert [(1,'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1,2), "abcd")
    assert [(1,'a'), (2, 'b')] == list(gen)

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___