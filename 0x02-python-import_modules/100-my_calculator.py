#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
s = sys.argv
if len(s) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
a = int(s[1])
b = int(s[3])
if s[2] == '+':
    result = add(a, b)
    print("{} {} {} = {}".format(s[1], s[2], s[3], result))
elif s[2] == '-':
    result = sub(a, b)
    print("{} {} {} = {}".format(s[1], s[2], s[3], result))
elif s[2] == '*':
    result = mul(a, b)
    print("{} {} {} = {}".format(s[1], s[2], s[3], result))
elif s[2] == '/':
    result = div(a, b)
    print("{} {} {} = {}".format(s[1], s[2], s[3], result))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
