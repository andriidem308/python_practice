MIN_BASE = 1
MAX_BASE = 36

NUMBERS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
    'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25,
    'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
    'Y': 34, 'Z': 35
}


def change_number(number):
    return NUMBERS[number]


def split_number(number):
    return list(map(change_number, list(number)))


def correct_bases(number_list):
    left_bound = max(number_list) + 1
    right_bound = MAX_BASE + 1
    return list(range(left_bound, right_bound))


def calc_value(number_list, base):
    value = 0
    for i, e in enumerate(number_list[::-1]):
        value += e * base**i
    return value


def bases_values(number):
    result_dict = {}
    number_list = split_number(number)
    bases_list = correct_bases(number_list)
    for base in bases_list:
        result_dict[base] = calc_value(number_list, base)

    return result_dict


def get_common(number_1, number_2):
    for base_1, value_1 in bases_values(number_1).items():
        for base_2, value_2 in bases_values(number_2).items():
            if value_1 == value_2:
                return base_1, base_2
    return None, None


def output_result(number_1, base_1, number_2, base_2):
    if base_1 is None or base_2 is None:
        return f"{number_1} is not equal to {number_2} in any base 2..36"

    return f"{number_1} (base {base_1}) = {number_2} (base {base_2})"


while True:
    try:
        x, y = input().split()
    except:
        break

    bx, by = get_common(x, y)
    print(output_result(x, bx, y, by))

