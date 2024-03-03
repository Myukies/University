def round_robin(processes, quantum):
    remaining_burst_time = [process['burst_time'] for process in processes]
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    current_time = 0
    completed = 0

    while completed != len(processes):
        for i in range(len(processes)):
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] > quantum:
                    current_time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    current_time += remaining_burst_time[i]
                    waiting_time[i] = current_time - processes[i]['burst_time']
                    remaining_burst_time[i] = 0
                    completed += 1
                    turnaround_time[i] = current_time - processes[i]['arrival_time']

    print("Process\tWaiting Time\tTurnaround Time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(len(processes)):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(f"{processes[i]['id']}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


if __name__ == "__main__":
    # Example processes
    processes = [
        {"id": 1, "arrival_time": 0, "burst_time": 5},
        {"id": 2, "arrival_time": 1, "burst_time": 3},
        {"id": 3, "arrival_time": 2, "burst_time": 8},
        {"id": 4, "arrival_time": 3, "burst_time": 6},
        {"id": 5, "arrival_time": 4, "burst_time": 4}
    ]

    quantum = 2  # Example quantum time

    round_robin(processes, quantum)
