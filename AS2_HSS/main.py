import hash_table as ht
import data as dt


if __name__ == '__main__':
    table = ht.HashTable(len(dt.data))
    dt.merge_sort(dt.data)
    sorted_list = dt.data
    print("Sorted array is: ", end="\n")
    dt.print_list(sorted_list)
    for item in sorted_list:
        key = table.hash_function(item)
        table.insert(table.hash_table, key, item)
    print(table)

