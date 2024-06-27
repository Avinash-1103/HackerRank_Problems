#Problem : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
set_a = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

s_diff = set_a.symmetric_difference(set_b)
print(len(s_diff))