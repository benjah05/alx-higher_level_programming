#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    remainder = number % 10
    print("{}".format(remainder), end="")
    return (remainder)