__author__ = 'Kalyan'

notes = '''
Python allows users to add user defined types via classes. This allows you to augment
builtin types like dict, list, tuple with your own types with their own specific behavior.

Like most common languages like java and c#, python supports objected oriented features
like class definitions, inheritance and polymorphism.

However, unlike java and c#, python does not insist that you have to forcibly model your
problem domain as classes if it does not make sense. You could use any mix of modules,
functions and classes to model your application. For e.g. if you goal is to code up the
fibonacci function or write a routine that sorts a sequence then defining a class
does not make sense.

This assignment only deals with the syntax of classes and its features. You must
look up references to actually learn object oriented programming.

http://c2.com/cgi/wiki?AlanKaysDefinitionOfObjectOriented
'''

from placeholders import *

notes_1 = '''
 We are defining the classes in the function scope so that we can redefine them for every test.
 Generally you would define them at the module scope.
'''


#classes are objects too, they have a type, have attributes, can be passed
# to functions, held in data structures etc.
def test_classes_are_objects():
    class Queue(object):
        """Queue with push and pop functions."""
        pass

    def get_attr_count(obj):
        return len(dir(obj))

    assert 'type' == type(Queue).__name__ #note this.
    assert 'Queue with push and pop functions.' == Queue.__doc__
    assert 18== get_attr_count(Queue)

def test_classes_are_callable_objects():
    class Queue(object):
        pass

    #classes are callable objects just like function objects
    assert True== callable(Queue)


def test_classes_are_object_factories():
    class Queue(object):
        pass

    q1 = Queue()  # you can 'call' a class to create an instance
    q2 = Queue()

    assert '__main__.Queue' == type(q1).__class__
    assert '__main__.Queue' == type(q2).__class__

    assert False == (q1 is Queue)
    assert False == (q2 is Queue)
    assert False == (q2 is q1)

    assert True == isinstance(q1, Queue)
    assert True == isinstance(q2, Queue)

    assert 18 == len(dir(Queue))
    assert 18 == len(dir(q1))
    assert 18 == len(dir(q2))


#if an __init__ method exists it is called with the object that is
#being created, so you can initialize it.
def test_classes_init_constructor():
    test_list = []

    class Queue(object):
        def __init__(self):
            assert True, "Entered here !"
            test_list.append(self)

    q1 = Queue() # fix the assert to pass this.
    self_argument = test_list[0]
    assert True == (self_argument is q1)

def test_classes_init_with_args():
    class Queue(object):
        def __init__(self, name):
            self.name = name

    q1 = Queue("q1")
    q2 = Queue("q2")

    assert 'q1' == q1.name
    assert 'q2' == q2.name

    try:
        q3 = Queue()
    except TypeError: #what error do you get?
        pass


#just like def, class is also a runtime statement which bounds a class name with the class body code
def test_class_is_an_executable_statement():
    def create_class(value):
        if (value > 10):
            class Queue(object):
                def __init__(self):
                    self.name = ">10queue"
        else:
            class Queue(object):
                def __init__(self):
                    self.name = "<=10queue"

        return Queue

    Q_class = create_class(20)
    q1 = Q_class()
    assert '>10queue'== q1.name

    Q_class = create_class(5)
    q1 = Q_class()
    assert '<=10queue'== q1.name


# the self argument name is just a convention but it is
# followed widely, so don't change the name of the first argument
# this is in contrast to other languages where the instance is implicit via
# the 'this' keyword.
def test_classes_methods():
    class Queue(object):
        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            self._queue.append(obj)

        def pop(self):
            return self._queue.pop(0)

    q1 = Queue("q1")
    q1.push(10) #note that we pass only one argument
    assert 10== q1.pop()

    #above is a equivalent to
    Queue.push(q1, 10)
    assert 10 == Queue.pop(q1)


def test_classes_bound_and_unbound_methods():
    class Queue(object):
        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            self._queue.append(obj)

        def pop(self):
            return self._queue.pop(0)

    q1 = Queue("q1")
    q1_push = q1.push

    assert False == (q1.push is Queue.push)

    assert '<__main__.Queue object at 0x02A48D90>' == Queue.push.__self__   #unbound method
    assert None == q1_push.__self__      #bound method

    # now understand the output of these 2 statements.
    print q1.push
    print Queue.push

def test_classes_can_have_state():
    class Queue(object):
        count = 0
        def __init__(self, name):
            self.name = name
            self._queue = []
            Queue.count += 1

        def push(self, obj):
            self._queue.append(obj)

        def pop(self):
            return self._queue.pop(0)

    assert 0 == Queue.count
    q1 = Queue("q1")
    assert 1 == Queue.count
    q2 = Queue("q2")
    assert 2 == Queue.count

    try:
        value = q1.count
    except AttributeError :
        pass


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
