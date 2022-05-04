def hash_function(key, size):
    return key % size


def rehash(old_hash, size):
    return (old_hash + 1) % size


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def get(self, key):
        start_slot = hash_function(key, len(self.slots))

        value = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                value = self.data[position]
            else:
                position = rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


H = HashTable()
H[20] = "cat"
H[71] = "dog"
H[5] = "chicken"
H[31] = "cock"
H[32] = "cock2"
H[30] = "cock0"

print(H.slots)
print(H.data)

print(H[30])
print(H[31])
print(H[32])


