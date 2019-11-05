"""
The task is simple: given any positive integer N, you are supposed to count the total number of 1's in the decimal form of the integers from 1 to N. For example, given N being 12, there are five 1's in 1, 10, 11, and 12.
Input Specification:

Each input file contains one test case which gives the positive N (≤2​30​​).
Output Specification:

For each test case, print the number of 1's in one line.
Sample Input:

12

Sample Output:

5
"""

##########################################################
"""
本题考查规律应用，一次通过，但费了点时间
可转变为每个数位上出现'1'的总次数
对于某个数位d，必定有(before)d(after) = n的形式
    若d == 0:
        则d数位出现1的个数为before * 10 ^ after位数
    若d == 1:
        则d数位出现1的个数为before * 10 ^ after位数 + after + 1
    若d > 1:
        则d数位出现1的个数为(before + 1) * 10 ^ after位数
"""
##########################################################

n = input()
tot = 0
if len(n) == 1:
    if n >= '1':
        tot = 1
    else:
        tot = 0
else:
    for i in range(1, len(n)-1):
        if n[i] == '0':
            tot += int(n[:i]) * (10 ** (len(n) - i - 1))
        elif n[i] == '1':
            tot += int(n[:i]) * (10 ** (len(n) - i - 1)) + int(n[i + 1:]) + 1
        else:
            tot += (int(n[:i]) + 1) * (10 ** (len(n) - i - 1))
    if n[0] == '1':
        tot += int(n[1:]) + 1
    else:
        tot += 10 ** (len(n) - 1)
    if n[-1] == '0':
        tot += int(n[:-1])
    else:
        tot += int(n[:-1]) + 1
print(tot)
