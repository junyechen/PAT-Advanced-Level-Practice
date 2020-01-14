"""
Zhejiang University has 8 campuses and a lot of gates. From each gate we can collect the in/out times and the plate numbers of the cars crossing the gate. Now with all the information available, you are supposed to tell, at any specific time point, the number of cars parking on campus, and at the end of the day find the cars that have parked for the longest time period.
Input Specification:

Each input file contains one test case. Each case starts with two positive integers N (≤10​4​​), the number of records, and K (≤8×10​4​​) the number of queries. Then N lines follow, each gives a record in the format:

plate_number hh:mm:ss status

where plate_number is a string of 7 English capital letters or 1-digit numbers; hh:mm:ss represents the time point in a day by hour:minute:second, with the earliest time being 00:00:00 and the latest 23:59:59; and status is either in or out.

Note that all times will be within a single day. Each in record is paired with the chronologically next record for the same car provided it is an out record. Any in records that are not paired with an out record are ignored, as are out records not paired with an in record. It is guaranteed that at least one car is well paired in the input, and no car is both in and out at the same moment. Times are recorded using a 24-hour clock.

Then K lines of queries follow, each gives a time point in the format hh:mm:ss. Note: the queries are given in ascending order of the times.
Output Specification:

For each query, output in a line the total number of cars parking on campus. The last line of output is supposed to give the plate number of the car that has parked for the longest time period, and the corresponding time length. If such a car is not unique, then output all of their plate numbers in a line in alphabetical order, separated by a space.

Sample Input:

16 7
JH007BD 18:00:01 in
ZD00001 11:30:08 out
DB8888A 13:00:00 out
ZA3Q625 23:59:50 out
ZA133CH 10:23:00 in
ZD00001 04:09:59 in
JH007BD 05:09:59 in
ZA3Q625 11:42:01 out
JH007BD 05:10:33 in
ZA3Q625 06:30:50 in
JH007BD 12:23:42 out
ZA3Q625 23:55:00 in
JH007BD 12:24:23 out
ZA133CH 17:11:22 out
JH007BD 18:07:01 out
DB8888A 06:30:50 in
05:10:00
06:30:50
11:00:00
12:23:42
14:00:00
18:00:00
23:59:00

Sample Output:

1
4
5
2
1
0
1
JH007BD ZD00001 07:20:09
"""

#######################################################
"""
得出停车数量状态，发现网上有巧妙的方法，即通过将每条记录单列，将in记录1，out记录-1，对于某个时间点之前的所有记录状态相加，即可得到该时间点的停车数量
    而不需要通过计算区间分布来判断停车数量！
    这样就可以使2个超时变为1个超时
"""
#######################################################

n, k = map(int, input().split())
record = {}
for _ in range(n):
    info = input().split()
    if info[0] not in record:
        record[info[0]] = []
    time = list(map(int, info[1].split(':')))
    time = time[0] * 60 * 60 + time[1] * 60 + time[2]
    record[info[0]].append([time, info[2]])
clean_record = []
longest_time, longest_time_ID = 0, []
for ID in record:
    record[ID].sort(key=lambda x: x[0])
    i = 0
    duration_time = 0
    while i < len(record[ID]) - 1:
        if record[ID][i][1] == 'in' and record[ID][i + 1][1] == 'out':
            clean_record.append([record[ID][i][0], 1])
            clean_record.append([record[ID][i+1][0], -1])
            duration_time += clean_record[-1][0] - clean_record[-2][0]
            i += 2
        else:
            i += 1
    if duration_time > longest_time:
        longest_time = duration_time
        longest_time_ID = [ID]
    elif duration_time == longest_time:
        longest_time_ID.append(ID)
clean_record.sort(key=lambda x: x[0])
count, check_order = 0, 0
for _ in range(k):
    time = list(map(int, input().split(':')))
    time = time[0] * 60 * 60 + time[1] * 60 + time[2]
    while check_order < len(clean_record) and clean_record[check_order][0] <= time:
        count += clean_record[check_order][1]
        check_order += 1
    print(count)
print(' '.join(sorted(longest_time_ID)), '%02d:%02d:%02d' % (longest_time // 60 // 60, longest_time // 60 % 60, longest_time % 60))

'''
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

// 每一条记录的数据结构，当记录是进来，flag=1,反之，flag=-1
struct Record {
    string id;
    int time, flag;

    // 重载小于号以便排序
    bool operator<(const Record &b) {
        if (id != b.id)
            return id < b.id;
        return time < b.time;
    }
};

bool cmp_by_time(Record *a, Record *b) {
    return a->time < b->time;
}

int main() {
    int n, k, maxtime = -1;
    cin >> n >> k;

    // 读取记录
    vector<Record> records(n);
    for (int i = 0; i < n; i++) {
        string status;
        cin >> records[i].id;
        int h, m, s;
        scanf("%d:%d:%d", &h, &m, &s);
        records[i].time = h * 3600 + m * 60 + s;
        cin >> status;
        records[i].flag = status == "in" ? 1 : -1;
    }
    // 按照id优先，时间点第二的升序原则排序所有记录
    sort(records.begin(), records.end());

    // 清理并整理出干净的records，同时计算出最大停车时间以及车牌号数组
    // 题目意思是，同一辆车，按时间排序，必须前后两个record正好是一进一出，才统计进去。
    vector<Record *> clean_records;
    int park_time = 0;
    string pre = records[0].id;
    vector<string> ans;
    for (int i = 0; i < n - 1; i++) {
        if (records[i].id == records[i + 1].id && records[i].flag == 1 && records[i + 1].flag == -1) {
            clean_records.push_back(&records[i]);
            clean_records.push_back(&records[i + 1]);
            if (records[i].id != pre){
                if (park_time > maxtime){
                    maxtime = park_time;
                    ans.clear();
                    ans.emplace_back(pre);
                }else if (park_time == maxtime)
                    ans.emplace_back(pre);
                park_time = records[i + 1].time - records[i].time;
                pre = records[i].id;
            }else
                park_time += (records[i + 1].time - records[i].time);
        }
    }

    // 刚刚的对比会忽略最晚的车，最晚的车也要比一比
    if (park_time > maxtime){
        maxtime = park_time;
        ans.clear();
        ans.emplace_back(pre);
    }else if (park_time == maxtime)
        ans.emplace_back(pre);

    //将所有有效记录按时间排列
    sort(clean_records.begin(), clean_records.end(), cmp_by_time);

    // 执行查询任务,因为查询时间是递增的，所以每次查询从上次的时间下标之后就可以了
    int count = 0;
    int time_index = 0;
    for (int i = 0; i < k; i++) {
        int h, m, s;
        scanf("%d:%d:%d", &h, &m, &s);
        while(time_index<clean_records.size() && clean_records[time_index]->time <= h * 3600 + m * 60 + s){
            count += clean_records[time_index]->flag;
            time_index ++;
        }
        printf("%d\n", count);
    }

    // 打印所有的最大停车时间的车牌号
    for (auto &it:ans)
        cout<<it<<" ";
    printf("%02d:%02d:%02d", maxtime / 3600, (maxtime % 3600) / 60, maxtime % 60);
    return 0;
}
'''

'''
n, k = map(int, input().split())
record = {}
for _ in range(n):
    info = input().split()
    if info[0] not in record:
        record[info[0]] = []
    time = list(map(int, info[1].split(':')))
    time = time[0] * 60 * 60 + time[1] * 60 + time[2]
    record[info[0]].append([time, info[2]])
clean_record = []
longest_time, longest_time_ID = 0, []
for ID in record:
    record[ID].sort(key=lambda x: x[0])
    i = 0
    duration_time = 0
    while i < len(record[ID]) - 1:
        if record[ID][i][1] == 'in' and record[ID][i + 1][1] == 'out':
            clean_record.append([ID, record[ID][i][0], record[ID][i + 1][0]])
            duration_time += clean_record[-1][2] - clean_record[-1][1]
            i += 2
        else:
            i += 1
    if duration_time > longest_time:
        longest_time = duration_time
        longest_time_ID = [ID]
    elif duration_time == longest_time:
        longest_time_ID.append(ID)
clean_record.sort(key=lambda x: x[1])
que = []
check = 0
for _ in range(k):
    time = list(map(int, input().split(':')))
    time = time[0] * 60 * 60 + time[1] * 60 + time[2]
    que_remover = []
    for check_order in que:
        if clean_record[check_order][2] <= time:
            que_remover.append(check_order)
    for ele in que_remover:
        que.remove(ele)
    while check < len(clean_record) and clean_record[check][2] < time:
        check += 1
    while check < len(clean_record) and clean_record[check][1] <= time <= clean_record[check][2]:
        que.append(check)
        check += 1
    print(len(que))
print(' '.join(sorted(longest_time_ID)),
      '%02d:%02d:%02d' % (longest_time // 60 // 60, longest_time // 60 % 60, longest_time % 60))
'''
