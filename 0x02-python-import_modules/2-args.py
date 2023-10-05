#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n_arg = len(sys.argv)
    if n_arg == 1:
        print("0 arguments.")
    elif n_arg == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(n_arg - 1))
        for i in range(1, n_arg):
            print("{}: {}".format(i, sys.argv[i]))
