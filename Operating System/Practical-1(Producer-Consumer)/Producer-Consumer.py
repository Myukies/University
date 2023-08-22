import multiprocessing
import time
import random

BUFFER_SIZE = 5
NUM_ITEMS = 10

shared_buffer = multiprocessing.Array('i', BUFFER_SIZE)
buffer_lock = multiprocessing.Lock()
items_produced = multiprocessing.Value('i', 0)
items_consumed = multiprocessing.Value('i', 0)
buffer_not_full = multiprocessing.Condition(lock=buffer_lock)
buffer_not_empty = multiprocessing.Condition(lock=buffer_lock)

producer_done = multiprocessing.Event()
consumer_done = multiprocessing.Event()

def producer():
    for _ in range(NUM_ITEMS):
        item = random.randint(1, 100)
        with buffer_lock:
            while items_produced.value - items_consumed.value == BUFFER_SIZE:
                buffer_not_full.wait()
            shared_buffer[items_produced.value % BUFFER_SIZE] = item
            print(f"Producing {item}")
            items_produced.value += 1
            buffer_not_empty.notify()
        time.sleep(random.uniform(0.1, 0.5))
    producer_done.set()
    print("Producer finished producing items")

def consumer():
    while not producer_done.is_set() or items_consumed.value < NUM_ITEMS:
        with buffer_lock:
            while items_produced.value == items_consumed.value:
                if producer_done.is_set():
                    break
                buffer_not_empty.wait()
            if items_consumed.value < NUM_ITEMS:
                item = shared_buffer[items_consumed.value % BUFFER_SIZE]
                shared_buffer[items_consumed.value % BUFFER_SIZE] = 0
                items_consumed.value += 1
                buffer_not_full.notify()
                print(f"Consuming {item}")
        time.sleep(random.uniform(0.1, 0.3))
    print("Consumer finished consuming items")
    consumer_done.set()

if __name__ == "__main__":
    producer_process = multiprocessing.Process(target=producer)
    consumer_process = multiprocessing.Process(target=consumer)

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
    
    print("All items have been produced and consumed.")
