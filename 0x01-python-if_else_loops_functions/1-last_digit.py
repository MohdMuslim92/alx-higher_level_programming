#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = -1
else:
    sign = 1
last_digit = abs(number) % 10
last_digit = last_digit * sign
string = "Last digit of"
if last_digit > 5:
    print(f"{string} {number:d} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{string} {number} is {last_digit} and is 0")
else:
    print(f"{string} {number} is {last_digit} and is less than 6")
