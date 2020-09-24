import os
num_lines = 0
maxx = -1
with open('test1', 'r') as f:
    for line in f:
        num_lines += 1
        if len(line) > maxx:
            maxx = len(line)
    f.seek(0)
    content = f.read()
#print(content)
words = content.split()

print('liczba bajtów :', os.stat('test2').st_size)
print('liczba słów :', len(words))
print('liczba lini :', num_lines)
print('maksymalna długość linii (razem z \\n) :', maxx)
