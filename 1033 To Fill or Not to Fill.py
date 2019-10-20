"""
With highways available, driving a car from Hangzhou to any other city is easy. But since the tank capacity of a car is limited, we have to find gas stations on the way from time to time. Different gas station may give different price. You are asked to carefully design the cheapest route to go.

Input Specification:

Each input file contains one test case. For each case, the first line contains 4 positive numbers: C
​max
​​  (≤ 100), the maximum capacity of the tank; D (≤30000), the distance between Hangzhou and the destination city; D
​avg
​​  (≤20), the average distance per unit gas that the car can run; and N (≤ 500), the total number of gas stations. Then N lines follow, each contains a pair of non-negative numbers: P
​i
​​ , the unit gas price, and D
​i
​​  (≤D), the distance between this station and Hangzhou, for i=1,⋯,N. All the numbers in a line are separated by a space.

Output Specification:

For each test case, print the cheapest price in a line, accurate up to 2 decimal places. It is assumed that the tank is empty at the beginning. If it is impossible to reach the destination, print The maximum travel distance = X where X is the maximum possible distance the car can run, accurate up to 2 decimal places.

Sample Input 1:

50 1300 12 8
6.00 1250
7.00 600
7.00 150
7.10 0
7.20 200
7.50 400
7.30 1000
6.85 300
Sample Output 1:

749.17
Sample Input 2:

50 1300 12 2
7.10 0
7.00 600
Sample Output 2:

The maximum travel distance = 1200.00
"""


#########################################################
"""
本题比较复杂，但是一次通过
贪心算法，即局部优化局部推进进行，因此需要考虑较多问题
算法：
1. 将所有加油站按照距离远近进行排序，并将终点站也设置成加油站，放在列表最后，油费可设置成"无穷大"
2. 判断起点有无加油站，若无加油站，直接输出最远距离0
3. 贪心局部优化：
    1. 当前站点，最远范围内无加油站，则输出最远距离，退出
    2. 当前站点，最远范围内有加油站，则由近到远判断油费
        1. 若范围内有加油站油费比当前站便宜，则该站为下一站目标
        2. 若范围内无加油站油费比当前站便宜，则最远站为下一站目标，设置flag
    3. 根据下一站目标与flag，计算当前站点加油量与费用
        1. 若下一站目标为非便宜站点:
            1. 若下一站为终点站
                1. 若油箱油量够，则扣除油量，本站不加油
                2. 若油箱油量不够，则本站加油至刚好到达下一站
            2. 若下一站为非终点站
                1. 本站将油箱油量加满
        2. 若下一站目标是便宜站点
            1. 若油箱油量够下一站目标，则扣除油量，本站不加油
            2. 若油箱油量不够下一站目标，则本站加油至刚好到达下一站
3.1.1最容易考虑不全，从而造成出错。

牛客网的测试数据则是增加了同一距离多个加油站的情景，个人感觉题目里没有特别提到，此种情景模拟无多大意义
"""
#########################################################


cap, dis, d_avg, num = [int(_) for _ in input().split()]
p_dis = []
for _ in range(num):
    temp = input().split()
    temp[0] = float(temp[0])
    temp[1] = int(temp[1])
    p_dis.append(temp)
p_dis.sort(key=lambda x: x[1])
p_dis.append([65536, dis])
if p_dis[0][1] != 0:
    print("The maximum travel distance = 0.00")
    exit(0)
tank = 0
station = 0
charge = 0
while station < num:
    if p_dis[station][1] + cap * d_avg < p_dis[station+1][1]:
        print("The maximum travel distance = %.02f" % (p_dis[station][1] + cap * d_avg))
        exit(0)
    min_s = station
    for i in range(station+1, num+1):
        if p_dis[station][1] + cap * d_avg >= p_dis[i][1]:
            if p_dis[station][0] > p_dis[i][0]:
                min_s = i
                break
        else:
            break
    if min_s == station:
        if p_dis[station][1] + cap * d_avg >= p_dis[-1][1]:
            if tank >= (p_dis[-1][1] - p_dis[station][1]) / d_avg:
                pass
            else:
                charge += p_dis[station][0] * ((p_dis[-1][1] - p_dis[station][1]) / d_avg - tank)
            station = num
        else:
            charge += p_dis[station][0] * (50 - tank)
            tank = 50 - (p_dis[i-1][1] - p_dis[station][1]) / d_avg
            station = i - 1
    else:
        if (p_dis[min_s][1] - p_dis[station][1]) / d_avg > tank:
            charge += p_dis[station][0] * ((p_dis[min_s][1] - p_dis[station][1]) / d_avg - tank)
            tank = 0
        else:
            tank -= (p_dis[min_s][1] - p_dis[station][1]) / d_avg
        station = min_s
print("%.02f" % charge)


##########################################################
"""
cap, dis, d_avg, num = [int(_) for _ in input().split()]
p_dis = []
for _ in range(num):
    temp = input().split()
    temp[0] = float(temp[0])
    temp[1] = int(temp[1])
    p_dis.append(temp)
p_dis.sort(key=lambda x: (x[1], x[0]))
p_dis.append([65536, dis])
last = 0
i = 1
while i < len(p_dis):
    if p_dis[i][1] == last:
        p_dis.pop(i)
    else:
        last = p_dis[i][1]
        i += 1
num = len(p_dis) - 1
if p_dis[0][1] != 0:
    print("The maximum travel distance = 0.00")
    exit(0)
d = 0
tank = 0
station = 0
charge = 0
while station < num:
    if p_dis[station][1] + cap * d_avg < p_dis[station + 1][1]:
        print("The maximum travel distance = %.02f" % (p_dis[station][1] + cap * d_avg))
        exit(0)
    min_s = station
    for i in range(station + 1, num + 1):
        if p_dis[station][1] + cap * d_avg >= p_dis[i][1]:
            if p_dis[station][0] > p_dis[i][0]:
                min_s = i
                break
        else:
            break
    if min_s == station:
        if p_dis[station][1] + cap * d_avg >= p_dis[-1][1]:
            if tank >= (p_dis[-1][1] - p_dis[station][1]) / d_avg:
                pass
            else:
                charge += p_dis[station][0] * ((p_dis[-1][1] - p_dis[station][1]) / d_avg - tank)
            station = num
        else:
            charge += p_dis[station][0] * (50 - tank)
            tank = 50 - (p_dis[i - 1][1] - p_dis[station][1]) / d_avg
            station = i - 1
    else:
        if (p_dis[min_s][1] - p_dis[station][1]) / d_avg > tank:
            charge += p_dis[station][0] * ((p_dis[min_s][1] - p_dis[station][1]) / d_avg - tank)
            tank = 0
        else:
            tank -= (p_dis[min_s][1] - p_dis[station][1]) / d_avg
        station = min_s
print("%.2f" % charge)
"""
##########################################################