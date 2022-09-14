def bubblesort(array):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        idx = 0
        for i in range(0, len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = False
            idx += 1
    return array

array = [13, 7, 8, 2, 11, 5]
print(bubblesort(array))