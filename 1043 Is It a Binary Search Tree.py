"""
A Binary Search Tree (BST) is recursively defined as a binary tree which has the following properties:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
If we swap the left and right subtrees of every node, then the resulting tree is called the Mirror Image of a BST.

Now given a sequence of integer keys, you are supposed to tell if it is the preorder traversal sequence of a BST or the mirror image of a BST.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤1000). Then N integer keys are given in the next line. All the numbers in a line are separated by a space.

Output Specification:

For each test case, first print in a line YES if the sequence is the preorder traversal sequence of a BST or the mirror image of a BST, or NO if not. Then if the answer is YES, print in the next line the postorder traversal sequence of that tree. All the numbers in a line must be separated by a space, and there must be no extra space at the end of the line.

Sample Input 1:

7
8 6 5 7 10 8 11
Sample Output 1:

YES
5 7 6 8 11 10 8
Sample Input 2:

7
8 10 11 8 6 7 5
Sample Output 2:

YES
11 8 10 7 5 6 8
Sample Input 3:

7
8 6 8 5 10 9 11
Sample Output 3:

NO
"""

###############################
"""
这题思路比较简单，一开始想着现根据先序遍历与搜索二叉树的性质重建树，然后对树做中序遍历，若是按顺序递增或递减，则说明是对的，最后再做后序遍历。
后来发现在判断能否重建时，可将判断的条件放在重建时，而不是放在中序遍历时。
最后看到网上的更优解法，因为搜索二叉树的性质，可以通过先序遍历直接得到后序遍历，省去中间的重建步骤。

在完成后出现2出返回非零，1个是因为python默认限制递归深度为1000，超过就报错，导入sys，在sys.setrecursionlimit()中更改递归深度即可
另一个返回非零错误是当只有1个数字的时候，情况考虑到了，但是代码习惯不佳，if else 两个代码块是独立关系，不应该把else的代码块拎出一部分玩蛇。哎，浪费1个多小时。
"""
###############################

import sys

sys.setrecursionlimit(5000)


class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def tree(seq):
    global flag
    if flag:
        if seq:
            root = Node(seq[0])
            i = 1
            while i < len(seq) and seq[0] > seq[i]:
                i += 1
            j = len(seq) - 1
            while j > 0 and seq[0] <= seq[j]:
                j -= 1
            if i - j != 1:
                flag = False
            else:
                root.left_node = tree(seq[1:i])
                root.right_node = tree(seq[j + 1:len(seq)])
        else:
            root = None
        return root
    else:
        return None


def mir_tree(seq):
    global flag
    if flag:
        if seq:
            root = Node(seq[0])
            i = 1
            while i < len(seq) and seq[0] <= seq[i]:
                i += 1
            j = len(seq) - 1
            while j > 0 and seq[0] > seq[j]:
                j -= 1
            if i - j != 1:
                flag = False
            else:
                root.left_node = mir_tree(seq[1:i])
                root.right_node = mir_tree(seq[j + 1:len(seq)])
        else:
            root = None
        return root
    else:
        return None


def post_order(root):
    global p_order
    if root:
        post_order(root.left_node)
        post_order(root.right_node)
        p_order.append(root.value)


n = int(input())
key = [int(_) for _ in input().split()]
if n == 1:
    print("YES")
    print(key[0])
else:
    if key[1] < key[0]:
        flag = True
        t = tree(key)
    else:
        flag = True
        t = mir_tree(key)
    if flag:
        print("YES")
        p_order = []
        post_order(t)
        print(' '.join(list(map(str, p_order))))
    else:
        print("NO")

####################################################################
"""
class Node:
    def __init__(self, value='', left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def tree(seq):
    if seq:
        root = Node(seq[0])
        i = 1
        while i < len(seq) and seq[0] > seq[i]:
            i += 1
        root.left_node = tree(seq[1:i])
        if i < len(seq):
            root.right_node = tree(seq[i:])
        else:
            root.right_node = None
    else:
        root = None
    return root


def mir_tree(seq):
    if seq:
        root = Node(seq[0])
        i = 1
        while i < len(seq) and seq[0] <= seq[i]:
            i += 1
        root.left_node = mir_tree(seq[1:i])
        if i < len(seq):
            root.right_node = mir_tree(seq[i:])
        else:
            root.right_node = None
    else:
        root = None
    return root


def mid_order(root):
    global last, flag
    if flag:
        if root:
            mid_order(root.left_node)
            if root.value >= last:
                last = root.value
            else:
                flag = False
            mid_order(root.right_node)


def mir_mid_order(root):
    global last, flag
    if flag:
        if root:
            mir_mid_order(root.left_node)
            if root.value <= last:
                last = root.value
            else:
                flag = False
            mir_mid_order(root.right_node)


def post_order(root):
    global p_order
    if root:
        post_order(root.left_node)
        post_order(root.right_node)
        p_order.append(root.value)


n = int(input())
key = [int(_) for _ in input().split()]
if n == 1:
    print("YES")
    print(key[0])
else:
    if key[1] < key[0]:
        t = tree(key)
        last = -10e9
        flag = True
        mid_order(t)
    else:
        t = mir_tree(key)
        last = 10e9
        flag = True
        mir_mid_order(t)
    if flag:
        print("YES")
        p_order = []
        post_order(t)
        print(' '.join(list(map(str, p_order))))
    else:
        print("NO")
"""
####################################################################
