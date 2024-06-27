#Problem : https://www.hackerrank.com/challenges/py-if-else/problem

def oddeven(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")    

oddeven(int(input()))