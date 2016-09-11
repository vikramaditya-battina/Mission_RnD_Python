import threading
import time

# creating a thread.
class Worker(threading.Thread):
    def __init__(self,x):
        self.x = x
        obj=Account()
        threading.Thread.__init__(self)
    def run (self):
        i = 0
        print 'vikram'        #while i < 10:
            #print threading.current_thread().name, "[", str(self.x), "]"



def thread_demo():
    for x in xrange(10):
        worker_thread = Worker(x)
        worker_thread.start()


count = 0

def increment():
    global count
    count += 1


# sample race condition, what locks will u you use to make this thread safe?
class Account(object):
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        self.balance = value

    def debit(self, value):
        lock=threading.Lock()
        lock.acquire()
        balance = self.get_balance()
        time.sleep(3)
        balance -= value
        self.set_balance(balance)
        lock.release()
    def credit(self, value):
        lock=threading.Lock()
        lock.acquire()

        balance = self.get_balance()
        time.sleep(3)
        balance += value

        self.set_balance(balance)
        lock.release()

if __name__=='__main__':
    obj=Account()
    lock=threading.Lock()
    t=threading.Thread(None,target=obj.credit,args=(2000,))
    t.start()
    print obj.get_balance()
    t2=threading.Thread(None,target=obj.debit,args=(3000,))
    t2.start()
    print obj.get_balance()

    #t=threading.Thread(None,target=obj.credit,args=(100,))

    #obj.credit(100)
    #print obj.get_balance()