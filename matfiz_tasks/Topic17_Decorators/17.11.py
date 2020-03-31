def counter(func):

    if not hasattr(counter, 'count'):
        counter.count = {}
    counter.count[func.__name__] = 0

    def wrapper(a):
        res = func(a)
        counter.count[func.__name__] += 1
        print('{0} була викликана {1} разів, рез: {2}'.format(func.__name__, counter.count[func.__name__], res))
        return res

    return wrapper


@counter
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@counter
def factorial(n):
    if n == 1 or n == 0: return 1
    elif n > 1: return n*factorial(n-1)


def main():
    print(fibonacci(7))
    print()
    print(factorial(5))


if __name__ == '__main__':
    main()