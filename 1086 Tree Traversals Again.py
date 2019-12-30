"""
An inorder binary tree traversal can be implemented in a non-recursive way with a stack. For example, suppose that when a 6-node binary tree (with the keys numbered from 1 to 6) is traversed, the stack operations are: push(1); push(2); push(3); pop(); pop(); push(4); pop(); pop(); push(5); push(6); pop(); pop(). Then a unique binary tree (shown in Figure 1) can be generated from this sequence of operations. Your task is to give the postorder traversal sequence of this tree.

Figure 1
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤30) which is the total number of nodes in a tree (and hence the nodes are numbered from 1 to N). Then 2N lines follow, each describes a stack operation in the format: "Push X" where X is the index of the node being pushed onto the stack; or "Pop" meaning to pop one node from the stack.
Output Specification:

For each test case, print the postorder traversal sequence of the corresponding tree in one line. A solution is guaranteed to exist. All the numbers must be separated by exactly one space, and there must be no extra space at the end of the line.
Sample Input:
6
Push 1
Push 2
Push 3
Pop
Pop
Push 4
Pop
Pop
Push 5
Push 6
Pop
Pop

Sample Output:
3 4 2 6 5 1
"""

###############################################################
"""
本题push顺序为先根遍历，pop顺序为中根遍历，求后根遍历，因此比较简单

以往都是通过建立树的方式得到遍历，本次尝试不通过建立树的方式得到：
    核心函数为get_post_order_via_pre_in
    可以看到和建立树的函数差不太多：
        建立树的方式在前序遍历中找到根节点，根据根节点在中序遍历中划分出左子树和右子树，从而在前序遍历中也找到左子树和右子树
        递归调用重复，最后形成完整的树
    而不建立树的方式，根据后序遍历特点，是先遍历左子树，再遍历右子树，最后返回根节点，过程大体相同，但省去了建树和重新遍历
"""
###############################################################

def get_post_order_via_pre_in(p_order, i_order):
    if p_order:
        left_length = i_order.index(p_order[0])
        get_post_order_via_pre_in(p_order[1:1 + left_length], i_order[:left_length])
        get_post_order_via_pre_in(p_order[1 + left_length:], i_order[1 + left_length:])
        postorder.append(p_order[0])


n = int(input())
temp = []
inorder = []
preorder = []
for _ in range(n * 2):
    code = input()
    if code == 'Pop':
        inorder.append(temp.pop())
    else:
        temp.append(int(code.split()[1]))
        preorder.append(temp[-1])
postorder = []
get_post_order_via_pre_in(preorder, inorder)
print(' '.join(map(str, postorder)))

"""
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_post_order(root):
    global postorder
    if root.left:
        get_post_order(root.left)
    if root.right:
        get_post_order(root.right)
    postorder.append(root.value)


def in_order(p_order, i_order):
    if p_order:
        node = Node(p_order[0])
        left_length = i_order.index(p_order[0])
        node.left = in_order(p_order[1:1 + left_length], i_order[:left_length])
        node.right = in_order(p_order[1 + left_length:], i_order[1 + left_length:])
        return node
    else:
        return None


n = int(input())
temp = []
inorder = []
preorder = []
for _ in range(n * 2):
    code = input()
    if code == 'Pop':
        inorder.append(temp.pop())
    else:
        temp.append(int(code.split()[1]))
        preorder.append(temp[-1])
root = in_order(preorder, inorder)
postorder = []
get_post_order(root)
print(' '.join(map(str, postorder)))
"""
