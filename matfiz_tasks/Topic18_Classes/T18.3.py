class Genre:
    def __init__(self, genre_name=None, features=None):
        self.genre_name = genre_name
        self.features = features

    def input(self):
        self.genre_name = input("Genre name: ")
        self.features = input("Features: ")

    def output(self):
        print(f"Genre: {self.genre_name}\nFeatures: {self.features}")


class Carrier:
    def __init__(self, storage_type=None, color_scheme=None, valid_time=None):
        self.storage_type = storage_type
        self.color_scheme = color_scheme
        self.valid_time = valid_time

    def input(self):
        self.storage_type = input("Storage type: ")
        self.color_scheme = input("Color Scheme: ")
        self.valid_time = int(input("Valid time (days): "))

    def output(self):
        print(f"Storage: {self.storage_type}\nColor: {self.color_scheme}\nValid time: {self.valid_time}")


def make_quotes(plaintext):
    return "\"" + str(plaintext) + "\""


class Movie(Genre, Carrier):
    def __init__(self, name=None, author=None, producer=None, film_duration=None,
                 genre_name=None, features=None,
                 storage_type=None, color_scheme=None, valid_time=None
                 ):
        self.name = name
        self.author = author
        self.producer = producer
        self.film_duration = film_duration
        Genre.__init__(self, genre_name, features)
        Carrier.__init__(self, storage_type, color_scheme, valid_time)

    def input(self):
        self.name = input(f"Film name: ")
        self.author = input("Film Author: ")
        self.producer = input("Film Producer: ")
        self.film_duration = int(input("Film duration: "))
        Genre.input(self)
        Carrier.input(self)

    def bibliothek(self):
        lst = [self.name, self.author, self.producer, self.film_duration, self.genre_name,
               self.features, self.storage_type, self.color_scheme, self.valid_time]
        lst = [make_quotes(pt) for pt in lst]
        res = " ".join(lst)
        return res

    def test(self):
        lst = [self.name, self.author, self.producer, self.film_duration, self.genre_name,
               self.features, self.storage_type, self.color_scheme, self.valid_time]
        lst = [make_quotes(pt) for pt in lst]
        res = " ".join(lst)
        print(res)
        return res

    def output(self):
        print(f"\nName: {self.name}\nAuthor: {self.author}\nProducer: {self.producer}\nDuration: {self.film_duration}")
        Genre.output(self)
        Carrier.output(self)
        print("\n")


file_name = "bibliothek.txt"

file = open(file_name, 'r')
s = file.readlines()
file.close()

objects = []
total_films = 0

for line in s:
    total_films += 1
    name = ""
    written_by = ""
    producer = ""
    film_duration = ""
    name_gen = ""
    characteristic_features = ""
    type_carrier = ""
    c_scheme = ""
    duration = ""
    checker = 0
    inputer = ""
    for i in range(len(line)):
        if line[i] == '\"':
            if checker == 0:
                checker = 1
                continue
            else:
                checker = 0
                if name == "":
                    name = inputer
                elif written_by == "":
                    written_by = inputer
                elif producer == "":
                    producer = inputer
                elif film_duration == "":
                    film_duration = inputer
                elif name_gen == "":
                    name_gen = inputer
                elif characteristic_features == "":
                    characteristic_features = inputer
                elif type_carrier == "":
                    type_carrier = inputer
                elif c_scheme == "":
                    c_scheme = inputer
                elif duration == "":
                    duration = inputer
                inputer = ""
                continue
        if checker == 1:
            inputer += line[i]

    objects.append(
        Movie(name, written_by, producer, film_duration, name_gen, characteristic_features, type_carrier, c_scheme,
              duration))

chooser_option = -1
print("Wellcome to our Bibliothek!!!!")
while True:
    print("Main Menu:")
    print("Input 1 to see full Bibliothek!\nInput 2 to use search\nInput 3 to add your film\nInput 0 to exit")
    chooser_option = int(input("Input here: "))
    if chooser_option == 1:
        for i in range(total_films):
            print(i + 1, " Film is:")
            objects[i].output()
        print("\n\n\n")
    elif chooser_option == 2:
        pass
    elif chooser_option == 3:
        file = open(file_name, 'a')
        objects.append(Movie)
        objects[total_films - 1].input()
        objects[total_films - 1].output()
        file.write('\n')
        file.write(objects[total_films - 1].bibliothek())
        total_films += 1
        file.close()
        print("Done\n\n\n")


    elif chooser_option == 0:
        print("Thank you for your participatipon.Bue!")
        break
    else:
        print("Incorrect input try again!")


