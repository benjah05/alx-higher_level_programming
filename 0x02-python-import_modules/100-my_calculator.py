#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = sub(num1, num2)
    elif operator == '*':
        result = mul(num1, num2)
    elif operator == '/':
        if num2 == 0:
            print("Zero Division Error")
            sys.exit(1)
        result = div(num1, num2)
    print("{} {} {} = {}".format(num1, operator, num2, result))
