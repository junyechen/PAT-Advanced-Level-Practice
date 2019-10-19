"""
Excel can sort records according to any column. Now you are supposed to imitate this function.

Input Specification:

Each input file contains one test case. For each case, the first line contains two integers N (≤10
​5
​​ ) and C, where N is the number of records and C is the column that you are supposed to sort the records with. Then N lines follow, each contains a record of a student. A student's record consists of his or her distinct ID (a 6-digit number), name (a string with no more than 8 characters without space), and grade (an integer between 0 and 100, inclusive).

Output Specification:

For each test case, output the sorting result in N lines. That is, if C = 1 then the records must be sorted in increasing order according to ID's; if C = 2 then the records must be sorted in non-decreasing order according to names; and if C = 3 then the records must be sorted in non-decreasing order according to grades. If there are several students who have the same name or grade, they must be sorted according to their ID's in increasing order.

Sample Input 1:

3 1
000007 James 85
000010 Amy 90
000001 Zoe 60
Sample Output 1:

000001 Zoe 60
000007 James 85
000010 Amy 90
Sample Input 2:

4 2
000007 James 85
000010 Amy 90
000001 Zoe 60
000002 James 98
Sample Output 2:

000010 Amy 90
000002 James 98
000007 James 85
000001 Zoe 60
Sample Input 3:

4 3
000007 James 85
000010 Amy 90
000001 Zoe 60
000002 James 90
Sample Output 3:

000001 Zoe 60
000007 James 85
000002 James 90
000010 Amy 90
"""


####################################################
"""
本题非常简答，但老生常谈地遇到了python运行超时问题，经过网上指点，最后一个测试点数据量太大，但却是用学号进行排序的，而input().split()函数占据了大量的运行时间，故对于学号，可直接进行排序，无需切片，这样可节省大量时间
"""
####################################################


N, C = [int(_) for _ in input().split()]
record = []
for _ in range(N):
    record.append(input())
if C == 1:
    record.sort()
    for _ in range(N):
        print(record[_])
else:
    for _ in range(N):
        record_ = record[_].split()
        record_[2] = int(record_[2])
        record[_] = record_
    if C == 2:
        record.sort(key=lambda x: (x[1], x[0]))
    else:
        record.sort(key=lambda x: (x[2], x[0]))
    for _ in range(N):
        print(' '.join(list(map(str, record[_]))))


####################################################
"""
N, C = [int(_) for _ in input().split()]
record = []
for _ in range(N):
    record_ = input().split()
    record_[2] = int(record_[2])
    record.append(record_)
if C == 1:
    record.sort(key=lambda x: x[0])
elif C == 2:
    record.sort(key=lambda x: (x[1], x[0]))
else:
    record.sort(key=lambda x: (x[2], x[0]))
for _ in range(N):
    print(' '.join(list(map(str, record[_]))))
"""
####################################################
