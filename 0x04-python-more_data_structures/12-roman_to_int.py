#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == '':
        return 0
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'X\
C': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    if roman_string in romans:
        return romans[roman_string]
    else:
        res = 0
        roman = list(roman_string)
        for i in roman:
            if i in romans.keys():
                res += romans[i]
        return res
