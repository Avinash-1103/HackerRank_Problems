# Problem : https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    float_array = numpy.array(arr[::-1], dtype=float)
    return float_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)