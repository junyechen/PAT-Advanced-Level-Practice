"""
Given a constant K and a singly linked list L, you are supposed to reverse the links of every K elements on L. For example, given L being 1→2→3→4→5→6, if K=3, then you must output 3→2→1→6→5→4; if K=4, you must output 4→3→2→1→5→6.
Input Specification:

Each input file contains one test case. For each case, the first line contains the address of the first node, a positive N (≤10​5​​) which is the total number of nodes, and a positive K (≤N) which is the length of the sublist to be reversed. The address of a node is a 5-digit nonnegative integer, and NULL is represented by -1.

Then N lines follow, each describes a node in the format:

Address Data Next

where Address is the position of the node, Data is an integer, and Next is the position of the next node.
Output Specification:

For each case, output the resulting ordered linked list. Each node occupies a line, and is printed in the same format as in the input.
Sample Input:

00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218

Sample Output:

00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1
"""

######################################################
"""
本题只要注意不管怎么翻转，值总是跟着头地址，尾地址不是非常重要
因为总的数据不大，可以设立10^5数组，分别存储地址的值与地址的下一地址指针
然后按顺序将节点的地址放入一个list中
然后对list进行翻转，得到输出顺序的头地址
最后输出

本题python会超时，无法解决
"""
######################################################

val = [0 for _ in range(100000)]
tail = [-1 for _ in range(100000)]
first, n, k = map(int, input().split())
for _ in range(n):
    add, value, next_ = map(int, input().split())
    val[add] = value
    tail[add] = next_
head = first
link = []
while head != -1:
    link.append(head)
    head = tail[head]
n = len(link)
for i in range(n//k):
    link[i*k:(i+1)*k] = reversed(link[i*k:(i+1)*k])
for i in range(n-1):
    print('%05d %d %05d' % (link[i], val[link[i]], link[i+1]))
print('%05d %d %d' % (link[-1], val[link[-1]], -1))
