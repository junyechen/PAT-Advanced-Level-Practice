"""
The task is really simple: given N exits on a highway which forms a simple cycle, you are supposed to tell the shortest distance between any pair of exits.

Input Specification:

Each input file contains one test case. For each case, the first line contains an integer N (in [3,10
​5
​​ ]), followed by N integer distances D
​1
​​  D
​2
​​  ⋯ D
​N
​​ , where D
​i
​​  is the distance between the i-th and the (i+1)-st exits, and D
​N
​​  is between the N-th and the 1st exits. All the numbers in a line are separated by a space. The second line gives a positive integer M (≤10
​4
​​ ), with M lines follow, each contains a pair of exit numbers, provided that the exits are numbered from 1 to N. It is guaranteed that the total round trip distance is no more than 10
​7
​​ .

Output Specification:

For each test case, print your results in M lines, each contains the shortest distance between the corresponding given pair of exits.

Sample Input:

5 1 2 4 14 9
3
1 3
2 5
4 1
Sample Output:

3
10
7
"""

##############################################################
"""
这题第一反应是python要超时，果然超时
查看网上是否有优化
第一遍的做法是对每两个需要计算的站点，沿途每个距离加一次，另一段距离则用总距离去减上一段；
第二遍的做法是遍历沿途，将每个站点离第一个站点的总距离作为该站点的距离值，然后两个需要计算的站点通过距离值相减得到，另一段距离用总距离减去，但仍超时；
第三遍回顾网上python通过代码，发觉使用map(int, input().split())的方法，而不是[int(i) for i in input().split()]，将其应用于代码中，发现没有超时！130ms，进入200ms，至少比之前的代码快70ms！amazing！
"""
##############################################################

dis = list(map(int, input().split()))
tot = 0
dis[0] = 0
for i in range(1, len(dis)):
    tot += dis[i]
    dis[i] += dis[i - 1]
for _ in range(int(input())):
    start, end = map(int, input().split())
    if start > end:
        temp = start
        start = end
        end = temp
    dis1 = dis[end - 1] - dis[start - 1]
    dis2 = tot - dis1
    if dis1 > dis2:
        print(dis2)
    else:
        print(dis1)

##############################################################
"""
input_ = input().split()
dis_sum = [0] * (int(input_[0]) + 1)
dis_tot = 0
for i in range(1, len(input_)):
    dis_sum[i] = dis_sum[i - 1] + int(input_[i])
    dis_tot += int(input_[i])
for _ in range(int(input())):
    start, end = [int(_) for _ in input().split()]
    if start > end:
        temp = start
        start = end
        end = temp
    dis1 = dis_sum[end-1] - dis_sum[start-1]
    dis2 = dis_tot - dis1
    if dis1 > dis2:
        print(dis2)
    else:
        print(dis1)
"""
##############################################################

##############################################################
"""
def sum_(a, b):
    return sum(distance[a:b])


distance = [int(_) for _ in input().split()]
dis_total = sum(distance[1:])
for _ in range(int(input())):
    start, end = [int(_) for _ in input().split()]
    if start < end:
        if end - start < len(distance) / 2:
            dis1 = sum_(start, end)
        else:
            dis1 = sum_(1, start) + sum_(end, len(distance))
    else:
        if start - end < len(distance) / 2:
            dis1 = sum_(end, start)
        else:
            dis1 = sum_(1, end) + sum_(start, len(distance))
    dis2 = dis_total - dis1
    if dis1 > dis2:
        print(dis2)
    else:
        print(dis1)
"""
##############################################################
