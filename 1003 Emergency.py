"""
As an emergency rescue team leader of a city, you are given a special map of your country. The map shows several scattered cities connected by some roads. Amount of rescue teams in each city and the length of each road between any pair of cities are marked on the map. When there is an emergency call to you from some other city, your job is to lead your men to the place as quickly as possible, and at the mean time, call up as many hands on the way as possible.
Input Specification:

Each input file contains one test case. For each test case, the first line contains 4 positive integers: N (≤500) - the number of cities (and the cities are numbered from 0 to N−1), M - the number of roads, C​1​​ and C​2​​ - the cities that you are currently in and that you must save, respectively. The next line contains N integers, where the i-th integer is the number of rescue teams in the i-th city. Then M lines follow, each describes a road with three integers c​1​​, c​2​​ and L, which are the pair of cities connected by a road and the length of that road, respectively. It is guaranteed that there exists at least one path from C​1​​ to C​2​​.
Output Specification:

For each test case, print in one line two numbers: the number of different shortest paths between C​1​​ and C​2​​, and the maximum amount of rescue teams you can possibly gather. All the numbers in a line must be separated by exactly one space, and there is no extra space allowed at the end of a line.
Sample Input:

5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1

Sample Output:

2 4
"""

#################################################################
"""
本题涉及到算法问题，以前都没有接触过，因此做起来十分费力。该算法为Dikjstra求最短路径问题。
先掌握原理，核心为path[des] = min(path[des], path[start] + road[start][des])
个人模板建立为：
start = C1
set_.remove(start)
while set_:
    for des in set_:
        if road[start][des] != -1:
            if path[des] == -1:
                path[des] = path[start] + road[start][des]
            else:
                if path[des] > path[start] + road[start][des]:
                    path[des] = path[start] + road[start][des]
    min_ = None
    for i in set_:
        if path[i] != -1:
            if min_:
                if path[i] < path[min_]:
                    min_ = i
            else:
                min_ = i
    start = min_
    set_.remove(start)

本题在学习算法后，要进一步获得路线数和总人数，这里面出了比较严重的输入错误，而自己想当然的没看出来，导致总是几乎所有答案错误，不严谨
"""
#################################################################

N, M, C1, C2 = [int(i) for i in input().split()]
people = [int(i) for i in input().split()]
path = [-1] * (N)
path[C1] = 0
path_num = [0] * (N)
path_people = [0] * (N)
set_ = set(range(N))
road = [[-1 for i in range(N)] for j in range(N)]
for i in range(M):
    temp = [int(i) for i in input().split()]
    road[temp[0]][temp[1]] = road[temp[1]][temp[0]] = temp[2]
if C1 == C2:
    print(1,people[C1])
else:
    start = C1
    set_.remove(start)
    path_num[start] = 1
    path_people[start] = people[start]
    while set_:
        for des in set_:
            if road[start][des] != -1:
                if path[des] == -1:
                    path[des] = path[start] + road[start][des]
                    path_num[des] = path_num[start]
                    path_people[des] = path_people[start] + people[des]
                else:
                    if path[des] > path[start] + road[start][des]:
                        path[des] = path[start] + road[start][des]
                        path_num[des] = path_num[start]
                        path_people[des] = path_people[start] + people[des]
                    elif path[des] == path[start] + road[start][des]:
                        path_num[des] += path_num[start]
                        path_people[des] = max(path_people[des],path_people[start] + people[des])
        min_ = None
        for i in set_:
            if path[i] != -1:
                if min_:
                    if path[i] < path[min_]:
                        min_ = i
                else:
                    min_ = i
        start = min_
        set_.remove(start)
    print(path_num[C2],path_people[C2])


####################################################
"""
def search(C2,R,temp):
    if temp[0] == C2:
        return temp[1]
    else:
        for i in R[temp[0]]:
            t_ = search(C2,R,i)
            if t_ != 0:
                return t_ + i[1]
            else:
                return 0
        return 0
N, M, C1, C2 = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
R = [[] for i in range(len(C))]
for i in range(M):
    temp = [int(i) for i in input().split()]
    R[temp[0]].append(temp[1:3])
r, t = 0, 0
for i in R[C1]:
    if i[0] == C2:
        r += 1
        t += i[1]
    else:
        t_ = search(C2,R,i)
        if t_ != 0:
            r += 1
            t += t_
print(r,t)
"""
####################################################