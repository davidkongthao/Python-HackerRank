"""

Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

"""

def split_and_join(line):
    output = '-'.join(line.split(' '))
    return output
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)