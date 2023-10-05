#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n_arg = len(sys.argv)
    s = 0
    if n_arg == 1:
        print("{}".format(s))
    else:
        for i in range(1, n_arg):
            s += int(sys.argv[i])
        print("{}".format(s))
