#Problem : https://www.hackerrank.com/challenges/text-alignment/problem

length = int(input())
cha = "H"

for i in range(length):
    print((cha * i).rjust(length - 1) + cha + (cha * i).ljust(length - 1))

for j in range(length + 1):
    print(((cha * length).center(length * 2)) + ((cha * length).center(length * 6)))

for k in range((length + 1) // 2):
    print((cha * (length * 5)).center(length * 6))    

for n in range(length + 1):
    print(((cha * length).center(length * 2)) + ((cha * length).center(length * 6)))

for i in range(length):
    print(((cha *(length - i - 1)).rjust(length) + cha + ( cha * (length - i - 1 )).ljust(length)).rjust(length * 6))
