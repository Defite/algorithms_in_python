list = [1, 2, 3, 4, 5]


def sum(list):
    """Sums all numbers in list

    Args:
        list ([number]): list of numbers

    Returns:
        [number]: sum of all numbers in list
    """
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])


print('sum', sum(list))


def count(list):
    """Count length of list

    Args:
        list ([number]): list of numbers
    """

    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print('List length', count(list))


def findBiggest(list):
    """Finds biggest number in the list

    Args:
        list ([number]): list of numbers
    """

    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        biggest = findBiggest(list[1:])

    return list[0] if list[0] > biggest else biggest


print('Biggest number', findBiggest(list))
