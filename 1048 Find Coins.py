"""
Eva loves to collect coins from all over the universe, including some other planets like Mars. One day she visited a universal shopping mall which could accept all kinds of coins as payments. However, there was a special requirement of the payment: for each bill, she could only use exactly two coins to pay the exact amount. Since she has as many as 10​5​​ coins with her, she definitely needs your help. You are supposed to tell her, for any given amount of money, whether or not she can find two coins to pay for it.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive numbers: N (≤10​5​​, the total number of coins) and M (≤10​3​​, the amount of money Eva has to pay). The second line contains N face values of the coins, which are all positive numbers no more than 500. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in one line the two face values V​1​​ and V​2​​ (separated by a space) such that V​1​​+V​2​​=M and V​1​​≤V​2​​. If such a solution is not unique, output the one with the smallest V​1​​. If there is no solution, output No Solution instead.
Sample Input 1:

8 15
1 2 8 7 2 4 11 15

Sample Output 1:

4 11

Sample Input 2:

7 14
1 8 7 2 4 11 15

Sample Output 2:

No Solution
"""

#############################################
"""
非常简单，一次通过
有两种方法，一种就是从小到大依次遍历，另一种是用桶排序的方法
    但需注意测试点3的钱币数值是大于500的！不符合题意！
本题其实考察的也是排序，桶排的速度比前一快多了
"""
#############################################

n, m = map(int, input().split())
coin = [0] * m
for i in map(int, input().split()):
    if i < m:
        coin[i] += 1
for i in range(1, m // 2):
    if coin[i] != 0 and coin[m - i] != 0:
        print(i, m - i)
        exit(0)
if m % 2 == 0:
    if coin[m // 2] >= 2:
        print(m // 2, m // 2)
        exit(0)
else:
    if coin[m//2] != 0 and coin[m//2+1] != 0:
        print(m//2, m//2 + 1)
        exit(0)
print("No Solution")

"""
n, m = map(int, input().split())
coin = sorted(map(int, input().split()))
i, j = 0, len(coin)-1
while i < j:
    if coin[i] + coin[j] == m:
        print(coin[i], coin[j])
        exit(0)
    else:
        while coin[i] + coin[j] > m:
            j -= 1
        if i == j:
            print("No Solution")
            exit(0)
        if coin[i] + coin[j] == m:
            print(coin[i], coin[j])
            exit(0)
    i += 1
print("No Solution")
"""
