# problem : https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    output = textwrap.fill(string, max_width)
    return output