import heapq


# H = [9, 4, 3, 11, 24, 18, 7, 10, 13]
H = [4, 8, 3, 19, 2, 7]


# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H, 8)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H, 6)
print(H)
