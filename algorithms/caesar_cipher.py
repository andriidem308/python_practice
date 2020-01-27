LETTERS = "abcdefghijklmnopqrstuvwxyz"


def _prepare_dict(key):
    result_dict = {" ": "*"}
    for i in range(len(LETTERS)):
        result_dict[LETTERS[i]] = LETTERS[(i + key) % len(LETTERS)]
    return result_dict


def encode(line, key):
    cezar_dict = _prepare_dict(key)
    result_line = ""
    for letter in line.lower():
        if letter in cezar_dict.keys():
            result_line += cezar_dict[letter]
        else:
            result_line += letter
    return result_line


print(encode("Boeing-777", 7))