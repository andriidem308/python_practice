def find_period(a, b):
    before = str(a // b) + "."
    ans = ''
    indexes = {}
    index = 0
    a = a % b
    indexes[a] = index

    while True:
        if a == 0:
            break

        digit = a * 10 // b
        a = a * 10 - digit * b

        if a not in indexes:
            ans += str(digit)
            index += 1
            indexes[a] = index
        else:
            ans += str(digit)
            ans = ans[:indexes[a]] + '(' + ans[indexes[a]:] + ')'
            break
    return before + ans


input_data = input()
n, d = 1, 1
if '/' in input_data:
    n, d = map(int, input_data.split('/'))
elif ',' in input_data:
    n, d = map(int, input_data.split(','))
elif ' ' in input_data:
    n, d = map(int, input_data.split())
else:
    raise IOError('Bad input format!')

print(find_period(n, d))
