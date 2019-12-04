"""
A Binary Search Tree (BST) is recursively defined as a binary tree which has the following properties:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

A Complete Binary Tree (CBT) is a tree that is completely filled, with the possible exception of the bottom level, which is filled from left to right.

Now given a sequence of distinct non-negative integer keys, a unique BST can be constructed if it is required that the tree must also be a CBT. You are supposed to output the level order traversal sequence of this BST.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤1000). Then N distinct non-negative integer keys are given in the next line. All the numbers in a line are separated by a space and are no greater than 2000.
Output Specification:

For each test case, print in one line the level order traversal sequence of the corresponding complete binary search tree. All the numbers in a line must be separated by a space, and there must be no extra space at the end of the line.
Sample Input:

10
1 2 3 4 5 6 7 8 9 0

Sample Output:

6 3 8 1 5 7 9 0 2 4
"""

#########################################
"""
这题有技巧，考的是完全二叉树的性质：
    性质1：
        在二叉树上的第i层上至多有2^(i-1)个节点（i>=1）
    性质2：
        深度为k的二叉树至多有(2^k)-1个节点（k>=1）
    性质3：
        n0、n1、n2分别代表节点的度数为0、1、2。n为总结点数
        n0 = n2+1;
        n=n0+n1+n2
        分支总线=n-1=n1+2n2
    性质4：
        具有n个节点的完全二叉树的深度为 └log2n┘+ 1
    性质5：
        如果对一颗有n个节点的完全二叉树（其深度为└log2n┘+1）的节点按层序编号，对于任意节点i有：
            如果i=1，则节点i是二叉树的根节点，无双亲；如果i>1，则其双亲节点是└i/2┘
            如果2i>n，则节点i无左孩子；否则其左孩子就是2i
            如果2i+1>n，则节点i无有右孩子；否则其右孩子就是2i+1
最重要的是性质5

此外还有一个重要的性质是，按照题目的有序树，则根据其性质，中序遍历必定是从小到大的有序数列
而要求的是层序遍历，刚好和根节点的基础序号相符，那么中序遍历得到根节点的基础序号，并将排序后的数值加载其上，最后按中序遍历的根节点基础序号顺序输出即可得到答案

本题非常巧妙
"""
#########################################


def generate(root):
    global n, po, res, keys
    if root > n:
        return
    else:
        generate(root*2)
        res[root-1] = keys[po]
        po += 1
        generate(root*2+1)


n = int(input())
keys = list(map(int, input().split()))
keys.sort()
po = 0
res = [0] * n
generate(1)
print(' '.join(list(map(str, res))))
