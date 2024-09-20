#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    romDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for r in range(len(roman_string)):
        currVal = romDict[roman_string[r]]
        if r < len(roman_string) - 1:
            nextVal = romDict[roman_string[r + 1]]
            if currVal < nextVal:
                integer -= currVal
            else:
                integer += currVal
        else:
            integer += currVal
    return (integer)
