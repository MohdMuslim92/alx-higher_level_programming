#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            'M': 1000, 'MM': 2000, 'MMM': 3000,
            'C': 100, 'CC': 200, 'CCC': 300,
            'CD': 400, 'D': 500, 'DC': 600,
            'DCC': 700, 'DCCC': 800, 'CM': 900,
            'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40,
            'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80,
            'XC': 90, 'IX': 9, 'VIII': 8, 'Vii': 7,
            'VI': 6, 'V': 5, 'IV': 4,
            'III': 3, 'II': 2, 'I': 1
            }
    result = 0
    for number in roman_string:
        for key in roman:
            if number == key:
                result += roman[key]
    return result
