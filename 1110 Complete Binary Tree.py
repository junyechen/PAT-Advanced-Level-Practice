"""
Given a tree, you are supposed to tell if it is a complete binary tree.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤20) which is the total number of nodes in the tree -- and hence the nodes are numbered from 0 to N−1. Then N lines follow, each corresponds to a node, and gives the indices of the left and right children of the node. If the child does not exist, a - will be put at the position. Any pair of children are separated by a space.
Output Specification:

For each case, print in one line YES and the index of the last node if the tree is a complete binary tree, or NO and the index of the root if not. There must be exactly one space separating the word and the number.
Sample Input 1:

9
7 8
- -
- -
- -
0 1
2 3
4 5
- -
- -

Sample Output 1:

YES 8

Sample Input 2:

8
- -
4 5
0 6
- -
2 3
- 7
- -
- -

Sample Output 2:

NO 1
"""

###################################################
"""
这题看似很简单，但是因没有完全掌握完全二叉树的性质而导致艰难
本题最重要的性质：通过层序遍历，遍历最后一位时序列中的节点个数即为整个二叉树的节点个数
"""
###################################################

# def bfs(wait_que, depth):
#     global node
#     while wait_que:
#         temp = []
#         for i in wait_que:
#             temp.append(node[i][0])
#             temp.append(node[i][1])
#         for i in range(len(temp)):
#             if temp[i] == -1:
#                 break
#         else:
#             wait_que = temp
#             continue
#         if i != 0 and i % 2 != 0:
#             return -1, 0
#         for j in range(i, len(temp)):
#             if temp[j] != -1:
#                 return -1, 0
#         if i == 0:
#             break
#         wait_que = temp[:i]
#     return depth, wait_que[-1]


def bfs(wait_que, depth):
    global node
    count = 1
    last = wait_que[0]
    while wait_que:
        temp = []
        for i in wait_que:
            temp.append(node[i][0])
            temp.append(node[i][1])
        for i in range(len(temp)):
            if temp[i] == -1:
                if len(node) == count:
                    return depth, last
                else:
                    return -1, 0
            else:
                count += 1
                last = temp[i]
        wait_que = temp
    return depth, wait_que[-1]


N = int(input())
node = []
root = [1] * N
for i in range(N):
    child = input().split()
    if child[0] == '-':
        child[0] = -1
    else:
        child[0] = int(child[0])
        root[child[0]] = 0
    if child[1] == '-':
        child[1] = -1
    else:
        child[1] = int(child[1])
        root[child[1]] = 0
    node.append(child)
for i in range(N):
    if root[i] == 1:
        root = i
        break
max_depth, last_node = bfs([root], 0)
if max_depth == -1:
    print('NO', root)
else:
    print('YES', last_node)
