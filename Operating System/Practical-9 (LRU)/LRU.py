def lru_page_replacement(pages, capacity):
    page_faults = 0
    cache = []

    for page in pages:
        if page not in cache:
            page_faults += 1
            if len(cache) == capacity:
                cache.pop(0)
            cache.append(page)
        else:
            cache.remove(page)
            cache.append(page)

    return page_faults

if __name__ == "__main__":
    pages = [1, 3, 0, 3, 5, 6, 3]
    capacity = 3

    page_faults = lru_page_replacement(pages, capacity)
    print(f"Total Page Faults: {page_faults}")
