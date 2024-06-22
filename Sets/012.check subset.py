# Problem : https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for test in range(t):

    a = int(input())
    set_a = set(map(int, input().split()))
    
    b = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))