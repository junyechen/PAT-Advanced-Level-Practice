"""
Mice and Rice is the name of a programming contest in which each programmer must write a piece of code to control the movements of a mouse in a given map. The goal of each mouse is to eat as much rice as possible in order to become a FatMouse.

First the playing order is randomly decided for N​P​​ programmers. Then every N​G​​ programmers are grouped in a match. The fattest mouse in a group wins and enters the next turn. All the losers in this turn are ranked the same. Every N​G​​ winners are then grouped in the next match until a final winner is determined.

For the sake of simplicity, assume that the weight of each mouse is fixed once the programmer submits his/her code. Given the weights of all the mice and the initial playing order, you are supposed to output the ranks for the programmers.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers: N​P​​ and N​G​​ (≤1000), the number of programmers and the maximum number of mice in a group, respectively. If there are less than N​G​​ mice at the end of the player's list, then all the mice left will be put into the last group. The second line contains N​P​​ distinct non-negative numbers W​i​​ (i=0,⋯,N​P​​−1) where each W​i​​ is the weight of the i-th mouse respectively. The third line gives the initial playing order which is a permutation of 0,⋯,N​P​​−1 (assume that the programmers are numbered from 0 to N​P​​−1). All the numbers in a line are separated by a space.
Output Specification:

For each test case, print the final ranks in a line. The i-th number is the rank of the i-th programmer, and all the numbers must be separated by a space, with no extra space at the end of the line.
Sample Input:

11 3
25 18 0 46 37 3 19 22 57 56 10
6 0 8 7 10 5 9 1 4 2 3

Sample Output:

5 5 5 2 5 5 5 3 1 3 5
"""

######################################################
"""
模拟题对我有点困难啊！
想了很久，写了很久，后来看了网上的解答才终于明了一个关键的步骤：
    对于每一轮淘汰的人的名次如何决定？
        只要 1+这一轮晋级的人数 就是该轮淘汰的人的名次！
    明白这个问题，解决这道题目就非常简单了！
另一个是关于题目理解的问题！
    第2行给的是i编号老鼠的体重
    第3行给的是按照游玩顺序排列的老鼠编号
        以题目给的示例为例：
            第一轮的第一组为：
                No. 6 19kg
                No. 0 25kg
                No. 8 57kg
"""
######################################################

np, ng = map(int, input().split())
w = list(map(int, input().split()))
p = list(map(int, input().split()))
pw = []
for r in range(np):
    pw.append([p[r], w[p[r]]])
rank = [1] * np
while len(pw) > 1:
    win = []
    lose = []
    for i in range(len(pw)//ng):
        max_index = i*ng
        for j in range(i*ng, (i+1)*ng):
            if pw[j][1] > pw[max_index][1]:
                max_index = j
        win.append(pw[max_index])
        for j in range(i*ng, (i+1)*ng):
            if j != max_index:
                lose.append(pw[j])
    if len(pw) % ng != 0:
        max_index = (len(pw) // ng) * ng
        for j in range(max_index, len(pw)):
            if pw[j][1] > pw[max_index][1]:
                max_index = j
        win.append(pw[max_index])
        for j in range((len(pw) // ng) * ng, len(pw)):
            if j != max_index:
                lose.append(pw[j])
    for i in lose:
        rank[i[0]] += len(win)
    pw = win
print(' '.join(map(str, rank)))

"""
np, ng = map(int, input().split())
w = list(map(int, input().split()))
p = list(map(int, input().split()))
pw = []
for r in range(np):
    pw.append([p[r], w[p[r]]])
rank_num = []
num = np
while num != 1:
    group = num // ng
    if num % ng != 0:
        group += 1
    rank_num.insert(0, num-group)
    num = group
rank_num.insert(0, 1)
rank_order = [1]
order = 1
for i in range(1, len(rank_num)):
    order += rank_num[i-1]
    rank_order.insert(0, order)
rank = [0] * np
r = 1
while len(pw) > 1:
    temp = []
    for i in range(len(pw)//ng):
        max_index = i*ng
        for j in range(i*ng, (i+1)*ng):
            if pw[j][1] > pw[max_index][1]:
                max_index = j
        temp.append(pw[max_index])
        rank[pw[max_index][0]] = r
    if len(pw) % ng != 0:
        max_index = (len(pw)//ng) * ng
        for j in range(max_index, len(pw)):
            if pw[j][1] > pw[max_index][1]:
                max_index = j
        temp.append(pw[max_index])
        rank[pw[max_index][0]] = r
    pw = temp
    r += 1
for i in rank[:-1]:
    print(rank_order[i], end=' ')
print(rank_order[rank[-1]])
"""
