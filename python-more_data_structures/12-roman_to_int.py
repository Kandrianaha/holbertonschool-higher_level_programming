#!/usr/bin/env python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        curr_value = roman_numerals.get(char, 0)
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value

    return total
