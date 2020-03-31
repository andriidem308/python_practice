def f(*args, **kwargs):
    try:
        assert len(kwargs) == len(args)

        list_of_x = args
        list_of_y = list(kwargs.values())

        sum = 0
        for i in range(len(args)):
            sum += list_of_x[i]**2 + list_of_y[i]**2 + list_of_x[i]*list_of_y[i]

        return sum
    except AssertionError:
        print('Кількість х не відповідає к-ті у!!!')



print(f(1,2,3,y1=4,y2=5,y3=6))