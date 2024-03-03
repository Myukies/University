def fcfs(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process['id']}\t{process['burst_time']}\t\t", end='')

        waiting_time = current_time - process['arrival_time']
        if waiting_time < 0:
            waiting_time = 0

        print(f"{waiting_time}\t\t", end='')

        turnaround_time = waiting_time + process['burst_time']
        print(turnaround_time)

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        current_time += process['burst_time']

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


if __name__ == "__main__":
    processes = [
        {"id": 1, "arrival_time": 0, "burst_time": 5},
        {"id": 2, "arrival_time": 1, "burst_time": 3},
        {"id": 3, "arrival_time": 2, "burst_time": 8},
        {"id": 4, "arrival_time": 3, "burst_time": 6},
        {"id": 5, "arrival_time": 4, "burst_time": 4}
    ]

    fcfs(processes)
