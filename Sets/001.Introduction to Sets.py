# problem : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    new_array = set(array)
    length = len(new_array)
    count = 0
    for i in new_array:
        count += i

    average = count/length

    return average 


