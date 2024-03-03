import multiprocessing
import random
import time

def producer(pipe):
    for i in range(10):
        item = random.randint(1, 100)  # Produce a random item
        pipe.send(item)
        print("Produced item:", item)
        time.sleep(1)  # Simulate some processing time
    pipe.close()

def consumer(pipe):
    while True:
        try:
            item = pipe.recv()
            print("Consumed item:", item)
            time.sleep(1)  # Simulate some processing time
        except EOFError:  # Pipe closed
            break

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    producer_process = multiprocessing.Process(target=producer, args=(child_conn,))
    consumer_process = multiprocessing.Process(target=consumer, args=(parent_conn,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
