"""
Suppose that all the keys in a binary tree are distinct positive integers. A unique binary tree can be determined by a given pair of postorder and inorder traversal sequences, or preorder and inorder traversal sequences. However, if only the postorder and preorder traversal sequences are given, the corresponding tree may no longer be unique.

Now given a pair of postorder and preorder traversal sequences, you are supposed to output the corresponding inorder traversal sequence of the tree. If the tree is not unique, simply output any one of them.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤ 30), the total number of nodes in the binary tree. The second line gives the preorder sequence and the third line gives the postorder sequence. All the numbers in a line are separated by a space.
Output Specification:

For each test case, first printf in a line Yes if the tree is unique, or No if not. Then print in the next line the inorder traversal sequence of the corresponding binary tree. If the solution is not unique, any answer would do. It is guaranteed that at least one solution exists. All the numbers in a line must be separated by exactly one space, and there must be no extra space at the end of the line.
Sample Input 1:

7
1 2 3 4 6 7 5
2 6 7 4 5 3 1

Sample Output 1:

Yes
2 1 6 4 7 3 5

Sample Input 2:

4
1 2 3 4
2 4 3 1

Sample Output 2:

No
2 1 3 4
"""


#######################################################################################################################
"""
根据前序、后序无法得到唯一的树，这是因为根左右、左右根的序列下，如果只有一颗子树，则无法通过前序和后序确定是左子树还是右子树
如：
    1 2 3 4
    2 4 3 1
    
    1是根节点，2、3、4是子树
    根据前序，2是节点，根据后序4、3是另一颗子树，故可暂时得到1-(2)-(3,4)
    1的左子树只有1个节点，为2
    1的右子树有2个节点
        根据前序，表明3是根节点，4是子树
        此时根据前后序无法推断4是3的左子树还是右子树，故序列不唯一

因此判断不唯一性就是发现前序中得到的子根节点，在后序中证明是唯一子根节点
可以预先假设子根节点都是左子树的根节点，若在后序遍历中找不到右子树节点，则证明树不唯一

中序遍历则按照左-中-右的方式遍历即可 无需建树
"""
#######################################################################################################################


def get_in_order_via_pre_and_post_order(pre, post):
    global unique, in_order
    if pre:
        if len(pre) == 1:
            in_order.append(pre[0])
            return
        else:
            pre_left_root = pre[1]
            post_left_root_index = post.index(pre_left_root)
            if len(post)-1-post_left_root_index == 1:
                unique = False
            get_in_order_via_pre_and_post_order(pre[1:1+post_left_root_index+1], post[:post_left_root_index+1])
            in_order.append(pre[0])
            get_in_order_via_pre_and_post_order(pre[1+post_left_root_index+1:], post[post_left_root_index+1:len(post)-1])
    else:
        return


n = int(input())
pre_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
unique = True
in_order = []
get_in_order_via_pre_and_post_order(pre_order, post_order)
if unique:
    print('Yes')
else:
    print('No')
print(' '.join(map(str, in_order)))
