"""
An AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Figures 1-4 illustrate the rotation rules.
F1.jpg 	F2.jpg
F3.jpg 	F4.jpg

Now given a sequence of insertions, you are supposed to output the level-order traversal sequence of the resulting AVL tree, and to tell if it is a complete binary tree.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤ 20). Then N distinct integer keys are given in the next line. All the numbers in a line are separated by a space.
Output Specification:

For each test case, insert the keys one by one into an initially empty AVL tree. Then first print in a line the level-order traversal sequence of the resulting AVL tree. All the numbers in a line must be separated by a space, and there must be no extra space at the end of the line. Then in the next line, print YES if the tree is complete, or NO if not.
Sample Input 1:

5
88 70 61 63 65

Sample Output 1:

70 63 88 61 65
YES

Sample Input 2:

8
88 70 61 96 120 90 65 68

Sample Output 2:

88 65 96 61 70 90 120 68
NO
"""


#####################################
"""
再次温故了AVL树，复习的时间就比之间预习的时间短很多
但是对python的类的写法不熟悉，花了很久时间，最终还是参考了别人的代码
其中对于节点height的设定比较巧妙，默认是0（叶节点），如果是None则是-1

由于数据量非常小，所以都能AC通过
"""
#####################################


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def check_balance(self, root):
        return self.height(root.left) - self.height(root.right)

    def right_rotation(self, root):
        r = root.left
        root.left = r.right
        r.right = root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        return r

    def left_rotation(self, root):
        r = root.right
        root.right = r.left
        r.left = root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        return r

    def insertion(self, node):
        if self.root is None:
            self.root = node
        else:
            self.root = self.insertion_(node, self.root)

    def insertion_(self, node, root):
        if root is None:
            root = node
        elif node.value < root.value:
            root.left = self.insertion_(node, root.left)
            if self.check_balance(root) == 2:
                if self.check_balance(root.left) == 1:
                    root = self.right_rotation(root)
                else:
                    root.left = self.left_rotation(root.left)
                    root = self.right_rotation(root)
            root.height = max(self.height(root.left), self.height(root.right)) + 1
        else:
            root.right = self.insertion_(node, root.right)
            if self.check_balance(root) == -2:
                if self.check_balance(root.right) == -1:
                    root = self.left_rotation(root)
                else:
                    root.right = self.right_rotation(root.right)
                    root = self.left_rotation(root)
            root.height = max(self.height(root.left), self.height(root.right)) + 1
        return root

    def in_order(self):
        if self.root is None:
            return []
        else:
            res = wait_que = [self.root]
            flag = True
            num = 1
            while wait_que:
                temp = []
                for node in wait_que:
                    if node.left is not None:
                        temp.append(node.left)
                        if flag:
                            num += 1
                    else:
                        if flag:
                            flag = False
                    if node.right is not None:
                        temp.append(node.right)
                        if flag:
                            num += 1
                    else:
                        if flag:
                            flag = False
                wait_que = temp
                res += wait_que
        if num == len(res):
            flag = True
        else:
            flag = False
        return res + [flag]


n = int(input())
numbers = list(map(int, input().split()))
avl_tree = AVLTree()
for i in range(n):
    avl_tree.insertion(Node(numbers[i]))
res = avl_tree.in_order()
print(' '.join(map(str, [x.value for x in res[:-1]])))
if res[-1]:
    print('YES')
else:
    print('NO')
