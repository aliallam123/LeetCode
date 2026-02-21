#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    x = s.split(' ')
    caps = []
    for i in x:
        if i == "":
            caps.append("")
        else:
            caps.append((i[0].upper() + i[1:]))
        
    final = " ".join(caps)
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
