"""

Problem: https://www.hackerrank.com/challenges/python-tuples/problem


"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # tuple() turns a list into a tuple.
    my_list = tuple(integer_list)
    print(hash(my_list))