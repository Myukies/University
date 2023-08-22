import threading
import time
import random

BUFFER_SIZE = 5
buffer = []
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
terminate_flag = False  

def producer():
    while not terminate_flag:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Produced {item}, Buffer: {buffer}")
        mutex.release()
        full.release()
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    while not terminate_flag:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed {item}, Buffer: {buffer}")
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.1, 0.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

time.sleep(3)

terminate_flag = True

producer_thread.join()
consumer_thread.join()

print("Program finished.")
