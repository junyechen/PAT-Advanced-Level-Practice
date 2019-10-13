"""
Suppose a bank has K windows open for service. There is a yellow line in front of the windows which devides the waiting area into two parts. All the customers have to wait in line behind the yellow line, until it is his/her turn to be served and there is a window available. It is assumed that no window can be occupied by a single customer for more than 1 hour.

Now given the arriving time T and the processing time P of each customer, you are supposed to tell the average waiting time of all the customers.

Input Specification:

Each input file contains one test case. For each case, the first line contains 2 numbers: N (≤10
​4
​​ ) - the total number of customers, and K (≤100) - the number of windows. Then N lines follow, each contains 2 times: HH:MM:SS - the arriving time, and P - the processing time in minutes of a customer. Here HH is in the range [00, 23], MM and SS are both in [00, 59]. It is assumed that no two customers arrives at the same time.

Notice that the bank opens from 08:00 to 17:00. Anyone arrives early will have to wait in line till 08:00, and anyone comes too late (at or after 17:00:01) will not be served nor counted into the average.

Output Specification:

For each test case, print in one line the average waiting time of all the customers, in minutes and accurate up to 1 decimal place.

Sample Input:

7 3
07:55:00 16
17:00:01 2
07:59:59 15
08:01:00 60
08:00:00 30
08:00:02 2
08:03:00 10
Sample Output:

8.2
"""

###############################################################################
"""
本题坑点在于：如果在17点或之前到达，即使最后办理时间超过17点，仍会给该顾客办理业务（测试点5）
"""
###############################################################################


def trans(time):
    return (int(time[0:2]) - 8) * 3600 + int(time[3:5]) * 60 + int(time[6:8])


N, K = (int(_) for _ in input().split())
rec = []
for _ in range(N):
    temp = input().split()
    arr = trans(temp[0])
    deal = int(temp[1])*60
    rec.append([arr, deal])
rec = sorted(rec, key=lambda x: x[0])
end = [0] * K
time_wait, people = 0, 0
for i in rec:
    end.sort()
    if i[0] < end[0]:
        time_wait += end[0] - i[0]
        if i[1] > 3600:
            end[0] += 3600
        else:
            end[0] += i[1]
        people += 1
    elif i[0] == end[0]:
        if i[1] > 3600:
            end[0] += 3600
        else:
            end[0] += i[1]
        people += 1
    else:
        if i[0] > 9 * 3600:
            break
        if i[1] > 3600:
            end[0] = i[0] + 3600
        else:
            end[0] = i[0] + i[1]
        people += 1
print("%0.1f" % (time_wait / people / 60))
