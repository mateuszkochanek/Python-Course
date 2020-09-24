import os
import sys

def lower_case_rename(directory, fileName):
    os.rename(os.path.join(directory, fileName), os.path.join(directory, fileName.lower()))

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for name in files:
        lower_case_rename(root, name)
    for name in dirs:
        lower_case_rename(root, name)
