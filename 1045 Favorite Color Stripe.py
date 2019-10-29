"""
Eva is trying to make her own color stripe out of a given one. She would like to keep only her favorite colors in her favorite order by cutting off those unwanted pieces and sewing the remaining parts together to form her favorite color stripe.

It is said that a normal human eye can distinguish about less than 200 different colors, so Eva's favorite colors are limited. However the original stripe could be very long, and Eva would like to have the remaining favorite stripe with the maximum length. So she needs your help to find her the best result.

Note that the solution might not be unique, but you only have to tell her the maximum length. For example, given a stripe of colors {2 2 4 1 5 5 6 3 1 1 5 6}. If Eva's favorite colors are given in her favorite order as {2 3 1 5 6}, then she has 4 possible best solutions {2 2 1 1 1 5 6}, {2 2 1 5 5 5 6}, {2 2 1 5 5 6 6}, and {2 2 3 1 1 5 6}.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤200) which is the total number of colors involved (and hence the colors are numbered from 1 to N). Then the next line starts with a positive integer M (≤200) followed by M Eva's favorite color numbers given in her favorite order. Finally the third line starts with a positive integer L (≤10
​4
​​ ) which is the length of the given stripe, followed by L colors on the stripe. All the numbers in a line a separated by a space.

Output Specification:

For each test case, simply print in a line the maximum length of Eva's favorite stripe.

Sample Input:

6
5 2 3 1 5 6
12 2 2 4 1 5 5 6 3 1 1 5 6
Sample Output:

7
"""

#############################################################
"""
一次通过
本题主要学习了最长子串LCS的算法。
1. 最原始的动态规划思想：
    设有一串字符串s，假设d[i]为以s[i]为结尾的子串最长子串的长度，则易知，若s[i+1]>s[i]，则d[i+1]=d[i]+1；若s[i+1]<s[i]，则应存在s[j]使得最大j的s[j]<s[i+1]，则d[i+1]=d[j]+1，初始条件为d[0]=1。以该方法最终可以得到所有末尾的最长子串，然后取得最长的子串
2. 更新：
    不用d[i]记录长度，而用temp列表记录从头开始往后遍历过程的子串序列，若s[i+1]>s[i]，则temp.append(s[i+1])；否则应找到下表最大的j，使得temp[j]<s[i+1]，然后将其替换。最后最长子串长度即为temp的长度。
    例：243124
        i   temp
        0   2
        1   2 4
        2   2 3
        3   1 3
        4   1 2
        5   1 2 4
    则该例子的最长子串长度为3，但一定注意最后的temp不一定是最长子串！
"""
#############################################################


def binary_sort_replace(temp, start, end, comp):
    mid = (start + end) // 2
    if comp >= temp[mid]:
        binary_sort_replace(temp, mid + 1, end, comp)
    else:
        if mid == 0:
            temp[mid] = comp
        elif comp >= temp[mid - 1]:
            temp[mid] = comp
        else:
            binary_sort_replace(temp, start, mid - 1, comp)


N = int(input())
M = [int(_) for _ in input().split()]
M.pop(0)
L = [int(_) for _ in input().split()]
L.pop(0)
order = [0] * (N + 1)
for i in range(len(M)):
    order[M[i]] = i + 1
i = 0
while i < len(L):
    if order[L[i]] == 0:
        L.pop(i)
    else:
        L[i] = order[L[i]]
        i += 1
length = 1
temp = [L[0]]
i = 1
while i < len(L):
    if L[i] >= temp[length - 1]:
        temp.append(L[i])
        length += 1
        i += 1
    else:
        binary_sort_replace(temp, 0, length - 1, L[i])
        i += 1
print(length)
