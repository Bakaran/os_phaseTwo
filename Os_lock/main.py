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
