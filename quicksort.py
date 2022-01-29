def quicksort(array):
    """Quick Sort algorithm with zero element as pivot

    Args:
        array ([number]): array of numbers

    Returns:
        [array]: sorted array of numbers
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print('pivot', pivot)
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([100, 20, 80, 9, 10, 35, 40]))
