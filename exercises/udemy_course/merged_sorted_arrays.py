from typing import List


def merge_sorted_arrays_recursively(a: List[int], b: List[int]):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    if a[0] <= b[0]:
        return [a[0]] + merge_sorted_arrays_recursively(a[1:], b)
    
    return [b[0]] + merge_sorted_arrays_recursively(a, b[1:])


def merge_sorted_arrays(a: List[int], b: List[int]):

    merged_array = []

    while len(a) > 0 and len(b) > 0:

        if a[0] <= b[0]:
            merged_array.append(a.pop(0))
            
        else:
            merged_array.append(b.pop(0))

    merged_array.extend(a)
    merged_array.extend(b)

    return merged_array


if __name__ == '__main__':
    for merge_arrays in (merge_sorted_arrays, merge_sorted_arrays_recursively):
        assert merge_arrays([0, 3, 4, 31], [4,6,30]) == [0, 3, 4, 4, 6, 30, 31] 
        assert merge_arrays([4,6,30], [0, 3, 4, 31]) == [0, 3, 4, 4, 6, 30, 31]

        assert merge_arrays([0, 3, 4, 23, 41], []) == [0, 3, 4, 23, 41]
        assert merge_arrays([], [0, 3, 4, 23, 41]) == [0, 3, 4, 23, 41]
        assert merge_arrays([], []) == []

        assert merge_arrays([], []) == []
        assert merge_arrays([0, 3, 4, 23, 41], []) == [0, 3, 4, 23, 41]
        assert merge_arrays([], [0, 3, 4, 23, 41]) == [0, 3, 4, 23, 41]
        assert merge_arrays([0, 3, 4, 31], [4,6,30]) == [0, 3, 4, 4, 6, 30, 31] 

