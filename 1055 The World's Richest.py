"""
Forbes magazine publishes every year its list of billionaires based on the annual ranking of the world's wealthiest people. Now you are supposed to simulate this job, but concentrate only on the people in a certain range of ages. That is, given the net worths of N people, you must find the M richest people in a given range of their ages.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers: N (≤10​5​​) - the total number of people, and K (≤10​3​​) - the number of queries. Then N lines follow, each contains the name (string of no more than 8 characters without space), age (integer in (0, 200]), and the net worth (integer in [−10​6​​,10​6​​]) of a person. Finally there are K lines of queries, each contains three positive integers: M (≤100) - the maximum number of outputs, and [Amin, Amax] which are the range of ages. All the numbers in a line are separated by a space.
Output Specification:

For each query, first print in a line Case #X: where X is the query number starting from 1. Then output the M richest people with their ages in the range [Amin, Amax]. Each person's information occupies a line, in the format

Name Age Net_Worth

The outputs must be in non-increasing order of the net worths. In case there are equal worths, it must be in non-decreasing order of the ages. If both worths and ages are the same, then the output must be in non-decreasing alphabetical order of the names. It is guaranteed that there is no two persons share all the same of the three pieces of information. In case no one is found, output None.
Sample Input:

12 4
Zoe_Bill 35 2333
Bob_Volk 24 5888
Anny_Cin 95 999999
Williams 30 -22
Cindy 76 76000
Alice 18 88888
Joe_Mike 32 3222
Michael 5 300000
Rosemary 40 5888
Dobby 24 5888
Billy 24 5888
Nobody 5 0
4 15 45
4 30 35
4 5 95
1 45 50

Sample Output:

Case #1:
Alice 18 88888
Billy 24 5888
Bob_Volk 24 5888
Dobby 24 5888
Case #2:
Joe_Mike 32 3222
Zoe_Bill 35 2333
Williams 30 -22
Case #3:
Anny_Cin 95 999999
Michael 5 300000
Alice 18 88888
Cindy 76 76000
Case #4:
None
"""

######################################################
"""
测试点1、2超时
这题在落实时，就明显地预感到python会超时，果不其然，用网上AC的C++代码，测试点1用时190ms，测试点2用时56ms
python这货应该是没法优化了
    优化的方式为对所有数据进行排序后，再建立以年龄为单位的列表，存储某个年龄下的人在总表中的排名
"""
######################################################
n, k = map(int, input().split())
lis = []
for _ in range(n):
    name, age, net_worth = input().split()
    age = int(age)
    net_worth = int(net_worth)
    lis.append([name, age, net_worth])
lis.sort(key=lambda x: (-x[2], x[1], x[0]))
lis_age = [[] for _ in range(201)]
for i in range(len(lis)):
    lis_age[lis[i][1]].append(i)
for i in range(k):
    m, age_min, age_max = map(int, input().split())
    print("Case #%d:" % (i+1))
    temp = []
    for j in range(age_min, age_max+1):
        temp += lis_age[j]
    if len(temp) == 0:
        print("None")
    temp.sort()
    p = 0
    for j in temp:
        print(lis[j][0], lis[j][1], lis[j][2])
        p += 1
        if p == m:
            break

"""
n, k = map(int, input().split())
lis = []
for _ in range(n):
    name, age, net_worth = input().split()
    age = int(age)
    net_worth = int(net_worth)
    lis.append([name, age, net_worth])
lis.sort(key=lambda x: (-x[2], x[1], x[0]))
for i in range(k):
    m, age_min, age_max = map(int, input().split())
    j, p = 0, 0
    print("Case #%d:" % (i+1))
    while j < len(lis) and p < m:
        if age_min <= lis[j][1] <= age_max:
            print(lis[j][0], lis[j][1], lis[j][2])
            p += 1
        j += 1
    if p == 0:
        print("None")
"""
