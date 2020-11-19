LETTERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l")


def make_words(space):
    words = []

    if len(space) == 1:
        return space
    else:
        for i in range(len(space)):
            for perm in make_words(space[:i] + space[i + 1:]):
                words += [space[i] + perm]

    return words


n, k = map(int, input().split())
letters = LETTERS[:n]

words_list = make_words(letters)

print(words_list[k - 1])