import threading

class FibonacciThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.fib_sequence = [0, 1]

    def run(self):
        while len(self.fib_sequence) < self.n:
            next_fib = self.fib_sequence[-1] + self.fib_sequence[-2]
            self.fib_sequence.append(next_fib)

n = int(input("Enter your desired number: "))
threads = []

for i in range(5):  
    thread = FibonacciThread(n)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

fib_sequence = sorted(set(fib for thread in threads for fib in thread.fib_sequence))
print(f"Fibonacci sequence (multi-threaded) up to {n} numbers:", fib_sequence)

