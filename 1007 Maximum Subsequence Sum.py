"""
Given a sequence of K integers { N​1​​, N​2​​, ..., N​K​​ }. A continuous subsequence is defined to be { N​i​​, N​i+1​​, ..., N​j​​ } where 1≤i≤j≤K. The Maximum Subsequence is the continuous subsequence which has the largest sum of its elements. For example, given sequence { -2, 11, -4, 13, -5, -2 }, its maximum subsequence is { 11, -4, 13 } with the largest sum being 20.

Now you are supposed to find the largest sum, together with the first and the last numbers of the maximum subsequence.
Input Specification:

Each input file contains one test case. Each case occupies two lines. The first line contains a positive integer K (≤10000). The second line contains K numbers, separated by a space.
Output Specification:

For each test case, output in one line the largest sum, together with the first and the last numbers of the maximum subsequence. The numbers must be separated by one space, but there must be no extra space at the end of a line. In case that the maximum subsequence is not unique, output the one with the smallest indices i and j (as shown by the sample case). If all the K numbers are negative, then its maximum sum is defined to be 0, and you are supposed to output the first and the last numbers of the whole sequence.
Sample Input:

10
-10 1 2 3 4 -5 -23 3 7 -21

Sample Output:

10 1 4
"""

#######################################
"""
本题又是审题不仔细，最后要求输出的是序列两端的数字，而不是序号。本能一次通过。
本题也是一道动态规划问题，和前面1003急救的图论差不太多。
单球连续序列最大值，可以按顺序，求到每一个数为止可以取得的最大值，
    初始状态：s[0]=n[0]
    状态方程：s[i]=max(s[i-1]+n[i],n[i])，遍历该公式即可得到，以任意一个数为终点的任意序列可得到的最大值
    那么求连续序列最大值，只要在执行状态方程过程中判断是否是最大值即可
求序列两端则外加条件：
    当s[i]取n[i]时，意味着需要重新开始取序列
    当s[i]>max时，意味着序列末端更新
"""
#######################################

input()
n = [int(i) for i in input().split()]
sum_ = n[0]
max_ = n[0]
index_temp = 0
index_ = [0,0]
for i in range(1,len(n)):
    if sum_ + n[i] < n[i]:
        index_temp = i
        sum_ = n[i]
    else:
        sum_ += n[i]
    if sum_ > max_:
        max_ = sum_
        index_ = [index_temp, i]
if max_ < 0:
    print(0,n[0],n[len(n) - 1])
else:
    print(max_,n[index_[0]],n[index_[1]])
