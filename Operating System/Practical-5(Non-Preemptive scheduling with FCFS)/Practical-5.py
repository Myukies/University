process_list = [
    {"name": "P1", "arrival_time": 0, "burst_time": 10},
    {"name": "P2", "arrival_time": 2, "burst_time": 5},
    {"name": "P3", "arrival_time": 4, "burst_time": 8},
    {"name": "P4", "arrival_time": 6, "burst_time": 3}
]

current_time = 0
total_waiting_time = 0

print("Process\tStart Time\tEnd Time\tWaiting Time")

for process in process_list:
    waiting_time = max(0, current_time - process["arrival_time"])
    total_waiting_time += waiting_time

    current_time += process["burst_time"]

    print(f"{process['name']}\t{max(current_time - process['burst_time'], process['arrival_time'])}\t\t{current_time}\t\t{waiting_time}")

average_waiting_time = total_waiting_time / len(process_list)
print("\nAverage Waiting Time:", average_waiting_time)
