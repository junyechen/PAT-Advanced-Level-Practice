"""
There is a public bike service in Hangzhou City which provides great convenience to the tourists from all over the world. One may rent a bike at any station and return it to any other stations in the city.

The Public Bike Management Center (PBMC) keeps monitoring the real-time capacity of all the stations. A station is said to be in perfect condition if it is exactly half-full. If a station is full or empty, PBMC will collect or send bikes to adjust the condition of that station to perfect. And more, all the stations on the way will be adjusted as well.

When a problem station is reported, PBMC will always choose the shortest path to reach that station. If there are more than one shortest path, the one that requires the least number of bikes sent from PBMC will be chosen.



The above figure illustrates an example. The stations are represented by vertices and the roads correspond to the edges. The number on an edge is the time taken to reach one end station from another. The number written inside a vertex S is the current number of bikes stored at S. Given that the maximum capacity of each station is 10. To solve the problem at S
​3
​​ , we have 2 different shortest paths:

PBMC -> S
​1
​​  -> S
​3
​​ . In this case, 4 bikes must be sent from PBMC, because we can collect 1 bike from S
​1
​​  and then take 5 bikes to S
​3
​​ , so that both stations will be in perfect conditions.

PBMC -> S
​2
​​  -> S
​3
​​ . This path requires the same time as path 1, but only 3 bikes sent from PBMC and hence is the one that will be chosen.

Input Specification:

Each input file contains one test case. For each case, the first line contains 4 numbers: C
​max
​​  (≤100), always an even number, is the maximum capacity of each station; N (≤500), the total number of stations; S
​p
​​ , the index of the problem station (the stations are numbered from 1 to N, and PBMC is represented by the vertex 0); and M, the number of roads. The second line contains N non-negative numbers C
​i
​​  (i=1,⋯,N) where each C
​i
​​  is the current number of bikes at S
​i
​​  respectively. Then M lines follow, each contains 3 numbers: S
​i
​​ , S
​j
​​ , and T
​ij
​​  which describe the time T
​ij
​​  taken to move betwen stations S
​i
​​  and S
​j
​​ . All the numbers in a line are separated by a space.

Output Specification:

For each test case, print your results in one line. First output the number of bikes that PBMC must send. Then after one space, output the path in the format: 0−>S
​1
​​ −>⋯−>S
​p
​​ . Finally after another space, output the number of bikes that we must take back to PBMC after the condition of S
​p
​​  is adjusted to perfect.

Note that if such a path is not unique, output the one that requires minimum number of bikes that we must take back to PBMC. The judge's data guarantee that such a path is unique.

Sample Input:

10 3 3 5
6 7 0
0 1 1
0 2 1
0 3 3
1 3 1
2 3 1
Sample Output:

3 0->2->3 0
"""


#########################################################################################
"""
本题采用dijkstra求最短路径+DFS深度优先遍历，获取所有最短路径，从而计算所需自行车数
不清楚为何有大部分运算错误以及非零返回
在牛客网上提交代码后，提示151行 for node in routine[path[0][0]]: 中routine下标溢出，回头查看path加上routine编号时，用的是变量j而不是i。。。崩溃、、、
"""
#########################################################################################


capacity_max, station_num, station_pro_num, road_num = [int(_) for _ in input().split()]
station_bike = [int(_) for _ in input().split()]
station_bike.insert(0, 0)
road = [[0 for _ in range(station_num + 1)] for _ in range(station_num + 1)]
for _ in range(road_num):
    i, j, t = [int(_) for _ in input().split()]
    road[i][j] = t
    road[j][i] = t
dijkstra = [65536 for _ in range(station_num + 1)]
dijkstra[0] = 0
unvisited = list(range(1, station_num + 1))
last = 0
route_last_node = [-1 for _ in range(station_num + 1)]


while unvisited:
    for now in unvisited:
        if road[last][now] != 0:
            if dijkstra[now] > dijkstra[last] + road[last][now]:
                dijkstra[now] = dijkstra[last] + road[last][now]
                route_last_node[now] = [last]
            elif dijkstra[now] == dijkstra[last] + road[last][now]:
                route_last_node[now].append(last)
    min_pos = unvisited[0]
    for i in unvisited:
        if dijkstra[min_pos] > dijkstra[i]:
            min_pos = i
    last = min_pos
    unvisited.remove(last)
routine = []
stack = []


def dfs(route_last_node, node, routine, stack):
    if node != 0:
        for i in route_last_node[node]:
            stack.insert(0, node)
            dfs(route_last_node, i, routine, stack)
            stack.pop(0)
    else:
        routine.append([_ for _ in stack])


dfs(route_last_node, station_pro_num, routine, stack)
path = []
bike_remain = 0
bike_need = 0
for i in range(len(routine)):
    for j in range(len(routine[i])):
        temp_need = capacity_max // 2 - station_bike[routine[i][j]]
        bike_remain -= temp_need
        if bike_remain <= 0:
            bike_need += -bike_remain
            bike_remain = 0
    path.append([i, bike_need, bike_remain])
    bike_remain, bike_need = 0, 0
path.sort(key=lambda x: (x[1], x[2]))
print(path[0][1], 0, end='')
for node in routine[path[0][0]]:
    print('->%d' % node, end='')
print('', path[0][2])
