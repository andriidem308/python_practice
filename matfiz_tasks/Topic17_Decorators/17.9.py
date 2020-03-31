def decorator(func):
    global results
    results = dict()

    def wrapper(*args):
        a = None
        for el in args:
            a = el
            if el in results:
                print('Таке вже є: {0}:{1}'.format(el, results[el]))
            else:
                results[el] = func(el)
                print(results[el])
        return results[a]
    return wrapper


@decorator
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(7))


if __name__ == '__main__':
    main()