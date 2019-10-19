"""
Given an increasing sequence S of N integers, the median is the number at the middle position. For example, the median of S1 = { 11, 12, 13, 14 } is 12, and the median of S2 = { 9, 10, 15, 16, 17 } is 15. The median of two sequences is defined to be the median of the nondecreasing sequence which contains all the elements of both sequences. For example, the median of S1 and S2 is 13.

Given two increasing sequences of integers, you are asked to find their median.

Input Specification:

Each input file contains one test case. Each case occupies 2 lines, each gives the information of a sequence. For each sequence, the first positive integer N (≤2×10
​5
​​ ) is the size of that sequence. Then N integers follow, separated by a space. It is guaranteed that all the integers are in the range of long int.

Output Specification:

For each test case you should output the median of the two given sequences in a line.

Sample Input:

4 11 12 13 14
5 9 10 15 16 17
Sample Output:

13
"""


#########################################
"""
本题非常简单，一次通过。
取了个巧，两个数列合并后排序取中间值，python没有超时，该方法就可行
翻阅网上评论，原本该题目有内存限制，为1.5MB，那这种方法肯定不行，必定超限= =
"""
#########################################


t1 = [int(_) for _ in input().split()]
t1.pop(0)
t2 = [int(_) for _ in input().split()]
t2.pop(0)
t = t1 + t2
t.sort()
print(t[int((len(t1)+len(t2))/2-0.5)])
