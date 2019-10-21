"""
Zhejiang University has 40000 students and provides 2500 courses. Now given the student name lists of all the courses, you are supposed to output the registered course list for each student who comes for a query.

Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers: N (≤40,000), the number of students who look for their course lists, and K (≤2,500), the total number of courses. Then the student name lists are given for the courses (numbered from 1 to K) in the following format: for each course i, first the course index i and the number of registered students N
​i
​​  (≤200) are given in a line. Then in the next line, N
​i
​​  student names are given. A student name consists of 3 capital English letters plus a one-digit number. Finally the last line contains the N names of students who come for a query. All the names and numbers in a line are separated by a space.

Output Specification:

For each test case, print your results in N lines. Each line corresponds to one student, in the following format: first print the student's name, then the total number of registered courses of that student, and finally the indices of the courses in increasing order. The query results must be printed in the same order as input. All the data in a line must be separated by a space, with no extra space at the end of the line.

Sample Input:

11 5
4 7
BOB5 DON2 FRA8 JAY9 KAT3 LOR6 ZOE1
1 4
ANN0 BOB5 JAY9 LOR6
2 7
ANN0 BOB5 FRA8 JAY9 JOE4 KAT3 LOR6
3 1
BOB5
5 9
AMY7 ANN0 BOB5 DON2 FRA8 JAY9 KAT3 LOR6 ZOE1
ZOE1 ANN0 BOB5 JOE4 JAY9 FRA8 DON2 AMY7 KAT3 LOR6 NON9
Sample Output:

ZOE1 2 4 5
ANN0 3 1 2 5
BOB5 5 1 2 3 4 5
JOE4 1 2
JAY9 4 1 2 4 5
FRA8 3 2 4 5
DON2 2 4 5
AMY7 1 5
KAT3 3 2 4 5
LOR6 4 1 2 4 5
NON9 0
"""


####################################################
"""
这题拿到手感觉思路非常简单，但是看题目的数据量估计又要超时
思路：建立以名字为关键词的字典，值为课程集合
一开始测试点1始终返回非零，而测试点5超时，经过努力后来发现：
    1. 测试点1返回非零：输入案例中，有课程号，但人数为0，下一行紧跟下一个课程的情况；加一个判断课程人数是否为0的条件就通过了
    2. 一开始是将输入的名字放于一个数组中，即：
        name = input().split()
        for name_ in name:
        然后尝试着将两句合并：
        for name in input().split():
        结果测试点5就通过了，虽然有450ms的运行时间

查看网上，对于C++用户，主要超时点为输入用scanf而不能用cin，另一个是用hash表，将学生名字转换成数字，可节省大量时间
不过既然python通过，就不考虑这劳什子鸟事
"""
####################################################


N, k = [int(_) for _ in input().split()]
name_course = {}
for _ in range(k):
    course, n = [int(_) for _ in input().split()]
    if n == 0:
        continue
    for name in input().split():
        if name in name_course:
            name_course[name].append(course)
        else:
            name_course[name] = [course]
for name in input().split():
    if name in name_course:
        name_course[name].sort()
        print(name, len(name_course[name]), ' '.join(list(map(str, name_course[name]))))
    else:
        print(name, 0)
