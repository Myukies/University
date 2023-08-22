import threading
import time

readers_count = 0
resource = "Initial data"
readers_count_lock = threading.Semaphore(1)
resource_lock = threading.Semaphore(1)
terminate_flag = False

def reader(reader_id):
    global readers_count, resource, terminate_flag
    while not terminate_flag:
        readers_count_lock.acquire(); readers_count += 1
        if readers_count == 1: resource_lock.acquire()
        readers_count_lock.release()
        
        print(f"Reader {reader_id} read: {resource}")
        
        readers_count_lock.acquire(); readers_count -= 1
        if readers_count == 0: resource_lock.release()
        readers_count_lock.release()
        
        time.sleep(1)

def writer(writer_id):
    global resource, terminate_flag
    while not terminate_flag:
        resource_lock.acquire()
        
        resource = f"New data written by Writer {writer_id}"
        print(f"Writer {writer_id} wrote: {resource}")
        
        resource_lock.release()
        
        time.sleep(2)

reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

for thread in reader_threads: thread.start()
for thread in writer_threads: thread.start()

time.sleep(3)

terminate_flag = True  

for thread in reader_threads: thread.join()
for thread in writer_threads: thread.join()

print("Program finished.")
