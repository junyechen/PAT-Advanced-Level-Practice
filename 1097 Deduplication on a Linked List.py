"""
Given a singly linked list L with integer keys, you are supposed to remove the nodes with duplicated absolute values of the keys. That is, for each value K, only the first node of which the value or absolute value of its key equals K will be kept. At the mean time, all the removed nodes must be kept in a separate list. For example, given L being 21→-15→-15→-7→15, you must output 21→-15→-7, and the removed list -15→15.
Input Specification:

Each input file contains one test case. For each case, the first line contains the address of the first node, and a positive N (≤10​5​​) which is the total number of nodes. The address of a node is a 5-digit nonnegative integer, and NULL is represented by −1.

Then N lines follow, each describes a node in the format:

Address Key Next

where Address is the position of the node, Key is an integer of which absolute value is no more than 10​4​​, and Next is the position of the next node.
Output Specification:

For each case, output the resulting linked list first, then the removed list. Each node occupies a line, and is printed in the same format as in the input.
Sample Input:

00100 5
99999 -7 87654
23854 -15 00000
87654 15 -1
00000 -15 99999
00100 21 23854

Sample Output:

00100 21 23854
23854 -15 99999
99999 -7 -1
00000 -15 87654
87654 15 -1
"""

######################################################
"""
开辟10^5数组，和之前类似题目相同思路建立链表，设立集合去重

超时，只能用C++
"""
######################################################

node = [[] for i in range(100000)]
head, n = map(int, input().split())
for _ in range(n):
    add, value, next_add = map(int, input().split())
    node[add] = [value, next_add]
key = {abs(node[head][0])}
reserve = [head]
remove = []
next_add = node[head][1]
while next_add != -1:
    temp = node[next_add]
    if abs(temp[0]) in key:
        remove.append(next_add)
        next_add = temp[1]
    else:
        reserve.append(next_add)
        key.add(abs(temp[0]))
        next_add = temp[1]
for i in range(len(reserve)-1):
    print("%05d %d %05d" % (reserve[i], node[reserve[i]][0], reserve[i+1]))
print("%05d %d -1" % (reserve[-1], node[reserve[-1]][0]))
for i in range(len(remove)-1):
    print("%05d %d %05d" % (remove[i], node[remove[i]][0], remove[i + 1]))
print("%05d %d -1" % (remove[-1], node[remove[-1]][0]))
