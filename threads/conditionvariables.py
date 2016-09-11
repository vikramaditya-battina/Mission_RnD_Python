import threading
class Queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.lis=[]
        self.index=-1
        self.cv=threading.Condition()
    def enqueue(self,value):
        self.cv.acquire()
        while self.index==self.maxsize-1:
            self.cv.wait()
        self.lis.append(value)
        self.index=self.index+1
        self.cv.notify_all()
        self.cv.release()

    def dequeue(self,value):
        self.cv.acquire()
        while self.index==-1:
            self.cv.wait()
        x=self.lis.pop(0)
        self.index=self.index-1
        self.cv.notify_all()
        self.cv.release()
        return x






