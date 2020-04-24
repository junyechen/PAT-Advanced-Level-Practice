"""
Given N integers, you are supposed to find the smallest positive integer that is NOT in the given list.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10​5​​). Then N integers are given in the next line, separated by spaces. All the numbers are in the range of int.
Output Specification:

Print in a line the smallest positive integer that is missing from the input list.
Sample Input:

10
5 -25 9 6 1 3 4 2 5 17

Sample Output:

7
"""

##############################################
"""
非常简单，注意输入的数列是从小到大连续排列的情况，则应输出的数为输入数列最大数+1
    或者直接定义数列为0~100000
"""
##############################################

n = int(input())
num = [0] * (n+1)
integer = list(map(int, input().split()))
for i in range(n):
    if 0 < integer[i] <= n:
        num[integer[i]] = 1
for i in range(1, n+1):
    if num[i] == 0:
        print(i)
        break
else:
    print(n+1)
