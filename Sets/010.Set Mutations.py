# Problem : https://www.hackerrank.com/challenges/py-set-mutations/problem

num_elements_A = int(input())
set_A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == "intersection_update":
        set_A.intersection_update(other_set)
    elif operation == "update":
        set_A.update(other_set)
    elif operation == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        set_A.difference_update(other_set)

print(sum(set_A))