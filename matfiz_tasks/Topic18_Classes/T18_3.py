class Genre:
    def __init__(self, name_gen=None, characteristic_features=None):
        self.name_genre = name_gen
        self.charecteristic_features = characteristic_features

    def input(self):
        self.name_genre = input("Input name of genre: ")
        self.charecteristic_features = input("Input charecteristic features: ")

    def output(self):
        print("Film has ", self.name_genre, " genre, and has ", self.charecteristic_features,
              " charecteristic features.")


class Carrier:
    def __init__(self, type_carrier=None, c_scheme=None, duration=None):
        self.type_carrier = type_carrier
        self.color_scheme = c_scheme
        self.duration_of_storage = duration

    def input(self):
        self.type_carrier = input("Input type of carrier: ")
        self.color_scheme = input("Input color scheme: ")
        self.duration_of_storage = int(input("Input duration of storage(in days): "))

    def output(self):
        print("Film is on ", self.type_carrier, " carrier type. Carrier has ", self.color_scheme,
              " color scheme.\nMovie will storage more ", self.duration_of_storage, " days.")


def make_quotes(plaintext):
    return "\"" + str(plaintext) + "\""


class Movie(Genre, Carrier):
    def __init__(self, name=None, written_by=None, producer=None, film_duration=None,
                 name_gen=None, characteristic_features=None,
                 type_carrier=None, c_scheme=None, duration=None
                 ):
        self.name = name
        self.written_by = written_by
        self.producer = producer
        self.film_duration = film_duration
        Genre.__init__(self, name_gen, characteristic_features)
        Carrier.__init__(self, type_carrier, c_scheme, duration)

    def input(self):
        self.name = input("Name of film: ")
        self.written_by = input("Film was written by: ")
        self.producer = input("Producer of the film: ")
        self.film_duration = int(input("Input film duration in minute: "))
        Genre.input(self)
        Carrier.input(self)

    def bibliothek(self):
        lst = [self.name, self.written_by, self.producer, self.film_duration, self.name_genre,
               self.charecteristic_features, self.type_carrier, self.color_scheme, self.duration_of_storage]
        lst = [make_quotes(pt) for pt in lst]
        res = " ".join(lst)
        return res

    def test(self):
        lst = [self.name, self.written_by, self.producer, self.film_duration, self.name_genre,
               self.charecteristic_features, self.type_carrier, self.color_scheme, self.duration_of_storage]
        lst = [make_quotes(pt) for pt in lst]
        res = " ".join(lst)
        return res

    def output(self):
        print("Name of film is ", self.name, ". It was written by ", self.written_by, ".\nHis producer was ",
              self.producer, ". Film duration is ", self.film_duration, " minute.")
        Genre.output(self)
        Carrier.output(self)
        print("\n")


file_name = "bibliothek.txt"

file = open(file_name, 'r')
s = file.readlines()
file.close()

file = open(file_name, 'a')

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
        objects.append(Movie)
        objects[total_films - 1].input()
        objects[total_films - 1].output()
        file.write('\n')
        file.write(objects[total_films - 1].bibliothek())
        total_films += 1
        print("Done\n\n\n")


    elif chooser_option == 0:
        print("Thank you for your participatipon.Bue!")
        break
    else:
        print("Incorrect input try again!")

file.close()
