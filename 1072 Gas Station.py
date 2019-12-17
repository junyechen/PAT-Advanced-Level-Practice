"""
A gas station has to be built at such a location that the minimum distance between the station and any of the residential housing is as far away as possible. However it must guarantee that all the houses are in its service range.

Now given the map of the city and several candidate locations for the gas station, you are supposed to give the best recommendation. If there are more than one solution, output the one with the smallest average distance to all the houses. If such a solution is still not unique, output the one with the smallest index number.
Input Specification:

Each input file contains one test case. For each case, the first line contains 4 positive integers: N (≤10​3​​), the total number of houses; M (≤10), the total number of the candidate locations for the gas stations; K (≤10​4​​), the number of roads connecting the houses and the gas stations; and D​S​​, the maximum service range of the gas station. It is hence assumed that all the houses are numbered from 1 to N, and all the candidate locations are numbered from G1 to GM.

Then K lines follow, each describes a road in the format

P1 P2 Dist

where P1 and P2 are the two ends of a road which can be either house numbers or gas station numbers, and Dist is the integer length of the road.
Output Specification:

For each test case, print in the first line the index number of the best location. In the next line, print the minimum and the average distances between the solution and all the houses. The numbers in a line must be separated by a space and be accurate up to 1 decimal place. If the solution does not exist, simply output No Solution.
Sample Input 1:

4 3 11 5
1 2 2
1 4 2
1 G1 4
1 G2 3
2 3 2
2 G2 1
3 4 2
3 G3 2
4 G1 3
G2 G1 1
G3 G2 2

Sample Output 1:

G1
2.0 3.3

Sample Input 2:

2 1 2 10
1 G1 9
2 G1 20

Sample Output 2:

No Solution
"""


###################################################################################################
"""
本题为利用dijkstra对每一个加油站作为起点进行遍历，仍是非常地不熟练
此外，注意本题的输出条件：
    1. 满足站点至民居的距离不超过允许范围
    2. 满足1的条件下，取站点至民居的最小距离的最大的站点
    3. 如果满足2的条件，站点不唯一，取站点至民居平均距离最小的站点
    4. 如果满足3的条件，站点不唯一，取站点编号最小的站点

本题利用python最后一个测试点超时，估计是样本量问题，无法使用python解决，只能用C++

本题还需注意保留1位小数的四舍五入，python有0.5的进位问题，可采用int(+0.5)的方式进行四舍五入，规定小数位则相应的先挪动小数位、处理后再挪回小数位
"""
###################################################################################################


def dijkstra(origin):
    global roads, dij, des_set, closed
    start = origin
    des_set.remove(start)
    while des_set:
        for end in des_set:
            if roads[start][end] != closed:
                if start == origin:
                    dij[origin][end] = roads[start][end]
                else:
                    dij[origin][end] = min(dij[origin][end], dij[origin][start]+roads[start][end])
        min_dij = closed
        for i in des_set:
            if dij[origin][i] < min_dij:
                min_dij = dij[origin][i]
                min_dij_index = i
        start = min_dij_index
        des_set.remove(start)


n, m, k, ds = map(int, input().split())
closed = 100000
roads = [[closed for _ in range(n+m+1)] for _ in range(n+m+1)]
for i in range(k):
    p1, p2, dist = input().split()
    if p1[0] == 'G':
        p1 = n + int(p1[1:])
    else:
        p1 = int(p1)
    if p2[0] == 'G':
        p2 = n + int(p2[1:])
    else:
        p2 = int(p2)
    roads[p1][p2] = int(dist)
    roads[p2][p1] = int(dist)
dij = [[closed for _ in range(n+m+1)] for _ in range(n+m+1)]
min_road = [closed for _ in range(m+1)]
ave_road = [closed for _ in range(m+1)]
for i in range(n+1, n+m+1):
    des_set = set(range(1, n+m+1))
    dijkstra(i)
    min_road_ = closed
    ave_road_ = 0
    for j in range(1, n+1):
        if dij[i][j] > ds:
            min_road_ = closed
            break
        else:
            if dij[i][j] < min_road_:
                min_road_ = dij[i][j]
            ave_road_ += dij[i][j]
    if min_road_ == closed:
        min_road[i-n] = -1
        continue
    else:
        min_road[i-n] = min_road_
        ave_road[i-n] = ave_road_/n
res = list(zip(range(1, m+1), min_road[1:], ave_road[1:]))
res.sort(key=lambda x: (-x[1], x[2], x[0]))
if res[0][2] == closed:
    print("No Solution")
else:
    print("G%d" % res[0][0])
    print("%.1f %.1f" % (res[0][1], int(res[0][2]*10+0.5)/10))
# max_ave_index = 1
# for i in range(1, m+1):
#     if ave_road[max_ave_index] < ave_road[i] != closed:
#         max_ave_index = i
# if ave_road[max_ave_index] == closed:
#     print("No Solution")
# else:
#     print('G%d' % max_ave_index)
#     print("%0.1f %0.1f" % (min_road[max_ave_index], ave_road[max_ave_index]))
