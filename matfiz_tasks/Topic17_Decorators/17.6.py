def decor(func):
    def wrapper(*args,**kwargs):
        if len(kwargs) > 0:
            raise EnvironmentError
        print('Результат: ')
        return func(*args, **kwargs)
    return wrapper

@decor
def my_func(*args,**kwargs):
    temp = max(args)
    s = 0
    for e in args:
        s += e
    if temp > s: return 1
    else: return s

def main():
    print(my_func(1, 2, 3))


if __name__ == '__main__':
    main()
