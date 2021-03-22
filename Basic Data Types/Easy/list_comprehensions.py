"""

Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    brr=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                arr=[i,j,k]
                if sum(arr)!=n:
                    brr.append(arr)
    print(brr)
    
