import time 
from threading import Thread 
import multiprocessing
from  multiprocessing import Process


def do_work():
    print("Starting work")
    i = 0
    for _ in range(2000000):
        i += 1
    print("Finished Work")
    

if __name__ == "__main__":
    #multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()