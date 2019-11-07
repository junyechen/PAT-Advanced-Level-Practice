"""
A linked list consists of a series of structures, which are not necessarily adjacent in memory. We assume that each structure contains an integer key and a Next pointer to the next structure. Now given a linked list, you are supposed to sort the structures according to their key values in increasing order.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive N (<10​5​​) and an address of the head node, where N is the total number of nodes in memory and the address of a node is a 5-digit positive integer. NULL is represented by −1.

Then N lines follow, each describes a node in the format:

Address Key Next

where Address is the address of the node in memory, Key is an integer in [−10​5​​,10​5​​], and Next is the address of the next node. It is guaranteed that all the keys are distinct and there is no cycle in the linked list starting from the head node.
Output Specification:

For each test case, the output format is the same as that of the input, where N is the total number of nodes in the list and all the nodes must be sorted order.
Sample Input:

5 00001
11111 100 -1
00001 0 22222
33333 100000 11111
12345 -1 33333
22222 1000 12345

Sample Output:

5 12345
12345 -1 00001
00001 0 11111
11111 100 22222
22222 1000 33333
33333 100000 -1
"""

#########################################################
"""
本题和之前的套路相同，但是一开始又陷进去了，仍需要注意给出的节点可能是不在指定链表中的，故一定要对链表做遍历，获得所有有效节点，接下来排序就行。
特殊情况为空链表
本题仍旧是python的超时问题，代码已无处精简
    根据简单测试，测试点3在遍历链表时即已超时
"""
#########################################################

n, head = input().split()
n = int(n)
node = {}
for _ in range(n):
    h, key, t = input().split()
    key = int(key)
    node[h] = [key, t]
link = []
while head != "-1":
    link.append([head, node[head][0]])
    head = node[head][1]
if len(link) == 0:
    print(0, -1)
else:
    link.sort(key=lambda x: x[1])
    print(len(link), link[0][0])
    for i in range(len(link) - 1):
        print(link[i][0], link[i][1], link[i + 1][0])
    print(link[-1][0], link[-1][1], -1)

"""
n, head = map(int, input().split())
node = {}
for _ in range(n):
    h, key, t = map(int, input().split())
    node[h] = [key, t]
link = []
while head != -1:
    link.append([head, node[head][0]])
    head = node[head][1]
if len(link) == 0:
    print(0, -1)
else:
    link.sort(key=lambda x: x[1])
    print("%d %05d" % (len(link), link[0][0]))
    for i in range(len(link) - 1):
        print("%05d %d %05d" % (link[i][0], link[i][1], link[i + 1][0]))
    print("%05d %d -1" % (link[-1][0], link[-1][1]))
"""

"""
n, head = map(int, input().split())
link = []
for _ in range(n):
    h, key, t = map(int, input().split())
    link.append([h, key])
link.sort(key=lambda x: x[1])
print("%d %05d" % (n, link[0][0]))
for i in range(n-1):
    print("%05d %d %05d" % (link[i][0], link[i][1], link[i+1][0]))
print("%05d %d -1" % (link[-1][0], link[-1][1]))
"""
