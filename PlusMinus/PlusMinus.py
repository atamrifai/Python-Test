#!/bin/python3

import math

def plusMinus(arr):
    positif = []
    negatif = []
    netral = []
    for num in list(arr):
        if (num > 0):
            positif.append(num)
        elif (num < 0):
            negatif.append(num)
        else:
            netral.append(num)
    lenpos = len(positif) / len(arr)
    lentif = len(negatif) / len(arr)
    lentral = len(netral) / len(arr)
    print('{}\n{}\n{}'.format(lenpos, lentif, lentral))
        
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
