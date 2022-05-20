#!/bin/python3

def fizzBuzz(i):
    print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,i+1)),sep='\n')
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
