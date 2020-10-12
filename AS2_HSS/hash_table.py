import data as dt


class HashTable:

    def __init__(self, ts):
        hash_table = [[] for _ in range(len(dt.data))]
        self.hash_table = hash_table
        self.table_size = ts

    def hash_function(self, key):
        # return key % len(self.hash_table)
        _hash = key // 10
        return _hash

    def insert(self, hash_table, key, value):
        leaf = value % 10
        # using chaining to handle hash function collision
        # self.hash_table[key].append(leaf)
        hash_table[key].append(leaf)

    def __str__(self):
        s = ""

        print('Stem | Leaf', end="\n")
        for i in range(self.table_size):
            if self.hash_table[i] is not None:
                print(i, self.hash_table[i])

        return s
