"""
In the big cities, the subway systems always look so complex to the visitors. To give you some sense, the following figure shows the map of Beijing subway. Now you are supposed to help people with your computer skills! Given the starting position of your user, your task is to find the quickest way to his/her destination.

subwaymap.jpg
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤ 100), the number of subway lines. Then N lines follow, with the i-th (i=1,⋯,N) line describes the i-th subway line in the format:

M S[1] S[2] ... S[M]

where M (≤ 100) is the number of stops, and S[i]'s (i=1,⋯,M) are the indices of the stations (the indices are 4-digit numbers from 0000 to 9999) along the line. It is guaranteed that the stations are given in the correct order -- that is, the train travels between S[i] and S[i+1] (i=1,⋯,M−1) without any stop.

Note: It is possible to have loops, but not self-loop (no train starts from S and stops at S without passing through another station). Each station interval belongs to a unique subway line. Although the lines may cross each other at some stations (so called "transfer stations"), no station can be the conjunction of more than 5 lines.

After the description of the subway, another positive integer K (≤ 10) is given. Then K lines follow, each gives a query from your user: the two indices as the starting station and the destination, respectively.

The following figure shows the sample map.

samplemap.jpg

Note: It is guaranteed that all the stations are reachable, and all the queries consist of legal station numbers.
Output Specification:

For each query, first print in a line the minimum number of stops. Then you are supposed to show the optimal path in a friendly format as the following:

Take Line#X1 from S1 to S2.
Take Line#X2 from S2 to S3.
......

where Xi's are the line numbers and Si's are the station indices. Note: Besides the starting and ending stations, only the transfer stations shall be printed.

If the quickest path is not unique, output the one with the minimum number of transfers, which is guaranteed to be unique.
Sample Input:

4
7 1001 3212 1003 1204 1005 1306 7797
9 9988 2333 1204 2006 2005 2004 2003 2302 2001
13 3011 3812 3013 3001 1306 3003 2333 3066 3212 3008 2302 3010 3011
4 6666 8432 4011 1306
3
3011 3013
6666 2001
2004 3001

Sample Output:

2
Take Line#3 from 3011 to 3013.
10
Take Line#4 from 6666 to 1306.
Take Line#3 from 1306 to 2302.
Take Line#2 from 2302 to 2001.
6
Take Line#2 from 2004 to 1204.
Take Line#1 from 1204 to 1306.
Take Line#3 from 1306 to 3001.
"""

#######################################################
"""
这题有点难度，主要是借鉴了思路。
一开始觉得要使用dijkstra算法，但是发现邻接矩阵会非常大，对于路线转换不知道怎么设置
后来借鉴了网上的算法，只需要DFS深度遍历，不需要dijkstra，这样DFS不需要邻接矩阵，只需要邻接表就可以，即使用字典；而对于路线转换的问题，C++
    采用2个int作为一个键值表明2个站点之间的线路，python中也可以这样设置，但是这里使用的是pre*10000+post作为单键，而非双键表示。
递归时注意原始值的改写，尽量在函数括号中改写值，而不要在函数外改值再调用，这有可能会造成回溯时，本应该是原值的地方变成了改值
与网上思路不同的是，不在最后判断中转站，而在递归过程中就进行判断，并且生成路径列表
注意在结束递归的条件语句中，只需要写stop_num > max_stop不需要再添加transfer_num > max_transfer，因为后者不是关键要求，可以总站点少，
    但换乘站点多的情况

最后1个测试点超时，无法改进，不过奇怪的是，调用C++的代码时，最后1个测试点与之前的1个测试点的时间都是14ms，而python中前1个测试点可以通过
"""
#######################################################


def dfs(begin, stop_num, transfer_num, line_, route):
    global unvisited, max_stop, max_transfer, end, routine, map_roads, line
    if stop_num > max_stop:
        return
    elif begin == end:
        if (stop_num < max_stop) or (stop_num == max_stop and transfer_num < max_transfer):
            routine = route.copy() + [end, line_]
            max_stop = stop_num
            max_transfer = transfer_num
        else:
            return
    else:
        for next_station in map_roads[begin]:
            if next_station in unvisited:
                if line_ == -1:
                    unvisited.remove(next_station)
                    dfs(next_station, stop_num + 1, transfer_num, line[begin * 10000 + next_station],
                        [begin, line[begin * 10000 + next_station]])
                    unvisited.append(next_station)
                elif line_ != line[begin * 10000 + next_station]:
                    unvisited.remove(next_station)
                    dfs(next_station, stop_num + 1, transfer_num + 1, line[begin * 10000 + next_station],
                        route + [begin, line[begin * 10000 + next_station]])
                    unvisited.append(next_station)
                else:
                    unvisited.remove(next_station)
                    dfs(next_station, stop_num + 1, transfer_num, line_, route)
                    unvisited.append(next_station)


map_roads = {}
line = {}
for _ in range(int(input())):
    stations = list(map(int, input().split()))
    pre_station = stations[1]
    for i in range(2, stations[0] + 1):
        temp_station = stations[i]
        if pre_station in map_roads:
            map_roads[pre_station].append(temp_station)
        else:
            map_roads[pre_station] = [temp_station]
        if temp_station in map_roads:
            map_roads[temp_station].append(pre_station)
        else:
            map_roads[temp_station] = [pre_station]
        line[pre_station * 10000 + temp_station] = line[temp_station * 10000 + pre_station] = _ + 1
        pre_station = temp_station

stations = list(map_roads.keys())
for _ in range(int(input())):
    start, end = map(int, input().split())
    max_stop = max_transfer = len(stations)
    unvisited = stations.copy()
    unvisited.remove(start)
    routine = []
    dfs(start, 0, 0, -1, [])
    print(max_stop)
    for i in range(0, len(routine) - 2, 2):
        print("Take Line#%d from %04d to %04d." % (routine[i + 1], routine[i], routine[i + 2]))
