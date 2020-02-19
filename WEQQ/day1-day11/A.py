from threading import Lock,Thread

def a():
    while True:
        locka.acquire()
        print('a')
        lockb.release()


def b():
    while True:
        lockb.acquire()
        print('b')
        locka.release()




a1=Thread(target=a)
b2=Thread(target=b)

locka=Lock()
lockb=Lock()

# locka.acquire()

a1.start()
b2.start()

a1.join()
b2.join()

