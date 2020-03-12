def decorator_type(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                print("Incorrect Attribute!")
                exit(0)
            x = self.oInstance.__getattribute__(s)
            print(type(x))

    return NewCls


@decorator_type
class Human:
    def __init__(self):
        self.name = input("Input name: ")
        self.surname = input("Input surname: ")
        self.age = int(input("Input age: "))
        self.love = True if input("Input is human fall in love: ") == 'yes' else False

    def age_after_5_years(self):
        return self.age + 5

    def output(self):
        print(f"After 5 years, {self.name} {self.surname} will be: {self.age_after_5_years()}")


object = Human()
object.output()
