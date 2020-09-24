def flatten(li):
    for element in li:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element

li = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(li)))