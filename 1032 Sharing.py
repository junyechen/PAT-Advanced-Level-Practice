"""To store English words, one method is to use linked lists and store a word letter by letter. To save some space,
we may let the words share the same sublist if they share the same suffix. For example, loading and being are stored
as showed in Figure 1.

fig.jpg

Figure 1

You are supposed to find the starting position of the common suffix (e.g. the position of i in Figure 1).

Input Specification:

Each input file contains one test case. For each case, the first line contains two addresses of nodes and a positive
N (≤10 ​5 ​​ ), where the two addresses are the addresses of the first nodes of the two words, and N is the total
number of nodes. The address of a node is a 5-digit positive integer, and NULL is represented by −1.

Then N lines follow, each describes a node in the format:

Address Data Next whereAddress is the position of the node, Data is the letter contained by this node which is an
English letter chosen from { a-z, A-Z }, and Next is the position of the next node.

Output Specification:

For each case, simply output the 5-digit starting position of the common suffix. If the two words have no common
suffix, output -1 instead.

Sample Input 1:

11111 22222 9
67890 i 00002
00010 a 12345
00003 g -1
12345 D 67890
00002 n 00003
22222 B 23456
11111 L 00001
23456 e 67890
00001 o 00010
Sample Output 1:

67890
Sample Input 2:

00001 00002 4
00001 a 10001
10001 s -1
00002 a 10002
10002 t -1
Sample Output 2:

-1
"""


#####################################################
"""
本以为这是一道非常简单的题目
本题一开始想使用取巧的办法，即当有共同节点时，下一节点指针的地址会出现2次（如测试案例1中的67890，和测试案例2中的-1，都出现了2次），因此找到出现2个的下一节点指针地址，就是我们我们要的答案，但PAT网站的测试总是出现答案错误，或者返回非零，而牛客网上的测试案例是全部通过的。
后来发觉这样的取巧有点问题，因为2个字符串的关系可以是相等、包含、分叉与分离，我这种方法只考虑了后两种，前两中无法用我的方法检出共同地址，那么做一下更改，将两个字符串的头地址加入下一节指针地址列表中，这样出现2次的算法可以检出包含关系，至于相等可在最前直接比较头地址。
    但这样的算法仍出现错误。
经过广泛查阅，最后得出结论只能是PAT的测试案例不符合题目描述，在案例中的所有节点并不完全来自于2个字符串，而是混杂了其他字符串，导致用该算法，2个下一节点指针地址出现信息混淆。
不使用取巧办法，即通过链表计算地址，则python必定超时。
"""
#####################################################

w1, w2, n = input().split()
D, S = {}, set([])
for i in range(int(n)):
    a, b, c = input().split()
    D[a] = c
while w1 != '-1':
    S.add(w1)
    w1 = D[w1]
while w2 != '-1':
    if w2 in S:
        print(w2)
        break
    w2 = D[w2]
else:
    print(-1)

####################################################
"""
add1, add2, n = input().split()
address = set([add1, add2])
result = add1
flag = True
for _ in range(int(n)):
    temp = input()[-5:]
    if temp[-2:] == '-1':
        if '-1' in address:
            result = -1
            break
        else:
            address.add('-1')
    else:
        if temp in address:
            result = temp
            break
        else:
            address.add(temp)
print(result)
"""
####################################################

####################################################
"""
add1, add2, n = input().split()
address = set([add1, add2])
flag = True
result = add1
for _ in range(int(n)):
    if flag:
        temp = input().split()
        if temp[2] in address:
            if temp[2] == '-1':
                #print(-1)
                result = -1
            else:
                #print(temp[2])
                result = temp[2]
            flag = False
        else:
            address.add(temp[2])
    else:
        input()
print(result)
"""
####################################################

####################################################
"""
add1, add2, n = input().split()
address = set([add1, add2])
result = add1
flag = True
for _ in range(int(n)):
    temp = input().split()
    if temp[2] in address:
        if temp[2] == '-1':
            #print(-1)
            result = -1
        else:
            #print(temp[2])
            result = temp[2]
        flag = False
    else:
        address.add(temp[2])
print(result)
"""
####################################################

####################################################
"""
add1, add2, n = input().split()
address = set([add1])
flag = True
result = 0
for _ in range(int(n)):
    if flag:
        temp = input().split()
        if temp[2] in address:
            if temp[2] == '-1':
                #print(-1)
                result = -1
            else:
                #print(temp[2])
                result = temp[2]
            flag = False
        else:
            address.add(temp[2])
    else:
        input()
if result == 0:
    print(add2)
else:
    print(result)
"""
####################################################

####################################################
"""
add1, add2, n = [int(_) for _ in input().split()]
add = {}
flag = True
for _ in range(n):
    if flag:
        temp = input().split()
        if temp[2] in add:
            if temp[2] == '-1':
                #print(-1)
                result = -1
            else:
                #print(temp[2])
                result = temp[2]
            flag = False
        else:
            add[temp[2]] = 1
    else:
        input()
print(result)
"""
####################################################

####################################################
"""
add1, add2, n = [int(_) for _ in input().split()]
word = {}
flag = 0
for _ in range(n):
    temp = input().split()
    word[int(temp[0])] = int(temp[2])
    if temp[2] == '-1':
        flag += 1
if flag == 2:
    print(-1)
else:
    word1 = [add1]
    while word[word1[-1]] != -1:
        word1.append(word[word1[-1]])
    word2 = add2
    while word2 not in word1:
        word2 = word[word2]
    print("%05d" % word2)
"""
####################################################

####################################################
"""
add1, add2, n = [int(_) for _ in input().split()]
word = [0] * 100000
flag = 0
for _ in range(n):
    temp = input().split()
    word[int(temp[0])] = int(temp[2])
    if temp[2] == '-1':
        flag += 1
if flag == 2:
    print(-1)
else:
    word1 = [add1]
    while word[word1[-1]] != -1:
        word1.append(word[word1[-1]])
    word2 = add2
    while word2 not in word1:
        word2 = word[word2]
    print(word2)
"""
####################################################
