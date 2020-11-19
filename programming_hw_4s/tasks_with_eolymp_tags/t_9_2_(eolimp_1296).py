max_mlt = 0


def find_maxmult(sub_num, mult, tmp_parts):
    global max_mlt

    tmp = mult * int(sub_num)
    if tmp < max_mlt: return
    if tmp_parts == 1:
        max_mlt = tmp
        return

    for i in range(1, len(sub_num) - tmp_parts + 2):
        find_maxmult(sub_num[i:], mult * int(sub_num[:i]), tmp_parts - 1)


def procedure(number, parts):
    global max_mlt
    max_mlt = 0

    find_maxmult(str(number), 1, parts)
    return max_mlt


res_lst = []

with open('input.txt') as file_in:
    for line in file_in:
        n, m = map(int, line.strip().split())
        res_lst.append(procedure(n, m))

with open('output.txt', 'w') as file_out:
    for r in res_lst: file_out.write(str(r) + "\n")
