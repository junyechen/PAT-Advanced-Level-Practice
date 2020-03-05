"""
In graph theory, an Eulerian path is a path in a graph which visits every edge exactly once. Similarly, an Eulerian circuit is an Eulerian path which starts and ends on the same vertex. They were first discussed by Leonhard Euler while solving the famous Seven Bridges of Konigsberg problem in 1736. It has been proven that connected graphs with all vertices of even degree have an Eulerian circuit, and such graphs are called Eulerian. If there are exactly two vertices of odd degree, all Eulerian paths start at one of them and end at the other. A graph that has an Eulerian path but not an Eulerian circuit is called semi-Eulerian. (Cited from https://en.wikipedia.org/wiki/Eulerian_path)

Given an undirected graph, you are supposed to tell if it is Eulerian, semi-Eulerian, or non-Eulerian.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 2 numbers N (≤ 500), and M, which are the total number of vertices, and the number of edges, respectively. Then M lines follow, each describes an edge by giving the two ends of the edge (the vertices are numbered from 1 to N).
Output Specification:

For each test case, first print in a line the degrees of the vertices in ascending order of their indices. Then in the next line print your conclusion about the graph -- either Eulerian, Semi-Eulerian, or Non-Eulerian. Note that all the numbers in the first line must be separated by exactly 1 space, and there must be no extra space at the beginning or the end of the line.
Sample Input 1:

7 12
5 7
1 2
1 3
2 3
2 4
3 4
5 2
7 6
6 3
4 5
6 4
5 6

Sample Output 1:

2 4 4 4 4 4 2
Eulerian

Sample Input 2:

6 10
1 2
1 3
2 3
2 4
3 4
5 2
6 3
4 5
6 4
5 6

Sample Output 2:

2 4 4 4 3 3
Semi-Eulerian

Sample Input 3:

5 8
1 2
2 5
5 4
4 1
1 3
3 2
3 4
5 3

Sample Output 3:

3 3 4 3 3
Non-Eulerian
"""


###################################
"""
本题考查欧拉图性质，所有节点度数为偶数，表明是欧拉图，2个节点为奇数，则为半欧拉图，其他情况则是非欧拉图
特别注意题目案例可能给的图可能连通分量不为1，因此需要额外检测连通分量，若连通分量不为1，则为非欧拉图

数据量问题 python超时无法解决
"""
###################################


def dfs(start):
    global unvisited, maps
    unvisited.remove(start)
    for end in maps[start]:
        if end in unvisited:
            dfs(end)


n, m = map(int, input().split())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
unvisited = list(range(1, n+1))
connected_components = 0
while unvisited:
    dfs(unvisited[0])
    connected_components += 1
odd = 0
for i in range(n):
    maps[i+1] = len(maps[i+1])
    if maps[i+1] % 2 == 1:
        odd += 1
print(' '.join(map(str, maps[1:])))
if connected_components != 1:
    print('Non-Eulerian')
elif odd == 0:
    print('Eulerian')
elif odd == 2:
    print('Semi-Eulerian')
else:
    print('Non-Eulerian')
