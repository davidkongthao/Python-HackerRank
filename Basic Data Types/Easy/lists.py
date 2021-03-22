"""

Problem: https://www.hackerrank.com/challenges/python-lists/problem

"""

if __name__ == '__main__':
    N = int(input())
    x = []
    while N != 0:
        x += [input().split()]
        N -=1
    l = []
    for i in x:
        if i[0] == "print":
            print(l)
        elif len(i) == 3:
            eval("l.{0}({1},{2})".format(i[0],i[1],i[2]))
        elif len(i) == 2:
            eval("l.{0}({1})".format(i[0], i[1]))
        elif len(i) == 1:
            eval("l.{0}()".format(i[0]))