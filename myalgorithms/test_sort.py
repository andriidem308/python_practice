from myalgorithms import sorts

list_1 = [2, 3, 5, 7, 9]
list_2 = [1, 5, 6, 6, 8]

# list_3 = sorts._merge(list_1, list_2)
list_3 = [2, 3, 1, 5, 9, 7, 2, 8, 4, 2]
a = [8, 5, 4, 7, 9, 1, 2]
sorts.merge_sort_1(a)
print(a)

pos_1 = sorts.binary_search(a, -2)
pos_2 = sorts.binary_search(a, 3)
pos_3 = sorts.binary_search(a, 1)
pos_4 = sorts.binary_search(a, 7)
pos_5 = sorts.binary_search(a, 9)
pos_6 = sorts.binary_search(a, 15)

print(pos_1)
print(pos_2)
print(pos_3)
print(pos_4)
print(pos_5)
print(pos_6)