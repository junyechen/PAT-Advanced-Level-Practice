"""
A long-distance telephone company charges its customers by the following rules:

Making a long-distance call costs a certain amount per minute, depending on the time of day when the call is made. When a customer starts connecting a long-distance call, the time will be recorded, and so will be the time when the customer hangs up the phone. Every calendar month, a bill is sent to the customer for each minute called (at a rate determined by the time of day). Your job is to prepare the bills for each month, given a set of phone call records.

Input Specification:

Each input file contains one test case. Each case has two parts: the rate structure, and the phone call records.

The rate structure consists of a line with 24 non-negative integers denoting the toll (cents/minute) from 00:00 - 01:00, the toll from 01:00 - 02:00, and so on for each hour in the day.

The next line contains a positive number N (≤1000), followed by N lines of records. Each phone call record consists of the name of the customer (string of up to 20 characters without space), the time and date (mm:dd:hh:mm), and the word on-line or off-line.

For each test case, all dates will be within a single month. Each on-line record is paired with the chronologically next record for the same customer provided it is an off-line record. Any on-line records that are not paired with an off-line record are ignored, as are off-line records not paired with an on-line record. It is guaranteed that at least one call is well paired in the input. You may assume that no two records for the same customer have the same time. Times are recorded using a 24-hour clock.

Output Specification:

For each test case, you must print a phone bill for each customer.

Bills must be printed in alphabetical order of customers' names. For each customer, first print in a line the name of the customer and the month of the bill in the format shown by the sample. Then for each time period of a call, print in one line the beginning and ending time and date (dd:hh:mm), the lasting time (in minute) and the charge of the call. The calls must be listed in chronological order. Finally, print the total charge for the month in the format shown by the sample.

Sample Input:

10 10 10 10 10 10 20 20 20 15 15 15 15 15 15 15 20 30 20 15 15 10 10 10
10
CYLL 01:01:06:01 on-line
CYLL 01:28:16:05 off-line
CYJJ 01:01:07:00 off-line
CYLL 01:01:08:03 off-line
CYJJ 01:01:05:59 on-line
aaa 01:01:01:03 on-line
aaa 01:02:00:01 on-line
CYLL 01:28:15:41 on-line
aaa 01:05:02:24 on-line
aaa 01:04:23:59 off-line
Sample Output:

CYJJ 01
01:05:59 01:07:00 61 $12.10
Total amount: $12.10
CYLL 01
01:06:01 01:08:03 122 $24.40
28:15:41 28:16:05 24 $3.85
Total amount: $28.25
aaa 01
02:00:01 04:23:59 4318 $638.80
Total amount: $638.80
"""

toll = [int(_) for _ in input().split()]
day_toll = sum(toll) * 60 / 100
n = int(input())
name = []
time = {}
for _ in range(n):
    name_, time_, state_ = input().split()
    name.append(name_)
    if name_ in time:
        time[name_].append(time_ + ' ' + state_)
    else:
        time[name_] = [time_ + ' ' + state_]
name = sorted(list(set(name)))
for name_ in name:
    time_state = time[name_]
    time_state.sort()
    i = 0
    amount = 0
    output_ = []
    while i < len(time_state) - 1:
        if time_state[i][13] == 'n':
            if time_state[i + 1][13] == 'f':
                month = time_state[i][0:2]
                time1, time2 = time_state[i][3:11], time_state[i + 1][3:11]
                day1, day2 = int(time1[0:2]), int(time2[0:2])
                hour1, hour2 = int(time1[3:5]), int(time2[3:5])
                min1, min2 = int(time1[6:8]), int(time2[6:8])
                time_span = (day2 - day1) * 1440 + (hour2 - hour1) * 60 + (min2 - min1)
                amount_ = (day2 - day1) * day_toll + (sum(toll[:hour2]) - sum(toll[:hour1])) * 60 / 100 + toll[
                    hour2] * min2 / 100 - toll[hour1] * min1 / 100
                output_.append(time1 + ' ' + time2 + ' ' + str(time_span) + ' ' + "$%0.2f" % amount_)
                amount += amount_
                i += 2
            else:
                i += 1
        else:
            i += 1
    if amount != 0:
        print(name_, month)
        for _ in output_:
            print(_)
        print("Total amount: $%0.2f" % amount)
