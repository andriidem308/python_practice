def decorator_protector_repeat(func):
    def wrapper(*args,**kwargs):
        allelements = func(*args,**kwargs)
        res = []
        for e in allelements:
            if e not in res: res.append(e)
        return res
    return wrapper

@decorator_protector_repeat
def f(file_name):
    list_of_words = []
    s = open(file_name, 'rt')
    #s = 'Showdown your skills like cat like kitty cat dog your'
    list_of_words = s.read().split()
    return list_of_words

print(f('textfor_decorator.txt'))

