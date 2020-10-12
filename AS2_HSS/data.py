
data = [36, 29, 31, 125, 139, 131, 115, 105, 111, 40, 119, 47, 105, 57, 122, 109, 124, 115, 43, 120, 43, 27, 27, 32, 61, 37,
        127, 29, 113, 121, 58, 114, 126, 53, 114, 96, 12, 127, 28, 42, 39, 113, 42, 18, 44, 18, 28, 48, 125, 107, 114, 34, 133,
        45, 120, 30, 127, 31, 116, 146, 58, 109, 23, 105, 63, 27, 44, 105, 99, 41, 128, 121, 116, 125, 118, 44, 37, 113, 124,
        37, 48, 127, 25, 109, 7, 31, 141, 46, 13, 27, 43, 117, 116, 27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118, 117, 38,
        27, 106, 33, 117, 116, 132, 104, 123, 35, 113, 122, 42, 117, 119, 32, 61, 37, 127, 29, 113, 121, 58, 114, 126, 53,
        114, 96]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  # Finding the mid of the array
        l = array[:mid]  # Dividing the array elements
        r = array[mid:]  # into 2 halves

        merge_sort(l)  # Sorting the first half
        merge_sort(r)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1


# Code to print the list
def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# It returns location of x in given array arr
# if present, else returns -1
def binary_search(array, left, right, key):
    while left <= right:

        mid = left + (right - left) // 2

        # Check if x is present at mid
        if array[mid] == key:
            return mid

            # If x is greater, ignore left half
        elif array[mid] < key:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element
    # was not present
    return -1




