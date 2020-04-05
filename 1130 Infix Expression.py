"""
Given a syntax tree (binary), you are supposed to output the corresponding infix expression, with parentheses reflecting the precedences of the operators.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤ 20) which is the total number of nodes in the syntax tree. Then N lines follow, each gives the information of a node (the i-th line corresponds to the i-th node) in the format:

data left_child right_child

where data is a string of no more than 10 characters, left_child and right_child are the indices of this node's left and right children, respectively. The nodes are indexed from 1 to N. The NULL link is represented by −1. The figures 1 and 2 correspond to the samples 1 and 2, respectively.
infix1.JPG 	infix2.JPG
Figure 1 	Figure 2
Output Specification:

For each case, print in a line the infix expression, with parentheses reflecting the precedences of the operators. Note that there must be no extra parentheses for the final expression, as is shown by the samples. There must be no space between any symbols.
Sample Input 1:

8
* 8 7
a -1 -1
* 4 1
+ 2 5
b -1 -1
d -1 -1
- -1 6
c -1 -1

Sample Output 1:

(a+b)*(c*(-d))

Sample Input 2:

8
2.35 -1 -1
* 6 1
- -1 4
% 7 8
+ 2 3
a -1 -1
str -1 -1
871 -1 -1

Sample Output 2:

(a*2.35)+(-(str%871))
"""

####################################
"""
给出节点得出中序遍历，只是多了括号的问题
可先判断节点是否为叶节点，若为叶节点，则不加括号
在最后输出的时候除去根节点的括号

但若只有1个节点，则会多除去一次根节点的括号，因此需单独讨论
"""
####################################


class Node:
    def __init__(self, index):
        self.index = index
        self.value = None
        self.left = self.right = -1


def get_in_order(r):
    global nodes, in_order
    if r == -1:
        return
    else:
        if nodes[r].left == nodes[r].right == -1:
            pass
        else:
            in_order.append('(')

        get_in_order(nodes[r].left)
        in_order.append(nodes[r].value)
        get_in_order(nodes[r].right)

        if nodes[r].left == nodes[r].right == -1:
            pass
        else:
            in_order.append(')')


n = int(input())
nodes = [Node(_) for _ in range(n+1)]
root = list(range(1, n+1))
for i in range(1, n+1):
    value, left, right = input().split()
    left = int(left)
    right = int(right)
    nodes[i].value = value
    nodes[i].left = left
    nodes[i].right = right
    if left in root:
        root.remove(left)
    if right in root:
        root.remove(right)
in_order = []
get_in_order(root[0])
if n == 1:
    print(in_order[0])
else:
    print(''.join(map(str, in_order[1:len(in_order)-1])))
