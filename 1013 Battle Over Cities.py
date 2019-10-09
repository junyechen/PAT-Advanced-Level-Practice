"""
It is vitally important to have all the cities connected by highways in a war. If a city is occupied by the enemy, all the highways from/toward that city are closed. We must know immediately if we need to repair any other highways to keep the rest of the cities connected. Given the map of cities which have all the remaining highways marked, you are supposed to tell the number of highways need to be repaired, quickly.

For example, if we have 3 cities and 2 highways connecting city​1​​-city​2​​ and city​1​​-city​3​​. Then if city​1​​ is occupied by the enemy, we must have 1 highway repaired, that is the highway city​2​​-city​3​​.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 3 numbers N (<1000), M and K, which are the total number of cities, the number of remaining highways, and the number of cities to be checked, respectively. Then M lines follow, each describes a highway by 2 integers, which are the numbers of the cities the highway connects. The cities are numbered from 1 to N. Finally there is a line containing K numbers, which represent the cities we concern.
Output Specification:

For each of the K cities, output in a line the number of highways need to be repaired if that city is lost.
Sample Input:

3 2 3
1 2
1 3
1 2 3

Sample Output:

1
0
0
"""

#############################################################
"""
本题为连通图中，去掉一个顶点，剩下的顶点与边需要多少连通量完成这幅图，答案为该连通量-1。
采用深度优先搜寻遍历搜寻DFS
学习网上C++代码，用python几乎一致，但是测试点3始终非零返回，测试点4运行超时。运行超时可以接受，但是非零返回原因不明。
"""
#############################################################

def dfs(city, node, road,N):
    city[node] = 1
    for i in range(1,N + 1):
        if city[i] == 0 and road[node][i] == 1:
            dfs(city,i,road,N)

N, M, K = [int(i) for i in input().split()]
r = [[0 for i in range(N + 1)] for j in range(N + 1)]
for _ in range(M):
    c1, c2 = [int(i) for i in input().split()]
    r[c1][c2] = 1
    r[c2][c1] = 1
k = [int(i) for i in input().split()]
for i in k:
    city = [0] * (N + 1)
    city[i] = 1
    num = 0
    for j in range(1,N + 1):
        if city[j] == 0:
            dfs(city, j,r,N)
            num += 1
    print(num - 1)