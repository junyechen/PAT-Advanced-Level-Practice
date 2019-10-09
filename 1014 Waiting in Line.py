"""
Suppose a bank has N windows open for service. There is a yellow line in front of the windows which devides the waiting area into two parts. The rules for the customers to wait in line are:

    The space inside the yellow line in front of each window is enough to contain a line with M customers. Hence when all the N lines are full, all the customers after (and including) the (NM+1)st one will have to wait in a line behind the yellow line.
    Each customer will choose the shortest line to wait in when crossing the yellow line. If there are two or more lines with the same length, the customer will always choose the window with the smallest number.
    Customer​i​​ will take T​i​​ minutes to have his/her transaction processed.
    The first N customers are assumed to be served at 8:00am.

Now given the processing time of each customer, you are supposed to tell the exact time at which a customer has his/her business done.

For example, suppose that a bank has 2 windows and each window may have 2 custmers waiting inside the yellow line. There are 5 customers waiting with transactions taking 1, 2, 6, 4 and 3 minutes, respectively. At 08:00 in the morning, customer​1​​ is served at window​1​​ while customer​2​​ is served at window​2​​. Customer​3​​ will wait in front of window​1​​ and customer​4​​ will wait in front of window​2​​. Customer​5​​ will wait behind the yellow line.

At 08:01, customer​1​​ is done and customer​5​​ enters the line in front of window​1​​ since that line seems shorter now. Customer​2​​ will leave at 08:02, customer​4​​ at 08:06, customer​3​​ at 08:07, and finally customer​5​​ at 08:10.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 4 positive integers: N (≤20, number of windows), M (≤10, the maximum capacity of each line inside the yellow line), K (≤1000, number of customers), and Q (≤1000, number of customer queries).

The next line contains K positive integers, which are the processing time of the K customers.

The last line contains Q positive integers, which represent the customers who are asking about the time they can have their transactions done. The customers are numbered from 1 to K.
Output Specification:

For each of the Q customers, print in one line the time at which his/her transaction is finished, in the format HH:MM where HH is in [08, 17] and MM is in [00, 59]. Note that since the bank is closed everyday after 17:00, for those customers who cannot be served before 17:00, you must output Sorry instead.
Sample Input:

2 2 7 5
1 2 6 4 3 534 2
3 4 5 6 7

Sample Output:

08:07
08:06
08:10
17:00
Sorry
"""

#################################################################################
"""
本题一开始想把所有情况列入队列里，导致情况复杂，运行超时。
可以将黄线内列一个容器，表明排队情况
针对每个窗口设计一个list用于放置每个窗口的第一人的结束时间，以用于弹出
针对每个窗口设计一个list用于存放队伍末尾人的结束时间，并将该时间存入结果list中
此后按照弹出时间找到最小窗口，删除该窗口第一人，将该窗口第二人的结束时间更新入弹出时间list，压入末尾人，更新队尾结束时间，并将该时间存入结果list中
"""
#################################################################################

N, M, K, Q = [int(i) for i in input().split()]
time = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
queues = [[0 for j in range(M)] for i in range(N)]
pop = [0 for _ in range(N)]
end = [0 for _ in range(N)]
ans = [0] * (K + 1)
cnt = 1
for j in range(M):
    for i in range(N):
        if cnt <= K:    #很关键，测试点2,3,4就是考虑黄线没填满的情况
            if j == 0:
                pop[i] = time[cnt - 1]
            queues[i][j] = cnt
            end[i] += time[cnt - 1]
            ans[cnt] = end[i]
            cnt += 1
while cnt <= K:
    minwin = pop.index(min(pop))
    queues[minwin].pop(0)
    pop[minwin] += time[queues[minwin][0] - 1]
    queues[minwin].append(cnt)
    end[minwin]+=time[cnt - 1]
    ans[cnt] = end[minwin]
    cnt += 1
for i in q:
    if ans[i] - time[i - 1] >= 540:
        print('Sorry')
    else:
        print("%02d:%02d" % (8 + ans[i] // 60,ans[i] % 60))

#################################################################################
"""
N, M, K, Q = [int(i) for i in input().split()]
time = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
winline = [[0 for j in range(M)] for i in range(N)]
timeline = [[0 for j in range(M)] for i in range(N)]
ansque = [0] * (K + 1)
cnt = 1
for j in range(M):
    for i in range(N):
        winline[i][j] = cnt
        timeline[i][j] = sum(timeline[i]) + time[cnt - 1]
        ansque[cnt] = timeline[i][j]
        cnt += 1
while cnt <= K:
    min = [0, timeline[0][0]]
    for i in range(N):
        if min[1] > timeline[i][0]:
            min = [i, timeline[i][0]]
    del winline[min[0]][0]
    del timeline[min[0]][0]
    winline[min[0]].append(cnt)
    timeline[min[0]].append(sum(timeline[min[0]]) + time[cnt - 1])
    ansque[cnt] = timeline[min[0]][-1]
    cnt += 1
for i in q:
    if ansque[i] - time[i - 1] >= 540:
        print('Sorry')
    else:
        print("%02d:%02d" % (8 + ansque[i] // 60,ansque[i] % 60))
"""
#################################################################################

#################################################################################
"""
N, M, K, Q = [int(i) for i in input().split()]
time = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
windows = [[[],[]] for i in range(N)]
ansque = [0] * (K + 1)
cnt = 1
for j in range(M):
    for i in range(N):
        windows[i][0].append(cnt)
        windows[i][1].append(sum(windows[i][1]) + time[cnt - 1])
        ansque[cnt]=windows[i][1][-1]
        cnt += 1
while cnt <= K:
    min = [0, windows[0][1][0]]
    for i in range(N):
        if min[1] > windows[i][1][0]:
            min[1] = windows[i][1][0]
            min[0] = i
    del windows[min[0]][0][0]
    del windows[min[0]][1][0]
    windows[min[0]][0].append(cnt)
    windows[min[0]][1].append(sum(windows[min[0]][1]) + time[cnt - 1])
    ansque[cnt]=windows[min[0]][1][-1]
    cnt += 1
for i in q:
    if ansque[i] > 540:
        print('Sorry')
    else:
        print("%02d:%02d" % (8 + ansque[i] // 60,ansque[i] % 60))
"""
#################################################################################

#################################################################################
"""
N, M, K, Q = [int(i) for i in input().split()]
time = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
windows = [[[],[]] for i in range(N)]
ansque = [0] * (K + 1)
cnt = 1
for j in range(M):
    for i in range(N):
        windows[i][0].append(cnt)
        windows[i][1].append(sum(windows[i][1]) + time[cnt - 1])
        cnt += 1
while cnt <= K:
    min = [0, windows[0][1][0]]
    for i in range(N):
        if min[1] > windows[i][1][0]:
            min[1] = windows[i][1][0]
            min[0] = i
    ansque[windows[min[0]][0][0]] = min[1]
    del windows[min[0]][0][0]
    del windows[min[0]][1][0]
    windows[min[0]][0].append(cnt)
    windows[min[0]][1].append(sum(windows[min[0]][1]) + time[cnt - 1])
    cnt += 1
for i in range(N):
    for j in range(M):
        ansque[windows[i][0][j]] = windows[i][1][j]
for i in q:
    if ansque[i] > 540:
        print('Sorry')
    else:
        print("%02d:%02d" % (8 + ansque[i] // 60,ansque[i] % 60))
"""
###############################################################################