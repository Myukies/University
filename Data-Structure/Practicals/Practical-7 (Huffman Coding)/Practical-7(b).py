import heapq
from collections import defaultdict

def build_huffman_tree(freq_map):
    heap = [[weight, [symbol, ""]] for symbol, weight in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def huffman_coding(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1
    
    huffman_tree = build_huffman_tree(freq_map)
    
    for symbol, code in huffman_tree:
        print(f"Symbol: {symbol}, Code: {code}")

user_input = input("Enter a string: ")
huffman_coding(user_input)