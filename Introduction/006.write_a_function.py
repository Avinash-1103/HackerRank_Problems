# Problem : https://www.hackerrank.com/challenges/write-a-function/problem

def leap(year):
    if year % 4 == 0 and ( year % 100 == 0 and year % 400 == 0 ):
        return leap
    else :
        return nonleap
    
leap(int(input()))    