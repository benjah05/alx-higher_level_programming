#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for i in range(len(str)):
        if i == n:
            continue
        string += str[i]
    return (string)
