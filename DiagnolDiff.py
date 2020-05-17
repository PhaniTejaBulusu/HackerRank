#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    aResult=0
    bResult=0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if (i==j):
                aResult+=arr[i][j]
            if (i==n-j-1):
                print(arr[i][j])
                bResult+=arr[i][j]
    return (abs(aResult-bResult))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
