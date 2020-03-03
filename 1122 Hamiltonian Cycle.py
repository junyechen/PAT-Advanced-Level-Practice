"""
The "Hamilton cycle problem" is to find a simple cycle that contains every vertex in a graph. Such a cycle is called a "Hamiltonian cycle".

In this problem, you are supposed to tell if a given cycle is a Hamiltonian cycle.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers N (2<N≤200), the number of vertices, and M, the number of edges in an undirected graph. Then M lines follow, each describes an edge in the format Vertex1 Vertex2, where the vertices are numbered from 1 to N. The next line gives a positive integer K which is the number of queries, followed by K lines of queries, each in the format:

n V​1​​ V​2​​ ... V​n​​

where n is the number of vertices in the list, and V​i​​'s are the vertices on a path.
Output Specification:

For each query, print in a line YES if the path does form a Hamiltonian cycle, or NO if not.
Sample Input:

6 10
6 2
3 4
1 5
2 5
3 1
4 1
1 6
6 3
1 2
4 5
6
7 5 1 4 3 6 2 5
6 5 1 4 3 6 2
9 6 2 1 6 3 4 5 2 6
4 1 2 5 1
7 6 1 3 4 5 2 6
7 6 1 2 5 4 3 1

Sample Output:

YES
NO
NO
NO
YES
NO
"""

###########################################################
"""
这题就是要看懂题目，没有下面的知识储备，根本不理哈密顿环到底是什么。因为题目中只说了这个环包括图的所有顶点，而没有说能否重复，是否必须要回到起点。

    哈密顿图：
    哈密顿图是一个无向图，由指定的起点通往指定的重点，途中经过所有节点有且只经过一次。
    在图论中，通常指的是哈密顿回路，即经过图中所有顶点有且只有一次，最终回到出发点。
    哈密顿回路为NP完全问题，暂不存在多项式内的解法。
    
    欧拉图：
    类似的有欧拉图：图中经过每天边有且只有一次，若最终回到出发点，则是欧拉回路。
    判断是否存在欧拉回路，是有定理的，网上可以找找。、

了解了哈密顿图之后，不难得到如下性质：
1. 顶点个数必须为图顶点个数+1
2. 起始点与终点是一样的
3. 路径当中没有重复点
4. 路径是存在的
只要上述4点有1点没有满足，则必定不为哈密顿图

如此，本题就非常简单
"""
###########################################################

n, m = map(int, input().split())
maps = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a][b] = maps[b][a] = 1
for _ in range(int(input())):
    queries = list(map(int, input().split()))
    if queries[0] != n+1:
        print('NO')
    elif queries[1] != queries[-1]:
        print('NO')
    elif len(set(queries[1:])) != n:
        print('NO')
    else:
        for i in range(1, len(queries)-1):
            if maps[queries[i]][queries[i+1]] != 1:
                print('NO')
                break
        else:
            print('YES')
