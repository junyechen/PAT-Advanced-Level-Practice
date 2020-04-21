"""
A clique is a subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent. A maximal clique is a clique that cannot be extended by including one more adjacent vertex. (Quoted from https://en.wikipedia.org/wiki/Clique_(graph_theory))

Now it is your job to judge if a given subset of vertices can form a maximal clique.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers Nv (≤ 200), the number of vertices in the graph, and Ne, the number of undirected edges. Then Ne lines follow, each gives a pair of vertices of an edge. The vertices are numbered from 1 to Nv.

After the graph, there is another positive integer M (≤ 100). Then M lines of query follow, each first gives a positive number K (≤ Nv), then followed by a sequence of K distinct vertices. All the numbers in a line are separated by a space.
Output Specification:

For each of the M queries, print in a line Yes if the given subset of vertices can form a maximal clique; or if it is a clique but not a maximal clique, print Not Maximal; or if it is not a clique at all, print Not a Clique.
Sample Input:

8 10
5 6
7 8
6 4
3 6
4 5
2 3
8 2
2 7
5 3
3 4
6
4 5 4 3 6
3 2 8 7
2 2 3
1 1
3 4 3 6
3 3 2 1

Sample Output:

Yes
Yes
Yes
Yes
Not Maximal
Not a Clique
"""

#############################################################################
"""
##python有超时问题，利用main可以降低超时发生率

##具体算法即为先检查给出的集合是否两两联系，若没有，则表明不为clique；然后再对集合外的点对集合内的点是否两两联系，若有1个集合外的点，则表明不为最大clique

经过网上的指点，本题实质上是集合问题，用集合的解法能有效减少一一比对的时间开销，从而解决超时问题
判断是否为clique：
    对于给定集合，如果该集合中的某个顶点的不相邻顶点与给定集合有交集，表明该顶点与交集的顶点不相邻，然而该顶点与交集的顶点同属于给定集合，所以给定集合不为clique
判断是否为max_clique：
    遍历所有给定集合外顶点，如果该顶点相邻顶点集合完全包含给定集合，表明该顶点与给定集合的顶点都相邻，但该顶点不属于给定集合，所以给定集合不为max_clique
"""
#############################################################################


def judge(clique):
    global relation, not_in_relation, nv
    for vertex in clique:
        if not_in_relation[vertex] & clique:
            return 'Not a Clique'
    not_in_clique = set(range(1, nv + 1)) - clique
    for vertex in not_in_clique:
        if clique.issubset(relation[vertex]):
            return 'Not Maximal'
    return 'Yes'


nv, ne = map(int, input().split())
relation = [{i} for i in range(nv + 1)]
not_in_relation = [set() for i in range(nv + 1)]
for _ in range(ne):
    a, b = map(int, input().split())
    relation[a].add(b)
    relation[b].add(a)
whole_set = set(range(1, nv + 1))
for i in range(1, nv + 1):
    not_in_relation[i] = whole_set - relation[i]
for _ in range(int(input())):
    print(judge(set(list(map(int, input().split()))[1:])))

#############################################################################
"""
def main():
    nv, ne = map(int, input().split())
    relation = {}
    for i in range(1, nv + 1):
        relation[i * nv + i] = 1
    for _ in range(ne):
        a, b = map(int, input().split())
        relation[a * nv + b] = relation[b * nv + a] = 1
    for _ in range(int(input())):
        clique = list(map(int, input().split()))[1:]
        flag_clique = True
        for i in range(len(clique)):
            for j in range(i, len(clique)):
                if clique[i] * nv + clique[j] not in relation:
                    flag_clique = False
                    break
            else:
                continue
            break
        if flag_clique:
            flag_maximal_clique = True
            not_in_clique = list(set(list(range(1, nv + 1))) - set(clique))
            for i in range(len(not_in_clique)):
                for j in range(len(clique)):
                    if not_in_clique[i] * nv + clique[j] not in relation:
                        break
                else:
                    flag_maximal_clique = False
                    break
            if flag_maximal_clique:
                print('Yes')
            else:
                print('Not Maximal')
        else:
            print('Not a Clique')


if __name__ == '__main__':
    main()
"""
#############################################################################
