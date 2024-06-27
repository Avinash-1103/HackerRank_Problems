# Problem : https://www.hackerrank.com/challenges/designer-door-mat/problem

def door_mat(n,m):
    for i in range(1,n,2):
        print((".|."*i).center(m,'-'))

    print("WELCOME".center(m,'-'))

    for j in range(n-2,-1,-2):
        print(('.|.'*j).center(m,'-'))

n, m = map(int,input().split())
door_mat(n,m)