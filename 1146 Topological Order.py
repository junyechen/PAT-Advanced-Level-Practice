"""
This is a problem given in the Graduate Entrance Exam in 2018: Which of the following is NOT a topological order obtained from the given directed graph? Now you are supposed to write a program to test each of the options.

gre.jpg
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers N (≤ 1,000), the number of vertices in the graph, and M (≤ 10,000), the number of directed edges. Then M lines follow, each gives the start and the end vertices of an edge. The vertices are numbered from 1 to N. After the graph, there is another positive integer K (≤ 100). Then K lines of query follow, each gives a permutation of all the vertices. All the numbers in a line are separated by a space.
Output Specification:

Print in a line all the indices of queries which correspond to "NOT a topological order". The indices start from zero. All the numbers are separated by a space, and there must no extra space at the beginning or the end of the line. It is graranteed that there is at least one answer.
Sample Input:

6 8
1 2
1 3
5 2
5 4
2 3
2 6
3 4
6 4
5
1 5 2 3 6 4
5 1 2 6 3 4
5 1 2 3 6 4
5 2 1 6 3 4
1 2 3 4 5 6

Sample Output:

3 4
"""

##################################################
"""
本题学习了拓扑序列的定义，总是从0度顶点（进入该顶点的道路条数为0）开始，然后该顶点发出的道路均撤除，再次从0度顶点开始。
一开始想着把拓扑序列完全得出，就是先遍历出0度顶点，然后排除，然后再遍历出0度顶点，这样最后得到的层状的序列，如果最后序列不是该层状序列的集合，则不为拓扑序列。
但是结果不对，而且超时，最后采用了一步步探索选项的方法。
"""
##################################################

n, m = map(int, input().split())
route_in = [0 for _ in range(n + 1)]
route_out = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    route_in[b] += 1
    route_out[a].append(b)
res = []
for i in range(int(input())):
    route_in_copy = route_in.copy()
    route_out_copy = route_out.copy()
    for node in list(map(int, input().split())):
        if route_in_copy[node] != 0:
            res.append(i)
            break
        else:
            for node_ in route_out_copy[node]:
                route_in_copy[node_] -= 1
print(*res)

##############################################
"""
n, m = map(int, input().split())
route_in = [0 for _ in range(n+1)]
route_out = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    route_in[b] += 1
    route_out[a].append(b)
res = []
remain = set(range(1, n+1))
while remain:
    temp = set()
    for node in remain:
        if route_in[node] == 0:
            temp.add(node)
    for node in temp:
        for node_ in route_out[node]:
            route_in[node_] -= 1
    res.append(temp)
    remain = remain - temp
output = []
for i in range(int(input())):
    seq = list(map(int, input().split()))
    pos = 0
    for sets in res:
        if set(seq[pos:pos+len(sets)]) == sets:
            pos += len(sets)
        else:
            output.append(i)
            break
# print(' '.join(map(str, output)))
print(*output)
"""
##############################################
