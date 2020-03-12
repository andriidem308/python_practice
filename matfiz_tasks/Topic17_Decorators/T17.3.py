def argskwargs_dec(somefunc):
    def inner_func(*args, **kwargs):
        try:
            r = somefunc(*args, **kwargs)
            assert len(args) == len(kwargs)
            print("lengths of args and kwargs are similar")
            print('Result:', r)
        except AssertionError:
            print("ERROR! Lengths of args and kwargs are different")
    return inner_func


@argskwargs_dec
def argskwargs(*args, **kwargs):
    res = 1
    for x, y in zip(args, kwargs.values()):
        res *= x + 1/y
    return res
    
argskwargs(1,2,a=4,b=5,c=6)
