#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    s = dir(hidden_4)
    for i in range(0, len(s)):
        if s[i][0] != '_' and s[i][1] != '_':
            print("{}".format(s[i]))
