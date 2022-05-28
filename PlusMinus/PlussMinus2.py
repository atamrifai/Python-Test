import math
def plusMinus(arr):
    positive, negative, zero, ran = [i for i in arr if i > 0], [i for i in arr if i < 0],[i for i in arr if i == 0], len(arr)
    print('{}\n{}\n{}'.format(len(positive)/ran, len(negative)/ran, len(zero)/ran))
 
if __name__ == '__main__':
   n = int(input().strip())
   arr = list(map(int, input().rstrip().split()))
   plusMinus(arr)
