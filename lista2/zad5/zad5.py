from random import randrange
import os
import sys
import math
from Crypto.Util.number import *


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x

def MillerRabin_test(n, r, d):
    a = randrange(2, n-2)
    x = pow(a, d, n)
    if (x == 1) or (x == n-1):
        return False
    for i in range(r):
        x = (x*x)%n
        if x == n-1:
            return False
        i += 1
    return True


def get_random_prime(bit_count):
    notPrime = True
    while notPrime:
        n = getRandomNBitInteger(bit_count)
        if n % 2 == 0:
            n -= 1
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for i in range(20):
            notPrime = MillerRabin_test(n, r, d)
            if notPrime:
                break
        if not notPrime:
            return n

def gen_keys(bit_count):
    bit_count = int(math.log(2)/math.log(10)*(int(bit_count)))
    p = get_random_prime(bit_count)
    q = get_random_prime(bit_count)
    n = p*q
    nPhi = (p-1)*(q-1)

    e = randrange(2, nPhi-1)
    g = gcd(e, nPhi)
    while g != 1:
        e = randrange(2, nPhi-1)
        g = gcd(e, nPhi)

    d = modInverse(e, nPhi)

    return [e, n, d, n]

def to_8_bits(string):
    bits = []
    for x in string:
        temp = bin(ord(x))[2:] # odcina na 0b na początku
        temp = '00000000'[len(temp):] + temp
        for bi in temp:
            bits.append(bi)
    return "".join(bits)

def encrypt(keys, message):
    key = int(keys[0])
    n = int(keys[1])
    cipher = ""
    num = ""
    i = 0
    message = to_8_bits(message)
    while i < len(message):
        num = num + message[i:i+8]
        if int(num, 2) >= n:
            cipher = cipher + str(pow(int(num[0:-8], 2), key, n))
            cipher = cipher + " "
            num = ""
            i -= 8
        i += 8
    cipher = cipher +  str(pow(int(num, 2), key, n))
    return cipher

def decrypt(keys, cipher):
    key = int(keys[0])
    n = int(keys[1])
    plaintext = ""
    cipher = cipher.split(" ")
    bincipher = ""
    print(cipher)
    for x in cipher:
        xbin = format(pow(int(x), key, n), 'b')
        while len(xbin) % 8 != 0:
            xbin = "0" + xbin
        bincipher = bincipher + xbin
    print(bincipher)
    char = ""
    for bi in bincipher:
        char = char + bi
        if len(char) == 8:
            plaintext = plaintext + chr(int(char, 2))
            char = ""
    return plaintext

if sys.argv[1] == '--gen_keys':
    keys = gen_keys(sys.argv[2])
    with open('key.pub', 'w') as f:
        f.write(str(keys[0]) + " " +str(keys[1]))
    with open('key.prv', 'w') as f:
        f.write(str(keys[2])+ " " +str(keys[3]))
elif sys.argv[1] == '--encrypt':
    try:
        with open('key.pub', 'r') as f:
            keys = f.read()
        keys = keys.split(" ")
        encrypted = encrypt(keys, sys.argv[2])
        print(encrypted)
    except OSError as e:
        print("No public key found")
elif sys.argv[1] == '--decrypt':
    try:
        with open('key.prv', 'r') as f:
            keys = f.read()
        keys = keys.split(" ")
        decrypted = decrypt(keys, sys.argv[2])
        print(decrypted)
    except OSError as e:
        print("No private key found")
else:
    print("Zły argument!")
