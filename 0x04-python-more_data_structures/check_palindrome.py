#!/usr/bin/python3
def is_palindrome(p):
    reverse = 0
    temp = p
    while (temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return (reverse == p)
def check_palindrome():
    palindrome_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if (is_palindrome(product)):
                palindrome_list.append(product)
    largest = 1
    for i in range(len(palindrome_list)):
        if palindrome_list[i] > largest:
            largest = palindrome_list[i]
    print("{:d}".format(largest), end="")
check_palindrome()
