"""

Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem

"""

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1, n + 1):
        # {0:{width}d} - Decimal
        # {0:{width}o} - Octa
        # {0:{width}X} - Hexa
        # {0:{width}b} - Binary
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,  width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)