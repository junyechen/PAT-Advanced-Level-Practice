"""
The lowest common ancestor (LCA) of two nodes U and V in a tree is the deepest node that has both U and V as descendants.

Given any two nodes in a binary tree, you are supposed to find their LCA.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers: M (≤ 1,000), the number of pairs of nodes to be tested; and N (≤ 10,000), the number of keys in the binary tree, respectively. In each of the following two lines, N distinct integers are given as the inorder and preorder traversal sequences of the binary tree, respectively. It is guaranteed that the binary tree can be uniquely determined by the input sequences. Then M lines follow, each contains a pair of integer keys U and V. All the keys are in the range of int.
Output Specification:

For each given pair of U and V, print in a line LCA of U and V is A. if the LCA is found and A is the key. But if A is one of U and V, print X is an ancestor of Y. where X is A and Y is the other node. If U or V is not found in the binary tree, print in a line ERROR: U is not found. or ERROR: V is not found. or ERROR: U and V are not found..
Sample Input:

6 8
7 2 3 4 6 5 1 8
5 3 7 2 6 4 8 1
2 6
8 1
7 9
12 -3
0 8
99 99

Sample Output:

LCA of 2 and 6 is 3.
8 is an ancestor of 1.
ERROR: 9 is not found.
ERROR: 12 and -3 are not found.
ERROR: 0 is not found.
ERROR: 99 and 99 are not found.
"""

##############################################################################
"""
python不能AC

第一次做根据树的遍历性质，想到判断共同祖先，则必定满足在中序遍历中共同祖先在A, B之间的条件。因此遍历A，B之间的数，代入先序遍历，判断该数是否在A，B的左边以满足根左右的顺序，这种方法只用了树的1种性质，中间有大量测试数据是浪费的，故最后两例超时。

第二次则利用树的遍历，但是在函数中直接纳入遍历数组，导致最后两例多次遍历后内存超限。

第三次则仅利用下标，而不纳入整个遍历数组，但是最后两例显示结果非零，不清楚原因。
"""
##############################################################################


def find_root(in_order_left, pre_order_left):
    global in_order, pre_order, a_index_in, b_index_in
    root = pre_order[pre_order_left]
    root_index_in = in_order.index(root)
    if a_index_in <= root_index_in <= b_index_in or b_index_in <= root_index_in <= a_index_in:
        if a_index_in == root_index_in:
            print('%d is an ancestor of %d.' % (a, b))
        elif b_index_in == root_index_in:
            print('%d is an ancestor of %d.' % (b, a))
        else:
            print('LCA of %d and %d is %d.' % (a, b, root))
    else:
        if a_index_in < root_index_in:
            find_root(in_order_left, pre_order_left + 1)
        else:
            find_root(root_index_in + 1, pre_order_left + root_index_in - in_order_left + 1)


m, n = map(int, input().split())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    if a not in in_order and b not in in_order:
        print('ERROR: %d and %d are not found.' % (a, b))
    elif a not in in_order:
        print('ERROR: %d is not found.' % a)
    elif b not in in_order:
        print('ERROR: %d is not found.' % b)
    else:
        a_index_in = in_order.index(a)
        b_index_in = in_order.index(b)
        find_root(0, 0)

##############################################################################
"""
def find_root(i_order, p_order):
    global a, b
    root = p_order[0]
    root_index_i = i_order.index(root)
    a_index_i = i_order.index(a)
    b_index_i = i_order.index(b)
    if a_index_i <= root_index_i <= b_index_i or b_index_i <= root_index_i <= a_index_i:
        if a_index_i == root_index_i:
            print('%d is an ancestor of %d.' % (a, b))
        elif b_index_i == root_index_i:
            print('%d is an ancestor of %d.' % (b, a))
        else:
            print('LCA of %d and %d is %d.' % (a, b, root))
    else:
        if a_index_i < root_index_i:
            find_root(i_order[:root_index_i], p_order[1:root_index_i+1])
        else:
            find_root(i_order[root_index_i+1:], p_order[root_index_i+1:])


m, n = map(int, input().split())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    if a not in in_order and b not in in_order:
        print('ERROR: %d and %d are not found.' % (a, b))
    elif a not in in_order:
        print('ERROR: %d is not found.' % a)
    elif b not in in_order:
        print('ERROR: %d is not found.' % b)
    else:
        find_root(in_order, pre_order)
"""
##############################################################################

##############################################################################
"""
m, n = map(int, input().split())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    if a not in in_order and b not in in_order:
        print('ERROR: %d and %d are not found.' % (a, b))
    elif a not in in_order:
        print('ERROR: %d is not found.' % a)
    elif b not in in_order:
        print('ERROR: %d is not found.' % b)
    else:
        a_index_pre = pre_order.index(a)
        b_index_pre = pre_order.index(b)
        a_index_in = in_order.index(a)
        b_index_in = in_order.index(b)
        for i in range(a_index_in + 1, b_index_in):
            c_index_pre = pre_order.index(in_order[i])
            if b_index_pre > a_index_pre > c_index_pre:
                print('LCA of %d and %d is %d.' % (a, b, in_order[i]))
                break
        else:
            for i in range(b_index_in + 1, a_index_in):
                c_index_pre = pre_order.index(in_order[i])
                if a_index_pre > b_index_pre > c_index_pre:
                    print('LCA of %d and %d is %d.' % (a, b, in_order[i]))
                    break
            else:
                if a_index_pre > b_index_pre:
                    print('%d is an ancestor of %d.' % (b, a))
                else:
                    print('%d is an ancestor of %d.' % (a, b))
"""
##############################################################################
