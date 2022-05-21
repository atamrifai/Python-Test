# Case Instruction

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

**Note:** This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

**Example**

![image](https://user-images.githubusercontent.com/58683035/169642181-29306374-155e-4124-8c9d-b3110edec79e.png)

There are n=5 elements, two positive, two negative and one zero. Their ratios are ,  and . 

![image](https://user-images.githubusercontent.com/58683035/169642197-83701892-2e3c-4ef0-9f3c-15034c03196f.png)

Results are printed as:
```
0.400000
0.400000
0.200000
```

**Function Description**

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

+ int arr[n]: an array of integers

**Print**

Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

**Input Format**

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

**Constraints**

![image](https://user-images.githubusercontent.com/58683035/169642224-ab496915-c5d0-4dba-a6ee-88ea38149729.png)


**Output Format**

Print the following 3 lines, each to 6 decimals:

1. proportion of positive values
2. proportion of negative values
3. proportion of zeros

**Sample Input**

```
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
```

**Sample Output**

```
0.500000
0.333333
0.166667
```

**Explanation**

![image](https://user-images.githubusercontent.com/58683035/169642310-73316eb9-6f26-4a87-8596-d2eaa54621e0.png)

