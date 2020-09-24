def qsort_v2(arr):
    if len(arr) <= 1:
        return arr
    return qsort_v2(list(filter(lambda x: x < arr[0],arr[1:]))) + [arr[0]] + qsort_v2(list(filter(lambda x: x >= arr[0],arr[1:])))

def qsort(arr):
    if len(arr) <= 1:
        return arr
    return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])

li = [5, 1, 9, 2, 8, 3, 7, 6, 8]
print(qsort_v2(li))