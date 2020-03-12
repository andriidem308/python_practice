import collections

# creating object of class <deque> filled with 2, 3, 4
dequeue = collections.deque([2, 3, 4])

# output <dequeue>
print(dequeue)

dequeue.append(5)       # append at right end -->   [2, 3, 4, 5]
dequeue.appendleft(1)   # append at left end -->    [1, 2, 3, 4, 5]
dequeue.pop()           # delete from right end --> [1, 2, 3, 4]
dequeue.popleft()       # delete from left end -->  [2, 3, 4]

print(dequeue)
