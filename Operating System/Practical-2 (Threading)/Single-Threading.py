import time

def main():

    n = int(input("Enter the number of threads: "))
    print("Main thread started.")
    for i in range(1, n+1):
        print(f"Main thread: {i}")
        time.sleep(1)  

    print("Main thread finished.")

if __name__ == "__main__":
    main()
