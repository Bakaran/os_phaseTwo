#from multiprocessing import Process, Value, Array, Queue
#from time import sleep
#import multiprocessing
#def add(num, value, mutex):
#    tmp = 0
#    while True:
#        mutex.acquire()
#        print('add')
#        num.value += value
#        tmp = num.value
#        sleep(1)
#        if tmp != num.value:
#            print("Process conflict")
#        mutex.release()


#def sub(num, value, mutex):
#    tmp = 0
#    while True:
#        mutex.acquire()
#        print('sub')
#        num.value -= value
#        tmp = num.value
#        sleep(1.5)
#        if tmp != num.value:
#            print("Process conflict")
#        mutex.release()

#def mul(num, value, mutex):
#    tmp = 0
#    while True:
#        mutex.acquire()
#        print('mul')
#        num.value *= value
#        tmp = num.value
#        sleep(2)
#        if tmp != num.value:
#            print("Process conflict")
#        mutex.release()

#def div(num, value, mutex):
#    tmp = 0
#    while True:
#        mutex.acquire()
#        print('div')
#        num.value /= value
#        tmp = num.value
#        sleep(3)
#        if tmp != num.value:
#            print("Process conflict")
#        mutex.release()


#def Show(num):
#    while True:
#        sleep(0.5)
#        print(num.value)



#if __name__ == '__main__':
#    num = Value('d', 0.0)
#    arr = Array('i', range(2))
#    manager = multiprocessing.Manager()
#    mutex = manager.Lock()
#    q = Queue()
#    p1 = Process(target=add, args=(num, 10,mutex,))
#    p2 = Process(target=sub, args=(num, 5,mutex,))
#    p3 = Process(target=mul, args=(num, 2,mutex,))
#    p4 = Process(target=div, args=(num, 4,mutex,))

#    show = Process(target=Show, args=(num,))
#    show.start()
#    sleep(1)
#    p1.start()
#    p2.start()
#    p3.start()
#    p4.start()
#    while (True):
#        p1.join()
#        p2.join()
#        p3.join()
#        p4.join()
from multiprocessing import Process, Value, Array, Queue
from time import sleep

class Semaphore:
    def __init__(self,n:int):
        self.sem = Value('i',1)
        self.flag_0 = Value('i',0)
        self.flag_1 = Value('i',0)
        self.flag_2 = Value('i',0)
        self.flag_3 = Value('i',0)
        self.flag_4 = Value('i',0)
        self.sem_q = Queue(n)
    def Wait(self,process_id:int):
        self.sem.value -= 1
        if self.sem.value < 0:
            if process_id == 0:
                self.flag_0.value = 0
            elif process_id == 1:
                self.flag_1.value = 0
            elif process_id == 2:
                self.flag_2.value = 0
            elif process_id == 3:
                self.flag_3.value = 0
            elif process_id == 4:
                self.flag_4.value = 0
            self.sem_q.put(process_id)
            while True:
                if process_id == 0:
                    if self.flag_0.value == 1:
                        break
                elif process_id == 1:
                    if self.flag_1.value == 1:
                        break
                elif process_id == 2:
                    if self.flag_2.value == 1:
                        break
                elif process_id == 3:
                    if self.flag_3.value == 1:
                        break
                elif process_id == 4:
                    if self.flag_4.value == 1:
                        break
    def Signal(self):
        self.sem.value += 1
        if self.sem.value <= 0:
            process_id = self.sem_q.get()
            if process_id == 0:
                self.flag_0.value = 1
            elif process_id == 1:
                self.flag_1.value = 1
            elif process_id == 2:
                self.flag_2.value = 1
            elif process_id == 3:
                self.flag_3.value = 1
            elif process_id == 4:
                self.flag_4.value = 1
def add(num, value,s):
    tmp = 0
    while True:
        s.Wait(0)
        print('add')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print("Process conflict")
        s.Signal()

def sub(num, value,s):
    tmp = 0
    while True:
        s.Wait(1)
        print('sub')
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print("Process conflict")
        s.Signal()

def mul(num, value,s):
    tmp = 0
    while True:
        s.Wait(2)
        print('mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print("Process conflict")
        s.Signal()

def div(num, value,s):
    tmp = 0
    while True:
        s.Wait(3)
        print('div')
        num.value /= value
        tmp = num.value
        sleep(3)
        if tmp != num.value:
            print("Process conflict")
        s.Signal()

def Show(num,s):
    while True:
        #s.Wait(4)
        sleep(0.5)
        print(num.value)
        #s.Signal()

if __name__ == '__main__':
    num = Value('d', 0.0)
    s = Semaphore(5)
    p1 = Process(target=add, args=(num, 10,s,))
    p2 = Process(target=sub, args=(num, 5,s,))
    p3 = Process(target=mul, args=(num, 2,s,))
    p4 = Process(target=div, args=(num, 4,s,))
    show = Process(target=Show, args=(num,s,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
