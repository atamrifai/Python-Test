#Import Libary
import math
import os
import random
import re
import sys

#Function

                
#Main Program
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') #to execute output on my machine *just delete if error
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()
