import threading
import time

def thread_function():
    print("Thread is starting...")
    time.sleep(2) 
    print("Thread is finishing...")

def main():
    thread = threading.Thread(target=thread_function)
    thread.start()
    thread.join()

    print("Main thread is finishing...")

if __name__ == "__main__":
    main()
