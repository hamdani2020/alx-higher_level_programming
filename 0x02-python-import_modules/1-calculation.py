#!/usr/bin/python3

if __name__ == "__main__":
    """ Print the addition, division, multiplication and division of 10 and 15."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
