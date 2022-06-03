#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    thirdArgv = sys.argv[2]
    result = 0
    operator = ["+", "-", "*", "/"]
    if thirdArgv not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if thirdArgv == "+":
            result = add(a, b)
        elif thirdArgv == "-":
            result = sub(a, b)
        elif thirdArgv == "*":
            result = mul(a, b)
        else:
            result = div(a, b)

        print("{} {} {} = {}".format(a, thirdArgv, b, result))
