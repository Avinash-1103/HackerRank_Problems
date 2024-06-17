#Problem : https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

for i in array:
    for j in set_a:
        if i == j:
            happiness += 1
    for k in set_b:
        if i == k:
            happiness -= 1
    
print(happiness)