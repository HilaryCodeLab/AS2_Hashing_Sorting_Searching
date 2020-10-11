import data as dt

data = [36, 29, 31, 125, 139, 131, 115, 105, 111, 40, 119, 47, 105, 57, 122, 109, 124, 115, 43, 120, 43, 27, 27, 32, 61, 37,
        127, 29, 113, 121, 58, 114, 126, 53, 114, 96, 12, 127, 28, 42, 39, 113, 42, 18, 44, 18, 28, 48, 125, 107, 114, 34, 133,
        45, 120, 30, 127, 31, 116, 146, 58, 109, 23, 105, 63, 27, 44, 105, 99, 41, 128, 121, 116, 125, 118, 44, 37, 113, 124,
        37, 48, 127, 25, 109, 7, 31, 141, 46, 13, 27, 43, 117, 116, 27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118, 117, 38,
        27, 106, 33, 117, 116, 132, 104, 123, 35, 113, 122, 42, 117, 119, 32, 61, 37, 127, 29, 113, 121, 58, 114, 126, 53,
        114, 96]


class HashTable:

    def __init__(self, ts):
        # self.table_size = len(ts)
        # Create empty hash table
        # self.hash_table = [None]*ts
        hash_table = [[] for _ in range(len(data))]
        self.hash_table = hash_table
        self.table_size = ts

    def hash_function(self, key):
        return key % len(self.hash_table)

    def insert(self, hash_table, key, value):
        hash_key = self.hash_function(key)
        # using chaining to handle hash function collision
        self.hash_table[hash_key].append(value)

    def __str__(self):
        s = ""
        print("hash table:", end="\n")
        for i in range(self.table_size):
            if self.hash_table[i] is not None:
                print(self.hash_table[i])

        return s


if __name__ == '__main__':
    # table = HashTable(135)
    # dt.merge_sort(data)
    # sorted_list = data
    # table = HashTable(len(sample_data))
    # dt.merge_sort(sample_data)
    # sorted_list = sample_data
    table = HashTable(len(data))
    dt.merge_sort(data)
    sorted_list = data
    print("Sorted array is: ", end="\n")
    dt.print_list(sorted_list)
    for item in sorted_list:
        key = table.hash_function(item)
        table.insert(table.hash_table, key, item)
    print(table)
