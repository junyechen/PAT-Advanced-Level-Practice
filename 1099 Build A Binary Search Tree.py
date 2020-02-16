"""
A Binary Search Tree (BST) is recursively defined as a binary tree which has the following properties:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

Given the structure of a binary tree and a sequence of distinct integer keys, there is only one way to fill these keys into the tree so that the resulting tree satisfies the definition of a BST. You are supposed to output the level order traversal sequence of that tree. The sample is illustrated by Figure 1 and 2.

figBST.jpg
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤100) which is the total number of nodes in the tree. The next N lines each contains the left and the right children of a node in the format left_index right_index, provided that the nodes are numbered from 0 to N−1, and 0 is always the root. If one child is missing, then −1 will represent the NULL child pointer. Finally N distinct integer keys are given in the last line.
Output Specification:

For each test case, print in one line the level order traversal sequence of that tree. All the numbers must be separated by a space, with no extra space at the end of the line.
Sample Input:

9
1 6
2 3
-1 -1
-1 4
5 -1
-1 -1
7 -1
-1 8
-1 -1
73 45 11 58 82 25 67 38 42

Sample Output:

58 25 82 11 38 67 45 73 42
"""

####################################################################
"""
本题思路明确，得到树的结构，通过中序遍历将各个数字赋入树中，最后通过层序遍历得到答案

一开始只有22分的原因为，未理解题目的输入意思，以为每一层为按照先序遍历得到的树的分布，而实际上每一层就是相应编号节点的左右子树分布，与遍历顺序无关！
"""
####################################################################


class Node:
    def __init__(self, index):
        self.index = index
        self.value = None
        self.left = -1
        self.right = -1


def set_value_by_middle_order(root):
    global nodes, data
    if root == -1:
        return
    else:
        left_child, right_child = nodes[root].left, nodes[root].right
        set_value_by_middle_order(left_child)
        nodes[root].value = data.pop(0)
        set_value_by_middle_order(right_child)


n = int(input())
nodes = [Node(_) for _ in range(n)]
for i in range(n):
    left, right = map(int, input().split())
    if left != -1:
        nodes[i].left = left
    if right != -1:
        nodes[i].right = right
data = list(map(int, input().split()))
data.sort()
set_value_by_middle_order(0)
temp_seq = [0]
res = [nodes[0].value]
while temp_seq:
    temp = []
    for node in temp_seq:
        left, right = nodes[node].left, nodes[node].right
        if left != -1:
            temp.append(left)
            res.append(nodes[left].value)
        if right != -1:
            temp.append(right)
            res.append(nodes[right].value)
    temp_seq = temp
print(" ".join(map(str, res)))


"""
def get_middle_order(root):
    global LDR, tree_data
    if root == -1:
        return
    else:
        left, right = map(int, input().split())
        tree_data[root] = [left, right]
        get_middle_order(left)
        LDR.append(root)
        get_middle_order(right)


def get_level_order(root):
    global level_order, tree_data
    level_order.append(root)
    temp_seq = level_order.copy()
    while temp_seq:
        temp = []
        for node in temp_seq:
            left, right = tree_data[node]
            if left != -1:
                temp.append(left)
            if right != -1:
                temp.append(right)
        level_order += temp
        temp_seq = temp


n = int(input())
tree_data = {}
LDR = []
level_order = []
get_middle_order(0)
get_level_order(0)
data = list(map(int, input().split()))
data.sort()
BST = {}
for i in range(n):
    BST[LDR[i]] = data[i]
res = []
for i in range(n):
    res.append(BST[level_order[i]])
print(' '.join(map(str, res)))
"""
