"""
A table tennis club has N tables available to the public. The tables are numbered from 1 to N. For any pair of players, if there are some tables open when they arrive, they will be assigned to the available table with the smallest number. If all the tables are occupied, they will have to wait in a queue. It is assumed that every pair of players can play for at most 2 hours.

Your job is to count for everyone in queue their waiting time, and for each table the number of players it has served for the day.

One thing that makes this procedure a bit complicated is that the club reserves some tables for their VIP members. When a VIP table is open, the first VIP pair in the queue will have the priviledge to take it. However, if there is no VIP in the queue, the next pair of players can take it. On the other hand, if when it is the turn of a VIP pair, yet no VIP table is available, they can be assigned as any ordinary players.

Input Specification:

Each input file contains one test case. For each case, the first line contains an integer N (≤10000) - the total number of pairs of players. Then N lines follow, each contains 2 times and a VIP tag: HH:MM:SS - the arriving time, P - the playing time in minutes of a pair of players, and tag - which is 1 if they hold a VIP card, or 0 if not. It is guaranteed that the arriving time is between 08:00:00 and 21:00:00 while the club is open. It is assumed that no two customers arrives at the same time. Following the players' info, there are 2 positive integers: K (≤100) - the number of tables, and M (< K) - the number of VIP tables. The last line contains M table numbers.

Output Specification:

For each test case, first print the arriving time, serving time and the waiting time for each pair of players in the format shown by the sample. Then print in a line the number of players served by each table. Notice that the output must be listed in chronological order of the serving time. The waiting time must be rounded up to an integer minute(s). If one cannot get a table before the closing time, their information must NOT be printed.

Sample Input:

9
20:52:00 10 0
08:00:00 20 0
08:02:00 30 0
20:51:00 10 0
08:10:00 5 0
08:12:00 10 1
20:50:00 10 0
08:01:30 15 1
20:53:00 10 1
3 1
2
Sample Output:

08:00:00 08:00:00 0
08:01:30 08:01:30 0
08:02:00 08:02:00 0
08:12:00 08:16:30 5
08:10:00 08:20:00 10
20:50:00 20:50:00 0
20:51:00 20:51:00 0
20:52:00 20:52:00 0
3 3 2
"""


###################################################################################################
"""
这题做的真的十分崩溃，在考试那么短的时间内，我肯定完不成，而现在在非考场，我也没法做到完全正确。
最下面一版，在PAT上是错1个测试点3，然后测试点8超时（python的常见问题），但在牛客网上全错
改正后，下面这个版本是完全通过牛客网，但是在PAT上则是测试点0、7非零返回，测试点8超时
这个模拟的题目实在非常耗费精力，暂且使用他人代码AC过，留以后C++二刷
"""
###################################################################################################


def print_(arrive_time, serve_time, wait_time):
    print("%02d:%02d:%02d %02d:%02d:%02d %d" % (
        arrive_time // 3600 + 8, arrive_time // 60 % 60, arrive_time % 60, serve_time // 3600 + 8,
        serve_time // 60 % 60,
        serve_time % 60, wait_time))


n = int(input())
line = []
for i in range(n):
    arrive, play, tag = input().split()
    arrive = (int(arrive[0:2]) - 8) * 3600 + int(arrive[3:5]) * 60 + int(arrive[6:8])
    if arrive >= 13 * 3600 or arrive < 0:
        continue
    play = int(play)
    if play > 120:
        play = 120
    line.append([arrive, play * 60, tag])
line.sort(key=lambda x: x[0])
k, m = [int(_) for _ in input().split()]
vip_table_no = [int(_) for _ in input().split()]
vip_table_no.sort()
table = [0] * k
table_wait = [0] * k
table_serve = [0] * k
while line:
    flag = False
    if line[0][2] == '1':
        for i in vip_table_no:
            if line[0][0] >= table[i - 1]:
                table[i - 1] = line[0][0] + line[0][1]
                table_serve[i - 1] += 1
                print_(line[0][0], line[0][0], 0)
                line.pop(0)
                flag = True
                break
    if flag:
        continue
    for i in range(k):
        if line[0][0] >= table[i]:
            table[i] = line[0][0] + line[0][1]
            table_serve[i] += 1
            print_(line[0][0], line[0][0], 0)
            line.pop(0)
            flag = True
            break
    if flag:
        continue
    min_end_time = table[0]
    min_table = [0]
    for i in range(1, k):
        if table[i] < min_end_time:
            min_end_time = table[i]
            min_table = [i]
        elif table[i] == min_end_time:
            min_table.append(i)
    if min_end_time >= 13 * 3600:
        break
    wait_que = []
    i = 0
    vip = []
    try:
        while line[i][0] <= min_end_time:
            wait_que.append(line[i])
            if line[i][2] == '1':
                vip.append(i)
            i += 1
    except:
        pass
    if vip:
        vip_table = []
        for i in min_table:
            if i + 1 in vip_table_no:
                vip_table.append(i)
        if len(vip) >= len(vip_table):
            while vip_table:
                wait = int((table[vip_table[0]] - wait_que[vip[0]][0]) / 60 + 0.5)
                table_wait[vip_table[0]] += wait
                print_(wait_que[vip[0]][0], table[vip_table[0]], wait)
                table[vip_table[0]] += wait_que[vip[0]][1]
                table_serve[vip_table[0]] += 1
                wait_que.pop(vip[0])
                line.pop(vip[0])
                vip.pop(0)
                min_table.pop(vip_table[0])
                vip_table.pop(0)
        else:
            while vip:
                wait = int((table[vip_table[0]] - wait_que[vip[0]][0]) / 60 + 0.5)
                table_wait[vip_table[0]] += wait
                print_(wait_que[vip[0]][0], table[vip_table[0]], wait)
                table[vip_table[0]] += wait_que[vip[0]][1]
                table_serve[vip_table[0]] += 1
                wait_que.pop(vip[0])
                line.pop(vip[0])
                vip.pop(0)
                min_table.pop(vip_table[0])
                vip_table.pop(0)
    for i in min_table:
        if wait_que:
            pass
        else:
            break
        wait = int((table[i] - wait_que[0][0]) / 60 + 0.5)
        table_wait[i] += wait
        print_(wait_que[0][0], table[i], wait)
        table[i] += wait_que[0][1]
        table_serve[i] += 1
        wait_que.pop(0)
        line.pop(0)
print(" ".join(list(map(str, table_serve))))


###################################################################################
"""
def print_(arrive_time, serve_time, wait_time):
    print("%02d:%02d:%02d %02d:%02d:%02d %d" % (
    arrive_time // 3600 + 8, arrive_time // 60 % 60, arrive_time % 60, serve_time // 3600 + 8, serve_time // 60 % 60,
    serve_time % 60, wait_time))


n = int(input())
line = []
for i in range(n):
    arrive, play, tag = input().split()
    arrive = (int(arrive[0:2]) - 8) * 3600 + int(arrive[3:5]) * 60 + int(arrive[6:8])
    play = int(play)
    if play > 120:
        play = 120
    line.append([arrive, play * 60, tag])
line.sort(key=lambda x: x[0])
k, m = [int(_) for _ in input().split()]
vip_table_no = [int(_) for _ in input().split()]
table = [0] * k
table_wait = [0] * k
table_serve = [0] * k
while line:
    flag = False
    if line[0][2] == '1':
        for i in vip_table_no:
            if line[0][0] >= table[i - 1]:
                table[i - 1] = line[0][0] + line[0][1]
                table_serve[i - 1] += 1
                print_(line[0][0], line[0][0], 0)
                line.pop(0)
                flag = True
                break
    if flag:
        continue
    for i in range(k):
        if line[0][0] >= table[i]:
            table[i] = line[0][0] + line[0][1]
            table_serve[i] += 1
            print_(line[0][0], line[0][0], 0)
            line.pop(0)
            flag = True
            break
    if flag:
        continue
    min_end_time = table[0]
    min_table = [0]
    for i in range(1, k):
        if table[i] < min_end_time:
            min_end_time = table[i]
            min_table = [i]
        elif table[i] == min_end_time:
            min_table.append(i)
    if min_end_time >= 13*3600:
        break
    wait_que = []
    i = 0
    try:
        while line[i][0] < min_end_time:
            wait_que.append(line[i])
            i += 1
    except:
        pass
    for i in min_table:
        flag = False
        if i + 1 in vip_table_no:
            for j in range(len(wait_que)):
                if wait_que[j][2] == '1':
                    wait = int((table[i] - wait_que[j][0]) / 60 + 0.5)
                    table_wait[i] += wait
                    print_(wait_que[j][0], table[i], wait)
                    table[i] += wait_que[j][1]
                    table_serve[i] += 1
                    wait_que.pop(j)
                    line.pop(j)
                    flag = True
                    break
        if flag:
            continue
        else:
            wait = int((table[i] - wait_que[0][0]) / 60 + 0.5)
            table_wait[i] += wait
            print_(wait_que[0][0], table[i], wait)
            table[i] += wait_que[0][1]
            table_serve[i] += 1
            wait_que.pop(0)
            line.pop(0)
print(" ".join(list(map(str, table_serve))))
"""
###################################################################################