# Already taken time 1:08:14
# https://visualgo.net/en/heap
def heapify(array, i):
    left = 2 * i
    right = 2 * i + 1
    root = i
    if left <= len(array) and array[left] > array[root]:
        array[root] = array[left]
    if array[right] <= len(array) and array[right] > array[root]:
        array[root] = array[right]
    


def sort_heap(array):
    pass



arr = [9,11, 4 , 2, 1, 10, 8, 6, 5, 16]

print(heapify(arr))