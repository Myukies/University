import threading
import queue
import random
import time

BUFFER_SIZE = 5
q = queue.Queue(BUFFER_SIZE)

class ProducerThread(threading.Thread):
    def run(self):
        global q
        for i in range(10):
            item = random.randint(1, 100)  # Produce a random item
            q.put(item)
            print("Produced item:", item)
            time.sleep(1)  # Simulate some processing time

class ConsumerThread(threading.Thread):
    def run(self):
        global q
        for i in range(10):
            item = q.get()
            print("Consumed item:", item)
            time.sleep(1)  # Simulate some processing time

producer_thread = ProducerThread()
consumer_thread = ConsumerThread()

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
