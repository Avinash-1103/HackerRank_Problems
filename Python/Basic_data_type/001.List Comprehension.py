# Poblem - https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
List = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n :
                List.append([i,j,k])
                    
print(List) 