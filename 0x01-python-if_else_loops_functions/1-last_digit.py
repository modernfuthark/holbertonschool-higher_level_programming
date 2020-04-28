#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
if number < 0:
    last = ((number * -1) % 10) * -1
    print("{} and is".format(last), end=" ")
else:
    last = number % 10
    print("{} and is".format(last), end=" ")

if last < 6 and last != 0:
    print("less than 6 and not 0")
elif last == 0:
    print("0")
else:
    print("greater than 5")
