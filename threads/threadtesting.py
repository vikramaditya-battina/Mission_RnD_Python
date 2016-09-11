import threading
import time
max=10
count=0
cv=threading.Condition()
def increment():
    global count
    print 'in to increment',count

    cv.acquire()
    while count==max:

        cv.wait()
    print 'incrementint...........'
    count=count+1
    cv.notify_all()
    cv.release()

def decrement():

    global count
    print 'into decrement',count
    cv.acquire()
    while count<=0:

        cv.wait()
    print 'decrementing.......'
    count=count-1
    cv.notify_all()
    cv.release()

if __name__=='__main__':
    i=0


    while i<10:
       decrement()

       i=i+1
    i=0
    while i<10:
        increment()

        i=i+1

    print count






