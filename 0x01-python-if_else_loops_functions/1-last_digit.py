#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
if number < 0:
    remainder = -(-number % 10)
else:
    remainder = number % 10
print("{}".format(remainder), end=" ")
if remainder > 5:
    print("and is greater than 5")
elif remainder == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
