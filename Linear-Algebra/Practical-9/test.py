import numpy as np

n = 4 
transition_matrix = np.array([
    [0, 0, 0.5, 0],
    [0.5, 0, 1, 0.5],
    [0, 0.5, 1, 0.5],
    [0.5, 0.5, 0.5, 0]
])

damping_factor = 0.85

page_rank = np.ones(n) / n

max_iterations = 100

epsilon = 1e-6

for _ in range(max_iterations):
    prev_page_rank = page_rank.copy()
    page_rank = (1 - damping_factor) / n + damping_factor * np.dot(transition_matrix.T, page_rank)

    if np.linalg.norm(page_rank - prev_page_rank) < epsilon:
        break

print("PageRank values:")
for i, pr in enumerate(page_rank):
    print(f"Page {i + 1}: {pr:.4f}")
