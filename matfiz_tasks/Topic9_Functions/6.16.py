def reformat(a: str, b: str):
    res = ""
    for ch in a:
        if ch not in b: res += ch
    return res


str_1 = input("line 1: ")
str_2 = input("line 2: ")
str_1 = reformat(str_1, str_2)
print(str_1, "-", str_2)