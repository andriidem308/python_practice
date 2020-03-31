def decorator(func):
    print('__________________________________')
    print('Результат виконання програми')
    print('----------------------------------')

    def Function(*args):
        for el in args:
            if not el == str(el):
                raise TypeError('\"{0}\" не є рядком.\nАргументами функції можуть бути тільки рядкик'.format(el))
        print('\nОтриманий список:')
        print(func(*args))
    return Function


@decorator
def unique(*args):
    lst = []
    for s in args:
        if s not in lst: lst.append(s)
    return lst


def main():
    unique('abc', '66', 'bbd', 'abc', 'amk', 'lkp', 'bbd')


if __name__ == '__main__':
    main()