import numpy as np
"""
# t = np.array([(1, 2, 5), (3, 4, 7)], dtype=[('a', '<i4'), ('b', '<i4'), ('c', '<i4')])


#  ____0____ ____1____  _____2_____  _____3_____   ______4______   ____5____  ___6___
#  <Surname> <Ecology> <Philosophy> <Programming> <Combinatorics> <Calculus> <Algebra>
students = np.array([
    ['Demchenko', 5, 4, 5, 5, 4, 4],  # index: 0
    ['Nikiforov', 5, 4, 5, 5, 5, 4],  # index: 1
    ['Troshchy', 5, 4, 5, 5, 5, 4],  # index: 2
    ['Korinovsky', 5, 4, 5, 5, 4, 4],  # index: 3
    ['Chicha', 5, 4, 5, 5, 4, 3]  # index: 4
])

# stud_matrix = np.reshape(students, (5, 7))

print(students[4][0], "'s marks: ", students[4][1:], sep='')  # print data for <Chicha>
print(students[1][0], "'s Philosophy mark: ", students[1][2], sep='')  # print data for <Nikiforov's Philosophy>
"""


a = np.array([[1, 1], [2, 2], [3, 3]])
b = a.flatten()

print(np.insert(b, [0, 6], [5, 6]))
print(np.insert(b, [2, 2], [7.13, False]))



