"""
Calculate a+b and output the sum in standard format -- that is, the digits must be separated into groups of three by commas (unless there are less than four digits).
Input Specification:

Each input file contains one test case. Each case contains a pair of integers a and b where −10​6​​≤a,b≤10​6​​. The numbers are separated by a space.
Output Specification:

For each test case, you should output the sum of a and b in one line. The sum must be written in the standard format.
Sample Input:

-1000000 9

Sample Output:

-999,991
"""

##########################################
"""
非常简单，一次通过
!!!
直接使用format内置函数，更加快捷！
"""
##########################################

##########################################
a, b = [int(i) for i in input().split()]
print("{:,}".format(a + b))
##########################################

##########################################
"""
a, b = [int(i) for i in input().split()]
sum = list(str(a + b))
ind = len(sum)
while ind - 3 > 1:
    sum.insert(ind - 3,',')
    ind -= 3
if ind - 3 == 1 and sum[0] != '-':
    sum.insert(1,',')
print(''.join(sum))
"""
##########################################