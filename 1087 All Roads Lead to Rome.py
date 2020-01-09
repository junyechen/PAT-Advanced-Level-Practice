"""
Indeed there are many different tourist routes from our city to Rome. You are supposed to find your clients the route with the least cost while gaining the most happiness.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers N (2≤N≤200), the number of cities, and K, the total number of routes between pairs of cities; followed by the name of the starting city. The next N−1 lines each gives the name of a city and an integer that represents the happiness one can gain from that city, except the starting city. Then K lines follow, each describes a route between two cities in the format City1 City2 Cost. Here the name of a city is a string of 3 capital English letters, and the destination is always ROM which represents Rome.
Output Specification:

For each test case, we are supposed to find the route with the least cost. If such a route is not unique, the one with the maximum happiness will be recommanded. If such a route is still not unique, then we output the one with the maximum average happiness -- it is guaranteed by the judge that such a solution exists and is unique.

Hence in the first line of output, you must print 4 numbers: the number of different routes with the least cost, the cost, the happiness, and the average happiness (take the integer part only) of the recommanded route. Then in the next line, you are supposed to print the route in the format City1->City2->...->ROM.
Sample Input:
6 7 HZH
ROM 100
PKN 40
GDN 55
PRS 95
BLN 80
ROM GDN 1
BLN ROM 1
HZH PKN 1
PRS ROM 2
BLN HZH 2
PKN GDN 1
HZH PRS 1

Sample Output:
3 3 195 97
HZH->PRS->ROM
"""

#############################################################
"""
非常不熟练，花了很久的时间。
dijkstra算法，加了一些控制条件。

最后测试点1没有过，但是不知道哪里出错。
"""
#############################################################


def dijkstra():
    global des_city, road, cities, happiness
    unvisited = list(range(1, cities))
    pre_route = [-1] * cities
    start = 0
    cost = [99999 for _ in range(cities)]
    cost[0] = 0
    routine = [1] * cities
    happy = [0] * cities
    by_pass = [0] * cities
    while unvisited:
        for des in unvisited:
            if road[start][des] != -1:
                temp_cost = cost[start]+road[start][des]
                if cost[des] > temp_cost:
                    cost[des] = temp_cost
                    routine[des] = routine[start]
                    pre_route[des] = start
                    happy[des] = happy[start]+happiness[des]
                    by_pass[des] = by_pass[start] + 1
                elif cost[des] == temp_cost:
                    routine[des] += routine[start]
                    if (happy[start]+happiness[des] >= happy[des]) and (by_pass[start]+1 < by_pass[des]):
                        pre_route[des] = start
                        happy[des] = happy[start]+happiness[des]
                        by_pass[des] = by_pass[start]+1
        min_index = unvisited[0]
        for i in unvisited:
            if cost[i] < cost[min_index]:
                min_index = i
        start = min_index
        unvisited.remove(start)
    return pre_route, cost, routine, happy, by_pass


cities, routes, start_city = input().split()
cities, routes = int(cities), int(routes)
happiness, city_name, city_no = {}, {}, [0]*cities
for _ in range(cities-1):
    info = input().split()
    happiness[_+1] = int(info[1])
    city_name[info[0]] = _ + 1
    city_no[_+1] = info[0]
city_name[start_city] = 0
city_no[0] = start_city
des_city = city_name['ROM']
road = [[-1 for _ in range(cities)] for _ in range(cities)]
for _ in range(routes):
    info = input().split()
    road[city_name[info[0]]][city_name[info[1]]] = int(info[2])
    road[city_name[info[1]]][city_name[info[0]]] = int(info[2])
[pre_route, cost, routine, happy, by_pass] = dijkstra()
print(routine[des_city], cost[des_city], happy[des_city], int(happy[des_city]/by_pass[des_city]))
r = [des_city]
while pre_route[r[0]] != -1:
    r.insert(0, pre_route[r[0]])
r = [city_no[i] for i in r]
print('->'.join(r))
