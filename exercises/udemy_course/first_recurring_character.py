
def first_recurring_character(arr):
    """
    Given an array, should return the first recurring character from it.

    Example: [2,5,1,2,3,5,1,2,4]
    Should return 2.

    Example: [2,3,4,5]
    Should return - 1, since all elements are distinct

    :param arr: Array of positive integers or strings
    :return: The first recurring character
    """
    characters_iterated = set()

    for el in arr:
        if el in characters_iterated:
            return el
        characters_iterated.add(el)
    return -1


if __name__ == '__main__':
    assert first_recurring_character([2,5,1,2,3,5,1,2,4]) == 2
    assert first_recurring_character([2,3,4,5]) == -1
