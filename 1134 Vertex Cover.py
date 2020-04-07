"""
A vertex cover of a graph is a set of vertices such that each edge of the graph is incident to at least one vertex of the set. Now given a graph with several vertex sets, you are supposed to tell if each of them is a vertex cover or not.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers N and M (both no more than 10​4​​), being the total numbers of vertices and the edges, respectively. Then M lines follow, each describes an edge by giving the indices (from 0 to N−1) of the two ends of the edge.

After the graph, a positive integer K (≤ 100) is given, which is the number of queries. Then K lines of queries follow, each in the format:

N​v​​ v[1] v[2]⋯v[N​v​​]

where N​v​​ is the number of vertices in the set, and v[i]'s are the indices of the vertices.
Output Specification:

For each query, print in a line Yes if the set is a vertex cover, or No if not.
Sample Input:

10 11
8 7
6 8
4 5
8 4
8 1
1 2
1 4
9 8
9 1
1 0
2 4
5
4 0 3 8 4
6 6 1 7 5 4 9
3 1 8 4
2 2 8
7 9 8 7 6 5 4 2

Sample Output:

No
Yes
Yes
No
No
"""

###################################################
"""
这题竟然花了很久的时间
最终算法：
    以顶点为列表下标，内容为道路编号
    对输入的顶点集合依次搜寻道路，并将得到的道路编号进行标记
    对集合中所有顶点处理后，若存在未标记道路，则表明有道路未覆盖，输出'No'，反之输出'Yes'
"""
###################################################

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(i)
    edges[b].append(i)
for _ in range(int(input())):
    vertices = list(map(int, input().split()))[1:]
    visited_edge = [0] * m
    for vertex in vertices:
        for edge in edges[vertex]:
            visited_edge[edge] = 1
    if 0 in visited_edge:
        print('No')
    else:
        print('Yes')

####################################################
"""
n, m = map(int, input().split())
edge = []
for _ in range(m):
    edge.append(input().split())
for _ in range(int(input())):
    vertices = input().split()[1:]
    for i in range(m):
        if set(edge[i]) & set(vertices):
            pass
        else:
            print('No')
            break
    else:
        print('Yes')
"""
####################################################


####################################################
"""
def main():
    n, m = map(int, input().split())
    edge = [[] for _ in range(m)]
    for i in range(m):
        edge[i] = list(map(int, input().split()))
    for _ in range(int(input())):
        vertices = list(map(int, input().split()))[1:]
        for i in range(m):
            if len(set(edge[i] + vertices)) == len(edge[i]) + len(vertices):
                print('No')
                break
        else:
            print('Yes')


if __name__ == '__main__':
    main()
"""
####################################################


####################################################
"""
import copy

n, m = map(int, input().split())
maps = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
for _ in range(int(input())):
    temp_map = copy.deepcopy(maps)
    vertices = list(map(int, input().split()))
    for vertex in vertices[1:]:
        temp_vertex = temp_map[vertex]
        for second_vertex in temp_vertex:
            temp_map[second_vertex].remove(vertex)
        temp_map[vertex] = []
    for list_ in temp_map:
        if list_:
            print('No')
            break
    else:
        print('Yes')
"""
####################################################
