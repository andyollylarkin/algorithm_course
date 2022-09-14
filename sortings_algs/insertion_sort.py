from readline import insert_text


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        while arr[j + 1] < arr[j] and j >= 0:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
        i += 1
    return arr


print(insertion_sort([8,4,2,5,10,1,4]))