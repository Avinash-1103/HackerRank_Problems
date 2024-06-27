# Problem : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?

# Reading input
n = int(input())
s = set(map(int, input().split()))
N = int(input())

# Executing commands
for _ in range(N):
    command = input().split()
    if command[0] == "pop":
        if len(s) > 0:
            s.pop()
    elif command[0] == "remove":
        if int(command[1]) in s:
            s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

# Printing the sum of elements in the set
print(sum(s))
