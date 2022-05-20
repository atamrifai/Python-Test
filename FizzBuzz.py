#!/bin/python3

import math

def fizzBuzz(n):
    for num in range (1,n+1): #+1 because to include 15
        fizz = 'Fizz' if num%3==0 else '' #save at object fizz if multiple 3 (output fizz if true)
        buzz = 'Buzz' if num%5==0 else '' #save at object buzz if multiple 5 (output buzz if true)
        print(f'{fizz}{buzz}' or num) #print as formatted laterals if all true. else print num

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
    
    
 
