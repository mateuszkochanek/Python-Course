def to_8_bits(string):
    bits = []
    for char in string:
        temp = bin(ord(char))[2:] # odcina na 0b na początku
        temp = '00000000'[len(temp):] + temp
        for bit in temp:
            bits.append(bit)
    return bits

def to_6_bits(string):
    arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    myMap = {}
    i = 0
    while i < 64:
        myMap[arr[i]] = i
        i += 1
    bits = []
    for char in string:
        temp = bin(myMap[char])[2:] # odcina na 0b na początku
        temp = '000000'[len(temp):] + temp
        for bit in temp:
            bits.append(bit)
    return bits

def code(string):
    arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    bits = to_8_bits(string)
    coded = []
    num = []
    num.append(bits[0])
    i = 1
    while i < len(bits):
        if i % 6 == 0:
            coded.append(arr[int(''.join(num), 2)])
            num = []
        num.append(bits[i])
        i += 1
    coded.append(arr[int(''.join(num), 2)])
    return ''.join(coded)

def decode(string):
    bits = to_6_bits(string)
    decoded = []
    num = []
    num.append(bits[0])
    i = 1
    while i < len(bits):
        if i % 8 == 0:
            decoded.append(str(chr(int(''.join(num), 2))))
            num = []
        num.append(bits[i])
        i += 1
    decoded.append(str(chr(int(''.join(num), 2))))
    return ''.join(decoded)


op = 2
if op == 1:
    with open('zad2/test1', "r") as f:
        content = f.read()
    coded = code(content)
    with open('zad2/test1kod', "w") as f:
        f.write(coded)
    print(coded)
else:
    with open('zad2/test1kod', "r") as f:
        content = f.read()
    decoded = decode(content)
    with open('zad2/test1dekod', "w") as f:
        f.write(decoded)
    print(decoded)
