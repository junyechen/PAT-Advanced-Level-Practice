"""
A Binary Search Tree (BST) is recursively defined as a binary tree which has the following properties:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Insert a sequence of numbers into an initially empty binary search tree. Then you are supposed to count the total number of nodes in the lowest 2 levels of the resulting tree.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤1000) which is the size of the input sequence. Then given in the next line are the N integers in [−10001000] which are supposed to be inserted into an initially empty binary search tree.
Output Specification:

For each case, print in one line the numbers of nodes in the lowest 2 levels of the resulting tree in the format:

n1 + n2 = n

where n1 is the number of nodes in the lowest level, n2 is that of the level above, and n is the sum.
Sample Input:

9
25 30 42 16 20 20 35 -5 28

Sample Output:

2 + 4 = 6
"""


########################################
"""
本题学习了二叉搜索树的插入构建，了解二叉搜索树的基本算法，比较简单
"""
########################################


class Node:
    def __init__(self, index):
        self.index = index
        self.value = None
        self.left = None
        self.right = None
        self.height = 0


def main():
    n = int(input())
    number = list(map(int, input().split()))
    nodes = [Node(_) for _ in range(n)]
    max_height = 0
    nodes[0].value = number[0]
    for i in range(1, n):
        root = nodes[0]
        height = 0
        while root:
            father = root
            height += 1
            if number[i] <= root.value:
                root = root.left
            else:
                root = root.right
        nodes[i].value = number[i]
        nodes[i].height = height
        if height > max_height:
            max_height = height
        root = nodes[i]
        if root.value <= father.value:
            father.left = root
        else:
            father.right = root
    last_one = last_two = 0
    for i in range(n):
        if nodes[i].height == max_height:
            last_one += 1
        elif nodes[i].height == max_height - 1:
            last_two += 1
    print(last_one, '+', last_two, '=', last_one+last_two)


if __name__ == "__main__":
    main()
