#!/bin/python3

# You are given a spreadsheet that contains a list of  athletes and their details 
# (such as age, height, weight and so on). You are required to sort the data based on the th 
# attribute and print the final resulting table. Follow the example given below for better understanding.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    result = sorted(arr, key=lambda r: r[k])
    
    for r in result:
        print(' '.join(str(e) for e in r))
