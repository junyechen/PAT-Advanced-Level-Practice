"""
A family hierarchy is usually presented by a pedigree tree. Your job is to count those family members who have no child.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 0<N<100, the number of nodes in a tree, and M (<N), the number of non-leaf nodes. Then M lines follow, each in the format:

ID K ID[1] ID[2] ... ID[K]

where ID is a two-digit number representing a given non-leaf node, K is the number of its children, followed by a sequence of two-digit ID's of its children. For the sake of simplicity, let us fix the root ID to be 01.

The input ends with N being 0. That case must NOT be processed.
Output Specification:

For each test case, you are supposed to count those family members who have no child for every seniority level starting from the root. The numbers must be printed in a line, separated by a space, and there must be no extra space at the end of each line.

The sample case represents a tree with only 2 nodes, where 01 is the root and 02 is its only child. Hence on the root 01 level, there is 0 leaf node; and on the next level, there is 1 leaf node. Then we should output 0 1 in a line.
Sample Input:

2 1
01 1 02

Sample Output:

0 1
"""

################################################
"""
在最后做截断操作时，忘记break了，导致第一次没有AC。
借鉴网上的一些代码，我的算法思路还是可行的。
"""
################################################

def search(tree, root, depth, pedigree):
    if tree[root]:
        for i in tree[root]:
            search(tree, i, depth + 1, pedigree)
    else:
        pedigree[depth] += 1

N, M = [int(i) for i in input().split()]
if N == 0:
    exit(0)
tree = [[] for i in range(N + 1)]
for i in range(M):
    temp = [int(i) for i in input().split()]
    tree[temp[0]] = temp[2:]
pedigree = [0] * (N + 1)
search(tree, 1, 1, pedigree)
for i in range(N - 1,0,-1):
    if pedigree[i] != 0:
        pedigree = pedigree[:i + 1]
        break
print(' '.join(list(map(str,pedigree[1:]))))
