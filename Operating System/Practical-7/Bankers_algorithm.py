def bankers_algorithm(allocated, max_needed, available):
    num_processes = len(allocated)
    num_resources = len(available)

    work = available.copy()
    finish = [False] * num_processes
    safe_sequence = []

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(allocated[i][j] + work[j] >= max_needed[i][j] for j in range(num_resources)):
                work = [work[j] + allocated[i][j] for j in range(num_resources)]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            break

    return safe_sequence if all(finish) else None

allocated = [
    [1, 2, 2],
    [1, 0, 3],
    [1, 2, 1]
]
max_needed = [
    [3, 3, 2],
    [1, 2, 3],
    [1, 3, 5]
]
available = [3, 3, 2]

safe_sequence = bankers_algorithm(allocated, max_needed, available)

print("Safe sequence:", safe_sequence) if safe_sequence else print("No safe sequence found. System is in an unsafe state.")
