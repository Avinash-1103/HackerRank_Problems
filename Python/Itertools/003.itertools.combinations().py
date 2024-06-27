from itertools import combinations

# Read the input
input_str = input().strip()
S, b = input_str.split()
b = int(b)

# Sort the string to ensure lexicographical order
S = ''.join(sorted(S))

# Generate and print combinations
for i in range(1, b + 1):
    for combo in combinations(S, i):
        print(''.join(combo))