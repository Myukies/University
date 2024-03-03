def fcfs(processes):
    current_time = 0

    print("FCFS Scheduling:")
    for process in processes:
        print(f"Process {process['pid']} starts at time {max(current_time, process['arrival_time'])}.")
        current_time = max(current_time, process['arrival_time']) + process['burst_time']
        print(f"Process {process['pid']} ends at time {current_time}.")

def main():
    processes = [
        {'pid': 1, 'arrival_time': 0, 'burst_time': 6},
        {'pid': 2, 'arrival_time': 2, 'burst_time': 3},
        {'pid': 3, 'arrival_time': 4, 'burst_time': 4},
        {'pid': 4, 'arrival_time': 6, 'burst_time': 5},
    ]
    fcfs(processes)

if __name__ == "__main__":
    main()
