def countingsort(values):
    """
    count sorting with negative numbers
    space complexity O(m+m)
    time complexity O(n + n + (n*m + n*m)) ???
    """

    # O(n)
    max_value = values[0]
    min_value = 0
    for value in values[1:]:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    # Space: O(m)
    counts_max = [0] * (max_value + 1)
    # Space: O(m)
    counts_min = [0] * (abs(min_value) + 1)

	# O(n)
    for value in values:
        if value >= 0:
            counts_max[value] += 1
        else:
            counts_min[abs(value)] += 1

    # O(n * m)
    index = 0
    for i in range(max_value + 1):
        for j in range(counts_max[i]):
            values[index] = i
            index += 1
    for i in range(abs(min_value) + 1):
        for j in range(counts_min[i]):
            values.insert(0, -i)
            values.pop()



val = [7, -2, 7, 3, 0, 5, -1, 3, -3, 1]
# [0,1,3,3,5,7,7]
# [-3,-2,-1]
# [-3, -2, -1, 0, 1, 3, 3, 5, 7, 7]
# [-3, -2, -1, 0, 1, 3, 3, 5, 7, 7]
countingsort(values=val)
print(val)