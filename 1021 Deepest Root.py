"""
A graph which is connected and acyclic can be considered a tree. The height of the tree depends on the selected root. Now you are supposed to find the root that results in a highest tree. Such a root is called the deepest root.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤10
​4
​​ ) which is the number of nodes, and hence the nodes are numbered from 1 to N. Then N−1 lines follow, each describes an edge by given the two adjacent nodes' numbers.

Output Specification:

For each test case, print each of the deepest roots in a line. If such a root is not unique, print them in increasing order of their numbers. In case that the given graph is not a tree, print Error: K components where K is the number of connected components in the graph.

Sample Input 1:

5
1 2
1 3
1 4
2 5
Sample Output 1:

3
4
5
Sample Input 2:

5
1 3
1 4
2 5
3 4
Sample Output 2:

Error: 2 components
"""


############################################################
"""
本题做起来颇为费劲，但是通过该题目认真学习了图的深度遍历，以及如何通过深度遍历确认图的连通分量（该名词也才在本题学会）
可通过连通分量确定图是"整体"还是"分割"以及"分割的数量"-->连通分量即可用于表征图的"分割"数量
在确定最大深度时，可从任意节点深度遍历找到最远点集合，再从最远点（集合里随便取一个节点）开始深度遍历找到与之相对应的最远点集合，两者取并集即为最深结点集合
"""
############################################################


def dfs(visit, i, relation, depth, max_depth, deep_root):
    visit[i] = 0
    depth += 1
    if depth > max_depth[0]:
        max_depth[0] = depth
        deep_root.clear()
        deep_root.append(i)
    elif depth == max_depth[0]:
        deep_root.append(i)
    for child in relation[i]:
        if visit[child]:
            dfs(visit, child, relation, depth, max_depth, deep_root)


N = int(input())
relation = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = [int(i) for i in input().split()]
    relation[a].append(b)
    relation[b].append(a)
visit = [1 for _ in range(N + 1)]
k = 0
depth = 0
max_depth = [0]
deep_root = []
for i in range(1, N + 1):
    if visit[i]:
        dfs(visit, i, relation, depth, max_depth, deep_root)
        k += 1
if k != 1:
    print("Error: %d components" % k)
else:
    d_root = deep_root
    visit = [1 for _ in range(N + 1)]
    depth = 0
    max_depth = [0]
    deep_root = []
    dfs(visit, d_root[0], relation, depth, max_depth, deep_root)
    d_root += deep_root
    for _ in sorted(list(set(d_root))):
        print(_)
