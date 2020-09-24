def subsets(arr):
    if not arr:
        return [[]]
    return subsets(arr[1:]) + [[arr[0]] + x for x in subsets(arr[1:])]

def subsets_v2(arr):
    if not arr:
        return [[]]
    return subsets(arr[1:]) + list(map(lambda x: [arr[0]] + x ,subsets_v2(arr[1:])))

li = [1,2,3,4]
print(subsets(li))
print(subsets_v2(li))