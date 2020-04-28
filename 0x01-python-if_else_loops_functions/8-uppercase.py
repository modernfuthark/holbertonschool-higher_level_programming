#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        mod = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            mod -= 32
        print("{:s}".format(chr(mod)), end="")
    print("")
