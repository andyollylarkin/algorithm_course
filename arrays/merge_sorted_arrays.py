def merge(array1, array2):
    """
    Insertion sort
    Time complexity O(n)
    Space complexity O(m+n)
    """
    array3 = array1 + array2
    i = 0
    while i < len(array3) - 1:
        if array3[i] > array3[i+1]:
            array3[i], array3[i+1] = array3[i+1], array3[i]
            if i - 1 >= 0: # if decrease counter great than lower bound -> rollback one step
                i -= 1
            continue
        else:
            i += 1
    return array3