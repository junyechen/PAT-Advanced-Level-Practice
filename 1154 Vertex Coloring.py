"""
A proper vertex coloring is a labeling of the graph's vertices with colors such that no two vertices sharing the same edge have the same color. A coloring using at most k colors is called a (proper) k-coloring.

Now you are supposed to tell if a given coloring is a proper k-coloring.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers N and M (both no more than 10​4​​), being the total numbers of vertices and edges, respectively. Then M lines follow, each describes an edge by giving the indices (from 0 to N−1) of the two ends of the edge.

After the graph, a positive integer K (≤ 100) is given, which is the number of colorings you are supposed to check. Then K lines follow, each contains N colors which are represented by non-negative integers in the range of int. The i-th color is the color of the i-th vertex.
Output Specification:

For each coloring, print in a line k-coloring if it is a proper k-coloring for some positive k, or No if not.
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
4
0 1 0 1 4 1 0 1 3 0
0 1 0 1 4 1 0 1 0 0
8 1 0 1 4 1 0 5 3 0
1 2 3 4 5 6 7 8 8 9

Sample Output:

4-coloring
No
6-coloring
No
"""

######################################################
"""
非常简单，一次通过
"""
######################################################

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
for _ in range(int(input())):
    coloring = list(map(int, input().split()))
    for a, b in edges:
        if coloring[a] == coloring[b]:
            print('No')
            break
    else:
        print('%d-coloring' % len(set(coloring)))
