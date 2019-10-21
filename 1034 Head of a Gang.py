"""
One way that the police finds the head of a gang is to check people's phone calls. If there is a phone call between A and B, we say that A and B is related. The weight of a relation is defined to be the total time length of all the phone calls made between the two persons. A "Gang" is a cluster of more than 2 persons who are related to each other with total relation weight being greater than a given threshold K. In each gang, the one with maximum total weight is the head. Now given a list of phone calls, you are supposed to find the gangs and the heads.

Input Specification:

Each input file contains one test case. For each case, the first line contains two positive numbers N and K (both less than or equal to 1000), the number of phone calls and the weight threthold, respectively. Then N lines follow, each in the following format:

Name1 Name2 Time
where Name1 and Name2 are the names of people at the two ends of the call, and Time is the length of the call. A name is a string of three capital letters chosen from A-Z. A time length is a positive integer which is no more than 1000 minutes.

Output Specification:

For each test case, first print in a line the total number of gangs. Then for each gang, print in a line the name of the head and the total number of the members. It is guaranteed that the head is unique for each gang. The output must be sorted according to the alphabetical order of the names of the heads.

Sample Input 1:

8 59
AAA BBB 10
BBB AAA 20
AAA CCC 40
DDD EEE 5
EEE DDD 70
FFF GGG 30
GGG HHH 20
HHH FFF 10
Sample Output 1:

2
AAA 3
GGG 3
Sample Input 2:

8 70
AAA BBB 10
BBB AAA 20
AAA CCC 40
DDD EEE 5
EEE DDD 70
FFF GGG 30
GGG HHH 20
HHH FFF 10
Sample Output 2:

0
"""


####################################
"""
本题思路明确，为深度优先遍历，得到不同连通图，确定图的所有边的权重是否超过阈值k，以及根据边的权重确定图的最大权重顶点
本题新学习了几种方法
    1. 可以逐层建立字典，就解决了深度优先搜索时图的遍历困难的问题
    2. 可在函数中用global声明变量，以引用主程序中的全局变量，不再需要通过函数的参数中设立list变量避免递归回溯时值的丢失
"""
####################################


def dfs(start):
    global relation, visit, gang
    visit[start] = 0
    gang.append(start)
    for end in relation[start]:
        if visit[end] == 1:
            dfs(end)


n, k = [int(_) for _ in input().split()]
relation, visit = {}, {}
for _ in range(n):
    name1, name2, time = input().split()
    time = int(time)
    visit[name1], visit[name2] = 1, 1
    if name1 in relation:
        if name2 in relation[name1]:
            relation[name1][name2] += time
        else:
            relation[name1][name2] = time
    else:
        relation[name1] = {}
        relation[name1][name2] = time
    if name2 in relation:
        if name1 in relation[name2]:
            relation[name2][name1] += time
        else:
            relation[name2][name1] = time
    else:
        relation[name2] = {}
        relation[name2][name1] = time
gang_num = 0
gang_head_num = []
for i in visit:
    if visit[i] == 1:
        gang = []
        dfs(i)
        if len(gang) > 2:
            weight = {}
            weight_sum = 0
            for gang_ in gang:
                for name in relation[gang_]:
                    w = relation[gang_][name]
                    if gang_ in weight:
                        weight[gang_] += w
                    else:
                        weight[gang_] = w
                    weight_sum += w
            if weight_sum/2 > k:
                gang_num += 1
                head = gang[0]
                for gang_ in gang:
                    if weight[head] < weight[gang_]:
                        head = gang_
                gang_head_num.append([head, len(gang)])
print(gang_num)
if gang_num == 0:
    pass
else:
    gang_head_num.sort(key=lambda x: x[0])
    for item in gang_head_num:
        print(item[0], item[1])

##########################################################
"""
def dfs(start, gang_num_, gang_, weight_):
    tag[start] = 0
    gang_num_[0] += 1
    gang_.append(start)
    for end in name:
        try:
            w = relation[(start, end)]
            weight_[0] += w
            weight[start] += w
            weight[end] += w
            if tag[end] == 1:
                dfs(end, gang_num_, gang_, weight_)
        except:
            pass


n, k = [int(_) for _ in input().split()]
relation = {}
name = []
for _ in range(n):
    temp = input().split()
    name.append(temp[0])
    name.append(temp[1])
    if (temp[0], temp[1]) in relation:
        relation[(temp[0], temp[1])] += int(temp[2])
        relation[(temp[1], temp[0])] += int(temp[2])
    else:
        relation[(temp[0], temp[1])] = int(temp[2])
        relation[(temp[1], temp[0])] = int(temp[2])
name = list(set(name))
tag, weight = {}, {}
for name_ in name:
    tag[name_] = 1
    weight[name_] = 0
gang_num = 0
gang_num_ = [0]
gang = []
head = []
weight_ = [0]
for name_ in name:
    if tag[name_] == 1:
        dfs(name_, gang_num_, gang, weight_)
        if gang_num_[0] > 2:
            head_ = gang[0]
            if weight_[0]/2 > k:
                for gang_ in gang:
                    if weight[head_] < weight[gang_]:
                        head_ = gang_
                gang_num += 1
                head.append([head_, gang_num_[0]])
        gang_num_[0] = 0
        gang = []
        weight_ = [0]
if gang_num == 0:
    print(0)
else:
    print(gang_num)
    head.sort(key=lambda x: x[0])
    for head_ in head:
        print(head_[0], head_[1])
"""
##########################################################
