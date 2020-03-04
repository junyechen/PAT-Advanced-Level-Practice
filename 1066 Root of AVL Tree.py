"""
An AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Figures 1-4 illustrate the rotation rules.

Now given a sequence of insertions, you are supposed to tell the root of the resulting AVL tree.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤20) which is the total number of keys to be inserted. Then N distinct integer keys are given in the next line. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print the root of the resulting AVL tree in one line.
Sample Input 1:

5
88 70 61 96 120

Sample Output 1:

70

Sample Input 2:

7
88 70 61 96 120 90 65

Sample Output 2:

88
"""

######################################
"""
本题花了非常多的时间，主要考查AVL树，是平衡的搜索二叉树，关键在于插入数值后的平衡
1. 简单插入：从根节点开始，如果数值小于根节点，则进入左叶节点，如果数值大于根节点，则进入右叶节点，如果左（右）叶节点不存在，则新增此数值的叶节点
2. 平衡：因为简单插入会导致搜索二叉树不等臂，造成搜索效能下降，故如果出现不等臂（即题目中，某节点的左右子树高度相差大于1），就需要平衡（因为我们是一个个节点插入，所以左右子树高度最大差值为2）
    1. 如果左子树高，则为右旋
        1. 将左叶节点设为新的根节点
        2. 将左叶节点的右子树设为原根节点的左子树
        3. 将原根节点设为左叶节点的右叶节点
    2. 如果右子树高，则为左旋
        1. 将右叶节点设为新的根节点
        2. 将右叶节点的左子树设为原根节点的右子树
        3. 将原根节点设为右叶节点的左叶节点
    3. 当在左边插入时，即插入值小于“比较根节点”，但若插入值大于“比较根节点”的左叶节点，则表明插入的值应为“比较根节点”的左叶节点，而非孙节点，故可以“比较根节点”的左叶节点为根进行左旋，然后再进行1步骤
    4. 当在右边插入时，即插入值大等于于“比较根节点”，但若插入值小于等于“比较根节点”的右叶节点，则表明插入的值应为“比较根节点”的右叶节点，而非孙节点，故可以“比较根节点”的右叶节点为根进行右旋，然后再进行2步骤
"""
######################################


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def rotate_left(self):
        root = self.right
        self.right = root.left
        root.left = self
        return root

    def rotate_right(self):
        root = self.left
        self.left = root.right
        root.right = self
        return root

    def get_height(self):
        if self.left:
            left = self.left.get_height()
        else:
            left = 0
        if self.right:
            right = self.right.get_height()
        else:
            right = 0
        return max(left, right) + 1

    def insert(self, value):
        if not self.value:
            self = Node(value)
        else:
            if self.value > value:
                if self.left:
                    self.left = self.left.insert(value)
                else:
                    self.left = Node(value)
                if self.left:
                    left = self.left.get_height()
                else:
                    left = 0
                if self.right:
                    right = self.right.get_height()
                else:
                    right = 0
                if left - right == 2:
                    if value >= self.left.value:
                        self.left = self.left.rotate_left()
                    self = self.rotate_right()
            else:
                if self.right:
                    self.right = self.right.insert(value)
                else:
                    self.right = Node(value)
                if self.left:
                    left = self.left.get_height()
                else:
                    left = 0
                if self.right:
                    right = self.right.get_height()
                else:
                    right = 0
                if right - left == 2:
                    if value < self.right.value:
                        self.right = self.right.rotate_right()
                    self = self.rotate_left()
        return self


input()
root = Node()
for i in map(int, input().split()):
    root = root.insert(i)
print(root.value)
