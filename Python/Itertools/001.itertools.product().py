from itertools import product

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

output = product(list_a, list_b)

formatted_output = ' '.join(f'({a}, {b})' for a, b in output)

print(formatted_output)