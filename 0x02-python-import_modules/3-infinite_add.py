#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sumNum = 0
    for n in range(1, len(sys.argv)):
        sumNum += int(sys.argv[n])
    print("{}".format(sumNum))
