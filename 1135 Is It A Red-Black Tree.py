"""
There is a kind of balanced binary search tree named red-black tree in the data structure. It has the following 5 properties:

    (1) Every node is either red or black.
    (2) The root is black.
    (3) Every leaf (NULL) is black.
    (4) If a node is red, then both its children are black.
    (5) For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

For example, the tree in Figure 1 is a red-black tree, while the ones in Figure 2 and 3 are not.
rbf1.jpg 	rbf2.jpg 	rbf3.jpg
Figure 1 	Figure 2 	Figure 3

For each given binary search tree, you are supposed to tell if it is a legal red-black tree.
Input Specification:

Each input file contains several test cases. The first line gives a positive integer K (≤30) which is the total number of cases. For each case, the first line gives a positive integer N (≤30), the total number of nodes in the binary tree. The second line gives the preorder traversal sequence of the tree. While all the keys in a tree are positive integers, we use negative signs to represent red nodes. All the numbers in a line are separated by a space. The sample input cases correspond to the trees shown in Figure 1, 2 and 3.
Output Specification:

For each test case, print in a line "Yes" if the given tree is a red-black tree, or "No" if not.
Sample Input:

3
9
7 -2 1 5 -4 -11 8 14 -15
9
11 -2 1 -7 5 -4 8 14 -15
8
10 -7 5 -6 8 15 -11 17

Sample Output:

Yes
No
No
"""

################################################
"""
本题初步学习了红黑树，比AVL树复杂的二叉搜索树，但是时间效率优于AVL树。
红黑树插入操作比AVL树多的是颜色转换，并且以颜色准换优先。
总是插入红节点，然后分3种大的情况（不过具体代码还需要细推，文字需要优化，但本题不涉及插入操作）：
1. 根节点，则变黑
2. 父节点为黑节点，不做任何额外处理
3. 父节点为红节点：
    a. 叔叔节点为红节点，转变颜色即可
    b. 叔叔节点为黑节点，由红节点的分布可分为左左、左右、右左、右右型，进行相应的AVL旋转即可

本题利用的性质为：
1. 从根节点出发至所有子节点，所有路径黑节点的个数是一致的
2. 红节点的子节点都是黑节点 --> 不存在两个相邻的红节点

理解通了，还是较为简单，一次通过
"""
################################################


def seek(height, seq, quality):
    global judge, max_height
    if judge:
        if seq:
            if quality == -1 and seq[0] < 0:    # 如果父节点是红节点，而子节点也是红节点，则不符合红黑树规则
                judge = False
            else:
                root = abs(seq[0])
                for i in range(1, len(seq)):
                    if abs(seq[i]) > root:
                        left = seq[1:i]
                        right = seq[i:]
                        break
                else:
                    left = seq[1:]
                    right = []
                seek(height + (1+seq[0]//root)//2, left, seq[0]//root)
                seek(height + (1+seq[0]//root)//2, right, seq[0]//root)
        else:
            if max_height == 0:
                max_height = height
            else:
                if max_height != height:
                    judge = False
    else:
        return


for _ in range(int(input())):
    n = int(input())
    pre_order = list(map(int, input().split()))
    r = pre_order[0]
    if r < 0:
        judge = False
    else:
        judge = True
        max_height = 0
        seek(0, pre_order, 1)
    if judge:
        print('Yes')
    else:
        print('No')
