"""
British astronomer Eddington liked to ride a bike. It is said that in order to show off his skill, he has even defined an "Eddington number", E -- that is, the maximum integer E such that it is for E days that one rides more than E miles. Eddington's own E was 87.

Now given everyday's distances that one rides for N days, you are supposed to find the corresponding E (≤N).
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10​5​​), the days of continuous riding. Then N non-negative integers are given in the next line, being the riding distances of everyday.
Output Specification:

For each case, print in a line the Eddington number for these N days.
Sample Input:

10
6 7 6 9 3 10 8 2 7 8

Sample Output:

6
"""

######################################################################
"""
逻辑分析题
将里程从大到小排列后进行比较，第n天里程大于n就继续向后探索，直到第m天里程小于等于m，则E为m-1
注意边界条件！可能遍历完所有天数！都满足！
    此项条件针对的是循环的写法 如我下面所写的，
    若为 for i in range(1, n+1): 则不需要额外的的else判断语句！！！
"""
######################################################################

n = int(input())
road = sorted(list(map(int, input().split())), reverse=True)
for i in range(n):
    if road[i] <= i+1:
        break
else:
    print(n)
    exit(0)
print(i)


##########################################################################
"""
n = int(input())
eddington_num = [0] * (n+1)
road = list(map(int, input().split()))
for i in range(n):
    eddington_num[:road[i]] = [x + 1 for x in eddington_num[:road[i]]]
for i in range(1, n):
    if eddington_num[i] == i:
        break
    elif eddington_num[i] < i:
        i -= 1
        break
print(i)
"""
##########################################################################
