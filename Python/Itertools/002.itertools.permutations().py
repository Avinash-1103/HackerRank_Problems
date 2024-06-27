import itertools

# Read input
input_str = input().strip()
s, k = input_str.split()
k = int(k)

# Generate permutations of size k
permutations = itertools.permutations(s, k)

# Convert permutations to sorted list
sorted_permutations = sorted([''.join(p) for p in permutations])

# Print each permutation in sorted order
for perm in sorted_permutations:
    print(perm)