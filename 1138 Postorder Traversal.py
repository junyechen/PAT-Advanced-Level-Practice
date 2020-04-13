"""
Suppose that all the keys in a binary tree are distinct positive integers. Given the preorder and inorder traversal sequences, you are supposed to output the first number of the postorder traversal sequence of the corresponding binary tree.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤ 50,000), the total number of nodes in the binary tree. The second line gives the preorder sequence and the third line gives the inorder sequence. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in one line the first number of the postorder traversal sequence of the corresponding binary tree.
Sample Input:

7
1 2 3 4 5 6 7
2 3 1 5 4 7 6

Sample Output:

3
"""


##########################################################################################
"""
一开始使用数组递归，出现内存超限错误，后面使用数组下标进行递归（使用先序左边界，中序左边界，中序右边界3个指标即可），出现运行超时
无法做到python AC，只能用C++ AC
"""
##########################################################################################


def get_post_order(pre_left, in_left, in_right):
    global pre_order, in_order
    if in_left <= in_right:
        root = pre_order[pre_left]
        root_index_in = in_order.index(root)
        left_length = root_index_in - in_left
        get_post_order(pre_left+1, in_left, root_index_in-1)
        get_post_order(pre_left+left_length+1, root_index_in + 1, in_right)
        print(root)
        exit(0)


n = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))
get_post_order(0, 0, n-1)


#########################################################################
"""
def get_post_order(pre_o, in_o):
    if pre_o:
        r = pre_o[0]
        r_index_in = in_o.index(r)
        get_post_order(pre_o[1:r_index_in + 1], in_o[:r_index_in])
        get_post_order(pre_o[r_index_in + 1:], in_o[r_index_in + 1:])
        print(r)
        exit(0)
    else:
        return


n = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))
get_post_order(pre_order, in_order)
"""
#########################################################################
