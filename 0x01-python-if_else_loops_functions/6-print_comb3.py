#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print("0", end="")
    else:
        if i // 10 >= i % 10:
            continue
    print("{}".format(i), end=", " if i < 89 else "\n")
