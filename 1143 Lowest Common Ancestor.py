"""
The lowest common ancestor (LCA) of two nodes U and V in a tree is the deepest node that has both U and V as descendants.

A binary search tree (BST) is recursively defined as a binary tree which has the following properties:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

Given any two nodes in a BST, you are supposed to find their LCA.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers: M (≤ 1,000), the number of pairs of nodes to be tested; and N (≤ 10,000), the number of keys in the BST, respectively. In the second line, N distinct integers are given as the preorder traversal sequence of the BST. Then M lines follow, each contains a pair of integer keys U and V. All the keys are in the range of int.
Output Specification:

For each given pair of U and V, print in a line LCA of U and V is A. if the LCA is found and A is the key. But if A is one of U and V, print X is an ancestor of Y. where X is A and Y is the other node. If U or V is not found in the BST, print in a line ERROR: U is not found. or ERROR: V is not found. or ERROR: U and V are not found..
Sample Input:

6 8
6 3 1 2 5 4 8 7
2 5
8 7
1 9
12 -3
0 8
99 99

Sample Output:

LCA of 2 and 5 is 3.
8 is an ancestor of 7.
ERROR: 9 is not found.
ERROR: 12 and -3 are not found.
ERROR: 0 is not found.
ERROR: 99 and 99 are not found.
"""

########################################################################
"""
python超时无法解决

一开始还想复杂，实际上抓住搜索二叉树的性质以及先序遍历的根左右即可，对先序遍历依次遍历，第一个在2个给定节点大小之间的节点即为最小共同祖先。
"""
########################################################################

m, n = map(int, input().split())
pre_order = list(map(int, input().split()))
pre_order_set = set(pre_order)
for _ in range(m):
    a, b = map(int, input().split())
    if (a not in pre_order_set) and (b not in pre_order_set):
        print('ERROR: %d and %d are not found.' % (a, b))
    elif a not in pre_order_set:
        print('ERROR: %d is not found.' % a)
    elif b not in pre_order_set:
        print('ERROR: %d is not found.' % b)
    else:
        for i in pre_order:
            if a <= i <= b or b <= i <= a:
                if i == a:
                    print('%d is an ancestor of %d.' % (a, b))
                elif i == b:
                    print('%d is an ancestor of %d.' % (b, a))
                else:
                    print('LCA of %d and %d is %d.' % (a, b, i))
                break
        # flag = True
        # if a > b:
        #     temp = a
        #     a = b
        #     b = temp
        #     flag = False
        # for i in pre_order:
        #     if a < i <= b:
        #         if b == i:
        #             if flag:
        #                 print('%d is an ancestor of %d.' % (i, a))
        #             else:
        #                 print('%d is an ancestor of %d.' % (i, b))
        #         else:
        #             if flag:
        #                 print('LCA of %d and %d is %d.' % (a, b, i))
        #             else:
        #                 print('LCA of %d and %d is %d.' % (b, a, i))
        #         break


#########################################################################
"""
def pre_order_traversal(p_order):
    global temp_a, temp_b, a, b, flag
    if p_order and flag:
        root = p_order[0]
        if temp_a < root <= temp_b:
            if temp_b == root:
                print('%d is an ancestor of %d.' % (temp_b, temp_a))
            else:
                print('LCA of %d and %d is %d.' % (a, b, root))
            flag = False
            return
        for i in range(1, len(p_order)):
            if p_order[i] >= root:
                pre_order_traversal(p_order[1:i])
                pre_order_traversal(p_order[i:])
                break
        else:
            pre_order_traversal(p_order[1:])


m, n = map(int, input().split())
pre_order = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    if a in pre_order and b in pre_order:
        if a > b:
            temp_a, temp_b = b, a
        else:
            temp_a, temp_b = a, b
        flag = True
        pre_order_traversal(pre_order)
    elif a not in pre_order and b not in pre_order:
        print('ERROR: %d and %d are not found.' % (a, b))
    elif a not in pre_order:
        print('ERROR: %d is not found.' % a)
    else:
        print('ERROR: %d is not found.' % b)
"""
#########################################################################
