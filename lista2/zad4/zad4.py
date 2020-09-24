import hashlib
import os
import sys

def file_sign(root, name):
    path = os.path.join(root, name)
    with open(path, 'r') as f:
        content = f.read()
    return [path, os.stat(path).st_size, hashlib.md5(content.encode()).hexdigest()]



li = []
for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for name in files:
        li.append(file_sign(root, name))
print("---------------------------")
i = 0
j = 0
wz = 0
while i < len(li):
    j = i + 1
    wz = 0
    while j < len(li):
        if (li[i][1] == li[j][1]) and (li[i][2] == li[j][2]) and (li[i][1] != -1):
            print(li[j][0])
            li[j][1] = -1
            wz = 1
        j += 1
    if wz == 1:
        print(li[i][0])
        li[i][1] = -1
        print("---------------------------")
    i += 1
