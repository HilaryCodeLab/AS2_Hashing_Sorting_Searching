def identity(element):
    return element


def find_index(elements, value, key):
    """

    :param elements: array
    :param value: string
    :param key: object attribute
    :return: array element
    """
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


def find(elements, value, key=identity):
    """

    :param elements: array
    :param value: string
    :param key: array index
    :return: none or array element
    """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]
