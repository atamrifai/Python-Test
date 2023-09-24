
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    sum_arr = sum(arr)  #sum all list on arr
    sum_list = []    # define empty array for sum of list
    for i in arr: 
        sum_list.append(sum_arr-i) # this loop every sum with minus i on iterate loop
    print(min(sum_list),max(sum_list)) # search min and max on sum of list

   


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
