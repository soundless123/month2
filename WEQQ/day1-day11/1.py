import threading
import time

def threada():
    for i in range(1, 27,2):
        lockb.acquire()
        print(i,end='')
        print(i+1,end='')
        locka.release()


def threadb():
    for i in range(65, 91,2):
        locka.acquire()
        print(chr(i),end='')
        print(chr(i+1),end='')
        lockb.release()



locka = threading.Lock()
lockb = threading.Lock()

ta = threading.Thread(None, threada)
tb = threading.Thread(None, threadb)
locka.acquire()

ta.start()
tb.start()

ta.join()
tb.join()



