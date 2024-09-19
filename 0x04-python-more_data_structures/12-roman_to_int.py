#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    integer = 0
    prev = 0
    for r in roman_string:
        for k, v in roman_numerals.items():
            if r > prev
                integer += r - 2 * prev
            else:
                integer += k
            prev = r
    return (integer)
