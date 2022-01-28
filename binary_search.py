def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while (start <= end):
        middle = (start + end) // 2
        guess = list[middle]

        if guess == item:
            return middle

        if guess > item:
            end = middle - 1
        else:
            start = middle + 1
    return None


my_list = [1, 3, 5, 7, 9, 11]

print(binary_search(my_list, -11))
