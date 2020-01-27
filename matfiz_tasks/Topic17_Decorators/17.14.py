def decorator(function):
    def wrapper(*args):
        res = function(*args)
        return list(set(res))
    return wrapper


@decorator
def f(filename):
    file = open(filename)
    text_lst = file.read().split(' ')
    return text_lst


print(f('17.14_in.txt'))
