import time 
from threading import Thread 

def do_work():
    print("Starting work")
    i = 0
    for _ in range(2000000):
        i += 1
    print("Finished Work")
    
for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
    
    
"""
Global Intrepeter Lock : Using just one processor and swapping out the threads 
This is why here, threads are being executed one after the other 
One thread is used at a time 
"""