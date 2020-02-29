"""
Given a set of N (>1) positive integers, you are supposed to partition them into two disjoint sets A​1​​ and A​2​​ of n​1​​ and n​2​​ numbers, respectively. Let S​1​​ and S​2​​ denote the sums of all the numbers in A​1​​ and A​2​​, respectively. You are supposed to make the partition so that ∣n​1​​−n​2​​∣ is minimized first, and then ∣S​1​​−S​2​​∣ is maximized.
Input Specification:

Each input file contains one test case. For each case, the first line gives an integer N (2≤N≤10​5​​), and then N positive integers follow in the next line, separated by spaces. It is guaranteed that all the integers and their sum are less than 2​31​​.
Output Specification:

For each case, print in a line two numbers: ∣n​1​​−n​2​​∣ and ∣S​1​​−S​2​​∣, separated by exactly one space.
Sample Input 1:

10
23 8 10 99 46 2333 46 1 666 555

Sample Output 1:

0 3611


Sample Input 2:

13
110 79 218 69 3721 100 29 135 2 6 13 5188 85

Sample Output 2:

1 9359
"""

#######################################################
"""
送分题
"""
#######################################################

N = int(input())
number = sorted(list(map(int, input().split())))
if N % 2 == 0:
    print(0, sum(number[N//2:]) - sum(number[:N//2]))
else:
    print(1, sum(number[N//2:]) - sum(number[:N//2]))
