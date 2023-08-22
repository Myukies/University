import threading
import time

def print_numbers():
    for i in range(1, 9):
        print(f"Number: {i}")
        time.sleep(1.2)  

def print_letters():
    for letter in 'Threading':
        print(f"Letter: {letter}")
        time.sleep(1.2)  

if __name__ == "__main__":
    print("Main thread started.")

    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main thread finished.")
