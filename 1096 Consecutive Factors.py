"""
Among all the factors of a positive integer N, there may exist several consecutive numbers. For example, 630 can be factored as 3×5×6×7, where 5, 6, and 7 are the three consecutive numbers. Now given any positive N, you are supposed to find the maximum number of consecutive factors, and list the smallest sequence of the consecutive factors.
Input Specification:

Each input file contains one test case, which gives the integer N (1<N<2​31​​).
Output Specification:

For each test case, print in the first line the maximum number of consecutive factors. Then in the second line, print the smallest sequence of the consecutive factors in the format factor[1]*factor[2]*...*factor[k], where the factors are listed in increasing order, and 1 is NOT included.
Sample Input:

630

Sample Output:

3
5*6*7
"""

#########################################
"""
求连续因数，则应按照要求，从2到sqrt(n)依次尝试，并更新序列，如果得到一定长度的序列，可以判断是否需要继续尝试序列，以减少比较时间
"""
#########################################

n = int(input())
sec_temp = 0
sec_long = 0
temp = n
start = 0
for i in range(2, int(n**0.5)+1):
    if i ** sec_long > n:
        break
    j = i
    while temp % j == 0:
        temp = temp // j
        j += 1
        sec_temp += 1
    if sec_temp > sec_long:
        sec_long = sec_temp
        start = i
    temp = n
    sec_temp = 0
if start == 0:
    print(1)
    print(n)
else:
    print(sec_long)
    print('*'.join(map(str, range(start, start+sec_long))))
