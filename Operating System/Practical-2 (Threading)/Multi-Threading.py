import threading
import time

def thread_function(thread_id):
    print(f"Thread {thread_id} is starting...")
    time.sleep(2)  
    print(f"Thread {thread_id} is finishing...")

def main():
    num_threads = 3
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Main thread is finishing...")

if __name__ == "__main__":
    main()
