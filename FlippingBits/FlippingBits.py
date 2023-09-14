#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
   return (2**32 - 1) - n
   #explanation:
   #don't flip the integer but minus it by n
   #2**32 = maximum integer on 32 Bit. just min by n. because output on 32 Bit integer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
