# Problem : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
set_a = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

intersection = set_a.intersection(set_b)
print(len(intersection))