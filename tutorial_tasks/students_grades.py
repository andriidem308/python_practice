def get_sum(_array: list, _index: int):
    pass


def input_info(_students: list, _amount: int):
    for i in range(_amount):
        surname = input("Surname: ")
        group_name = input("Group: ")
        marks_list = list(map(int, input("Marks List: ").split()))

        _students.append((
            surname,
            group_name,
            marks_list[0], marks_list[1], marks_list[2]
        ))


def get_avg(gr_list: list):
    return gr_list[0] / gr_list[1] / 3


def get_groups(_students_lst: list):
    groups = dict()

    for student in _students_lst:
        gr_name = student[1]
        marks_sum = sum(student[2:4])
        if gr_name not in groups.items():
            groups[gr_name] = [marks_sum, 1]
        else:
            groups[gr_name] += [marks_sum, 1]

    return groups


def find_best_group_(_students_lst: list):
    _groups = get_groups(_students_lst)
    max_avg = 0
    best_group = ""
    for key, value in _groups.items():
        avg = get_avg(value)
        if avg > max_avg:
            max_avg = avg
            best_group = key
    return best_group, max_avg


def find_best_group(_groups: dict):
    max_avg = 0
    best_group = ""
    for key, value in _groups.items():
        avg = get_avg(value)
        if avg > max_avg:
            max_avg = avg
            best_group = key
    return best_group, max_avg


def output_students(_students_lst: list):
    key, value = find_best_group_(_students_lst)
    print("The best group:", key)
    print("Their avg:", value)


students = [
    ("Andrii", "A", 5, 5, 5),
    ("Lexa", "A", 4, 4, 4),
    ("Tolik", "B", 3, 5, 3),
    ("Bodich", "A", 5, 4, 5),
    ("Chicha", "A", 5, 5, 5),
    ("Yarik", "A", 4, 4, 5),
    ("Sanya", "A", 5, 5, 4),
    ("Vlados", "C", 4, 5, 5),
    ("Nastia", "B", 5, 3, 5),
    ("Liza", "C", 5, 5, 5),
    ("Denis", "C", 2, 2, 5),
    ("Kolya", "C", 4, 5, 3),
]

# amount = int(input("amount of groups: "))

output_students(students)

