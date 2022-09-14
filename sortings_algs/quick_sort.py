def qsort(arr: list, low, high):
    """ Space complexity O(n - 1) """
    if low >= high:
        return
    if len(arr) <= 1:
        return arr

    pivot = arr.pop(low)

    # values less than pivot
    before = []
    # values great than pivot
    after = []

    for i in range(low, high-1):
        if arr[i] < pivot:
            before.append(arr[i])
        else:
            after.append(arr[i])
    

    # sort before part
    for i in range(0, len(before) - 1):
        if before[i] > before[i+1]:
            before[i], before[i+1] = before[i+1], before[i]
    
    # sort after part
    for i in range(0, len(after) - 1):
        if after[i] > after[i+1]:
            after[i], after[i+1] = after[i+1], after[i]
        
    return before + [pivot] + after





arr = [9,11,4,2,10,16,8]
print(qsort(arr, 0, len(arr)))