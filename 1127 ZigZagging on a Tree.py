"""
Suppose that all the keys in a binary tree are distinct positive integers. A unique binary tree can be determined by a given pair of postorder and inorder traversal sequences. And it is a simple standard routine to print the numbers in level-order. However, if you think the problem is too simple, then you are too naive. This time you are supposed to print the numbers in "zigzagging order" -- that is, starting from the root, print the numbers level-by-level, alternating between left to right and right to left. For example, for the following tree you must output: 1 11 5 8 17 12 20 15.

zigzag.jpg
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤30), the total number of nodes in the binary tree. The second line gives the inorder sequence and the third line gives the postorder sequence. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print the zigzagging sequence of the tree in a line. All the numbers in a line must be separated by exactly one space, and there must be no extra space at the end of the line.
Sample Input:

8
12 11 20 17 1 15 8 5
12 20 17 11 15 8 5 1

Sample Output:

1 11 5 8 17 12 20 15

"""


###########################################################################################################
"""
简单题，建树，层序遍历（层序稍微有点变通）

也可以通过非建树方式得到层序（建立层-节点字典序列）

"""
###########################################################################################################


class Nodes:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    level_order_by_level = {}

    def __init__(self):
        self.root = None

    def get_level_order_by_in_order_and_post_order(self, in_order, post_order, level):
        if in_order:
            if level in Tree.level_order_by_level:
                Tree.level_order_by_level[level].append(post_order[-1])
            else:
                Tree.level_order_by_level[level] = [post_order[-1]]
            r_index = in_order.index(post_order[-1])
            self.get_level_order_by_in_order_and_post_order(in_order[:r_index], post_order[:r_index], level + 1)
            self.get_level_order_by_in_order_and_post_order(in_order[r_index + 1:], post_order[r_index:len(post_order) - 1], level + 1)

    def get_tree_by_in_order_and_post_order(self, in_order, post_order):
        if in_order:
            r = Nodes(post_order[-1])
            r_index = in_order.index(post_order[-1])
            r.left = self.get_tree_by_in_order_and_post_order(in_order[:r_index], post_order[:r_index])
            r.right = self.get_tree_by_in_order_and_post_order(in_order[r_index + 1:],
                                                               post_order[r_index:len(post_order) - 1])
            return r
        else:
            return None

    def get_zig_zaging(self):
        wait_seq = {0: [self.root]}
        level = 0
        while wait_seq[level]:
            temp = []
            for node in wait_seq[level]:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                level += 1
                wait_seq[level] = temp
            else:
                break
        zig_zaging_seq = []
        for i in range(len(wait_seq.keys())):
            if i % 2 == 0:
                zig_zaging_seq += wait_seq[i][::-1]
            else:
                zig_zaging_seq += wait_seq[i]
        return zig_zaging_seq


def main():
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    tree = Tree()
    # tree.root = tree.get_tree_by_in_order_and_post_order(in_order, post_order)
    tree.get_level_order_by_in_order_and_post_order(in_order, post_order, 0)
    zig_zaging_seq = []
    for i in range(len(Tree.level_order_by_level.keys())):
        if i % 2 == 0:
            zig_zaging_seq += Tree.level_order_by_level[i][::-1]
        else:
            zig_zaging_seq += Tree.level_order_by_level[i]
    print(' '.join(map(str, zig_zaging_seq)))


if __name__ == '__main__':
    main()
