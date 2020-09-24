with open('../file', 'r') as f:
    content = f.read()
print("Całkowita liczba bajtów:", sum((int((tab.split(" "))[-1]) for tab in content.split("\n"))))