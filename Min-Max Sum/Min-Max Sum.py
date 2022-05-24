#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_arr = sum(arr)
    sum_list = []    
    for i in arr:
        sum_list.append(sum_arr-i)
    print(min(sum_list),max(sum_list))
   

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
