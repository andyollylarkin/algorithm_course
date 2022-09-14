def bubblesort(array):
    """
    Алгоритм пузырьковой сортировки массива в прямом порядке.
    """

    # Модифицируйте алгоритм.
    is_sorted = False
    while not is_sorted:

        is_sorted = True
        n = 1

        for i in range(len(array) - n):
            if array[i] < array[i + 1]: # difference between direct and reverse '>' and '<' operator
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        n += 1
    return array

# array = [13, 7, 8, 2, 11, 5]
# # [13, 11, 8, 7, 5, 2]
# print(bubblesort(array))