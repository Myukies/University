def fifo(page_references, num_frames):
    frame_queue = []  
    page_faults = 0  

    for page in page_references:
        if page not in frame_queue:
            if len(frame_queue) < num_frames:
                frame_queue.append(page)
            else:
                oldest_page = frame_queue.pop(0)
                print(f"Page {oldest_page} removed from memory")
                frame_queue.append(page)

            page_faults += 1

        print(f"Page {page}: Memory -> {frame_queue}")

    return page_faults

if __name__ == "__main__":
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    num_frames = 3

    print("FIFO Page Replacement Algorithm Simulation")
    print(f"Number of Frames in Memory: {num_frames}")
    print("\nPage Reference Sequence:")

    for page in pages:
        print(page, end=" ")

    print("\n\nSimulation Steps:")

    page_faults = fifo(pages, num_frames)
    print(f"\nTotal page faults: {page_faults}")
