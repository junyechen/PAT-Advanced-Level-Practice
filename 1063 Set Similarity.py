"""
Given two sets of integers, the similarity of the sets is defined to be N​c​​/N​t​​×100%, where N​c​​ is the number of distinct common numbers shared by the two sets, and N​t​​ is the total number of distinct numbers in the two sets. Your job is to calculate the similarity of any given pair of sets.
Input Specification:

Each input file contains one test case. Each case first gives a positive integer N (≤50) which is the total number of sets. Then N lines follow, each gives a set with a positive M (≤10​4​​) and followed by M integers in the range [0,10​9​​]. After the input of sets, a positive integer K (≤2000) is given, followed by K lines of queries. Each query gives a pair of set numbers (the sets are numbered from 1 to N). All the numbers in a line are separated by a space.
Output Specification:

For each query, print in one line the similarity of the sets, in the percentage form accurate up to 1 decimal place.
Sample Input:

3
3 99 87 101
4 87 101 5 87
7 99 101 18 5 135 18 99
2
1 2
1 3

Sample Output:

50.0%
33.3%
"""

##################################################################
"""
本题善用集合就可以，因为集合能自动过滤重复的数字，所以：
1. 对每一组数据集合化，保证每一组没有重复数字
2. 在比较时，将比较的两组数据放置一起并集合化，减少的数字即为这两组数据重复的数字
"""
##################################################################

case = []
for _ in range(int(input())):
    case.append(list(set(list(map(int, input().split()))[1:])))
for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    nt = len(set(case[a] + case[b]))
    nc = len(case[a]) + len(case[b]) - nt
    print('%.1f%%' % (nc/nt*100))
