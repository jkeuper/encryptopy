#!/usr/bin/env python3

import zlib
import hashlib

def encrypt(data, key) -> bytes:
    data = zlib.compress(data)
    return data[0:8] + xor_strings(data[8:], key)

def decrypt(data, key) -> bytes:
    res = xor_strings(data[8:], key)
    return zlib.decompress(data[0:8] + res)

def xor_strings(data, key) -> bytes:
    return bytes([a ^ b for a, b in zip(data, cycle(key))])

def cycle(iterable):
    m = hashlib.sha256()
    m.update(iterable)
    saved = m.digest()

    while saved:
        for element in saved:
            yield element

        m.update(saved)
        saved = m.digest()

##------------##
headerlength = 27
##------------##

import sys

if len(sys.argv) < 2:
    print('cat script.py | ' + sys.argv[0] + ' <key> >script.enc.py ')
    print('Missing key!')
else:
    message = ""
    for line in sys.stdin:
        message += line

    key = sys.argv[1].encode('ascii')
    cipherText = encrypt(message.encode('utf8'), key)
    
    fo = open(sys.argv[0], "r")
    lines = fo.readlines()
    print(*lines[0:headerlength], sep = '')
    print('cipherText = ', end ='')
    print(cipherText)
    print()
    print('key = input("Enter passphrase: ").encode("ascii")')
    print()
    print('script = decrypt(cipherText, key).decode("utf-8")')
    print("exec(script)")

