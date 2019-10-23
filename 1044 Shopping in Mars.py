"""
Shopping in Mars is quite a different experience. The Mars people pay by chained diamonds. Each diamond has a value (in Mars dollars M$). When making the payment, the chain can be cut at any position for only once and some of the diamonds are taken off the chain one by one. Once a diamond is off the chain, it cannot be taken back. For example, if we have a chain of 8 diamonds with values M$3, 2, 1, 5, 4, 6, 8, 7, and we must pay M$15. We may have 3 options:

Cut the chain between 4 and 6, and take off the diamonds from the position 1 to 5 (with values 3+2+1+5+4=15).
Cut before 5 or after 6, and take off the diamonds from the position 4 to 6 (with values 5+4+6=15).
Cut before 8, and take off the diamonds from the position 7 to 8 (with values 8+7=15).
Now given the chain of diamond values and the amount that a customer has to pay, you are supposed to list all the paying options for the customer.

If it is impossible to pay the exact amount, you must suggest solutions with minimum lost.

Input Specification:

Each input file contains one test case. For each case, the first line contains 2 numbers: N (≤10
​5
​​ ), the total number of diamonds on the chain, and M (≤10
​8
​​ ), the amount that the customer has to pay. Then the next line contains N positive numbers D
​1
​​ ⋯D
​N
​​  (D
​i
​​ ≤10
​3
​​  for all i=1,⋯,N) which are the values of the diamonds. All the numbers in a line are separated by a space.

Output Specification:

For each test case, print i-j in a line for each pair of i ≤ j such that Di + ... + Dj = M. Note that if there are more than one solution, all the solutions must be printed in increasing order of i.

If there is no solution, output i-j for pairs of i ≤ j such that Di + ... + Dj >M with (Di + ... + Dj −M) minimized. Again all the solutions must be printed in increasing order of i.

It is guaranteed that the total value of diamonds is sufficient to pay the given amount.

Sample Input 1:

16 15
3 2 1 5 4 6 8 7 16 10 15 11 9 12 14 13
Sample Output 1:

1-5
4-6
7-8
11-11
Sample Input 2:

5 13
2 4 5 7 9
Sample Output 2:

2-4
4-5
"""

##########################################
"""
这题是让人崩溃的一题，又是因为python运行超时问题
一开始算法是通过移动游标，计算即时和，但是有超时
    然后在该算法上稍微优化，仍有超时
查阅网上通过的python方法，用的是先对数列求和，用和的差来表征区间数列的和，看起来代码更简洁，于是采用，但仍是超时
    非常不了解为什么几乎一样的代码，它的没有超时，而我的超时
    是因为输入的问题？但是他把输入放在外面，而不是放在for循环的抬头（之前已经证明放在for循坏抬头，比另外建立list快）
    经过长时间思考，发现是输出问题：
        不用格式化输出比格式化输出慢很多！
        print(i,'-',j,sep='')
        print("%d-%d" % (i,j))
        上一句比下一句慢很多！
        下一句 总时间250ms，但上一句就超过300ms
    靠，因为这个浪费时间，太无语了吧！！！
"""
##########################################

N, M = [int(_) for _ in input().split()]
s = [0]
total = 0
for _ in input().split():
    total += int(_)
    s.append(total)
j = 1
minimum = 10e9
combo = []
for i in range(N+1):
    while j < N and s[j] - s[i] < M:
        j += 1
    if j == N:
        if s[j] - s[i] < M:
            break
    if s[j] - s[i] < minimum:
        combo.clear()
        combo.append([i+1, j])
        minimum = s[j] - s[i]
    elif s[j] - s[i] == minimum:
        combo.append([i+1, j])
for i, j in combo:
    print("%d-%d" % (i, j))

##############################################
"""
N, M = (int(_) for _ in input().split())
s = [0]
total = 0
for _ in input().split():
    total += int(_)
    s.append(total)
i = 0
minimum = 10e9
combo = []
for j in range(1, len(s)):
    if s[j] - s[i] == M:
        minimum = 0
        combo.append([0, i + 1, j])
        i += 1
    elif s[j] - s[i] > M:
        while s[j] - s[i] >= M:
            i += 1
        if s[j] - s[i - 1] == M:
            minimum = 0
            combo.append([0, i, j])
        else:
            if minimum >= s[j] - s[i - 1]:
                minimum = s[j] - s[i - 1]
                combo.append([minimum, i, j])
for term in combo:
    if term[0] == minimum:
        print(term[1], '-', term[2], sep='')
"""
##############################################

##############################################
"""
N, M = (int(_) for _ in input().split())
chain = [int(_) for _ in input().split()]
i = 0
j = 0
amount = 0
combo = []
minimum = 10e9
for j in range(len(chain)):
    amount += chain[j]
    if amount == M:
        minimum = 0
        combo.append([0, i, j])
        amount -= chain[i]
        i += 1
    elif amount > M:
        first = chain[i]
        while amount - first >= M:
            amount -= first
            i += 1
            first = chain[i]
        if amount == M:
            minimum = 0
            combo.append([0, i, j])
            amount -= chain[i]
            i += 1
        else:
            if minimum >= amount - M:
                minimum = amount - M
                combo.append([minimum, i, j])
            amount -= chain[i]
            i += 1
for term in combo:
    if term[0] == minimum:
        print(term[1]+1, '-', term[2]+1, sep='')
"""
##############################################

##############################################
"""
N, M = (int(_) for _ in input().split())
i = 1
j = 0
chain = []
amount = 0
combo = []
minimum = 10e9
for d in input().split():
    temp = int(d)
    j += 1
    amount += temp
    chain.append(temp)
    if amount == M:
        minimum = 0
        combo.append([0, i, j])
        amount -= chain.pop(0)
        i += 1
    elif amount > M:
        first = chain[0]
        while amount - first >= M:
            amount -= chain.pop(0)
            i += 1
            first = chain[0]
        if amount == M:
            minimum = 0
            combo.append([0, i, j])
            amount -= chain.pop(0)
            i += 1
        else:
            if minimum >= amount - M:
                minimum = amount - M
                combo.append([minimum, i, j])
            amount -= chain.pop(0)
            i += 1
for term in combo:
    if term[0] == minimum:
        print(term[1], '-', term[2], sep='')
"""
##############################################
