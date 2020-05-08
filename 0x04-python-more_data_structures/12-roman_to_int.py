#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    converted = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string) #save line space
    for i in range(0, length):
        if i + 1 < length and roman[roman_string[i + 1]] > roman[roman_string[i]]:
            converted -= roman[roman_string[i]]
        else:
           converted += roman[roman_string[i]]
    return (converted)
