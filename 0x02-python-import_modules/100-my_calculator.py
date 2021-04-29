#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    s = sys.argv
    if len(s) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(s[1])
        b = int(s[3])
        if s[2] == '+':
            print("{} {} {} = {}".format(s[1], s[2], s[3], add(a, b)))
        elif s[2] == '-':
            print("{} {} {} = {}".format(s[1], s[2], s[3], sub(a, b)))
        elif s[2] == '*':
            print("{} {} {} = {}".format(s[1], s[2], s[3], mul(a, b)))
        elif s[2] == '/':
            print("{} {} {} = {}".format(s[1], s[2], s[3], div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
