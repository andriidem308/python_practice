import random


def my_shiny_new_decorator(function_to_decorate):
    def func(*args):
        print('Відкорегований результат:')
        print(abs(function_to_decorate(*args)))

    return func


@my_shiny_new_decorator
def stand_alone_function(*args):
    res = 0
    for arg in args:
        res += arg
    return res


def main():
    stand_alone_function(-1, -2, -3)


if __name__ == '__main__':
    main()
