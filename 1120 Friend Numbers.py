"""
Two integers are called "friend numbers" if they share the same sum of their digits, and the sum is their "friend ID". For example, 123 and 51 are friend numbers since 1+2+3 = 5+1 = 6, and 6 is their friend ID. Given some numbers, you are supposed to count the number of different friend ID's among them.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N. Then N positive integers are given in the next line, separated by spaces. All the numbers are less than 10​4​​.
Output Specification:

For each case, print in the first line the number of different frind ID's among the given integers. Then in the second line, output the friend ID's in increasing order. The numbers must be separated by exactly one space and there must be no extra space at the end of the line.
Sample Input:

8
123 899 51 998 27 33 36 12

Sample Output:

4
3 6 9 26
"""

#############################################
"""
大水题
可以用sorted对set排序得到有序的list
中间可以不用list.append 而是用set.add
"""
#############################################

n = int(input())
numbers = input().split()
friend_num = []
for i in range(n):
    sum_ = 0
    for j in numbers[i]:
        sum_ += int(j)
    friend_num.append(sum_)
friend_num = sorted(set(friend_num))
print(len(friend_num))
print(' '.join(map(str, friend_num)))
