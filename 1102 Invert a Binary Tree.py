"""
The following is from Max Howell @twitter:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so fuck off.






Now it's your turn to prove that YOU CAN invert a binary tree!
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10) which is the total number of nodes in the tree -- and hence the nodes are numbered from 0 to N−1. Then N lines follow, each corresponds to a node from 0 to N−1, and gives the indices of the left and right children of the node. If the child does not exist, a - will be put at the position. Any pair of children are separated by a space.
Output Specification:

For each test case, print in the first line the level-order, and then in the second line the in-order traversal sequences of the inverted tree. There must be exactly one space between any adjacent numbers, and no extra space at the end of the line.
Sample Input:

8
1 -
- -
0 -
2 7
- -
- -
5 -
4 6

Sample Output:

3 7 2 6 4 0 5 1
6 5 7 4 3 2 0 1
"""

########################################################################
"""
翻转二叉树即为左右子树对称调换，题目求翻转二叉树的层序遍历和中序遍历

不同于前面1099 Build A Binary Search Tree，该题目根节点还需要自己求，可采用的方法是：不作为叶节点出现的节点即为根节点
找到根节点后就非常简单：
    层序遍历注意每一层翻转
    中序遍历只需要在最后翻转
"""
########################################################################


class Node:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None


def find_root():
    global nodes, N
    child_node = []
    for i in range(N):
        left_child, right_child = nodes[i].left, nodes[i].right
        if left_child is not None:
            child_node.append(left_child)
        if right_child is not None:
            child_node.append(right_child)
    return list(set(range(N)) - set(child_node))[0]


def get_in_order(root):
    global nodes, in_order
    if root is not None:
        left_child, right_child = nodes[root].left, nodes[root].right
        get_in_order(left_child)
        in_order.append(root)
        get_in_order(right_child)
    else:
        return


def get_level_order(root):
    global nodes, level_order
    temp_seq = [root]
    while temp_seq:
        temp = []
        for node in temp_seq:
            left_child, right_child = nodes[node].left, nodes[node].right
            if left_child is not None:
                temp.append(left_child)
            if right_child is not None:
                temp.append(right_child)
        level_order += temp_seq[::-1]
        temp_seq = temp


N = int(input())
nodes = [Node(_) for _ in range(N)]
for i in range(N):
    left, right = input().split()
    if left != '-':
        nodes[i].left = int(left)
    if right != '-':
        nodes[i].right = int(right)
root_node = find_root()
in_order = []
get_in_order(root_node)
level_order = []
get_level_order(root_node)
print(' '.join(map(str, level_order)))
print(' '.join(map(str, in_order[::-1])))
