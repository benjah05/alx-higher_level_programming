#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv)
    print("{} ".format(args - 1), end="")
    if args - 1 == 1:
        print("argument", end="")
    else:
        print("arguments", end="")
    if args - 1 == 0:
        print(".")
    else:
        print(":")
    for n in range(1, args):
        print("{}: {}".format(n, sys.argv[n]))
