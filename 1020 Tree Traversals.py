"""
Suppose that all the keys in a binary tree are distinct positive integers. Given the postorder and inorder traversal sequences, you are supposed to output the level order traversal sequence of the corresponding binary tree.

Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤30), the total number of nodes in the binary tree. The second line gives the postorder sequence and the third line gives the inorder sequence. All the numbers in a line are separated by a space.

Output Specification:

For each test case, print in one line the level order traversal sequence of the corresponding binary tree. All the numbers in a line must be separated by exactly one space, and there must be no extra space at the end of the line.

Sample Input:

7
2 3 1 5 7 6 4
1 2 3 4 5 6 7
Sample Output:

4 1 6 3 5 7 2
"""

###################################################################
"""
本题相对简单，一次通过
复习python的class声明和运用，复习二叉树的先中后序遍历与层序遍历
"""
###################################################################


class Node:
    def __init__(self, value='', left_node=None, right_node=None):
        self.value = value
        self.leftNode = left_node
        self.rightNode = right_node


def tree(i_order, p_order):
    if i_order:
        root_ = Node(p_order[-1])
        root_loc = i_order.index(root_.value)
        root_.leftNode = tree(i_order[:root_loc], p_order[:root_loc])
        root_.rightNode = tree(i_order[root_loc + 1:], p_order[root_loc:len(p_order)-1])
    else:
        root_ = None
    return root_


def levelorder(root_):
    que = [root_]
    l_order = []
    while que:
        temp = que.pop(0)
        l_order.append(temp.value)
        if temp.leftNode:
            que.append(temp.leftNode)
        if temp.rightNode:
            que.append(temp.rightNode)
    return l_order


N = int(input())
post_order = input().split()
in_order = input().split()
root = tree(in_order, post_order)
level_order = levelorder(root)
print(' '.join(level_order))
