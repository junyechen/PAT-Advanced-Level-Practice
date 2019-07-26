"""
To evaluate the performance of our first year CS majored students, we consider their grades of three courses only: C - C Programming Language, M - Mathematics (Calculus or Linear Algrbra), and E - English. At the mean time, we encourage students by emphasizing on their best ranks -- that is, among the four ranks with respect to the three courses and the average grade, we print the best rank for each student.

For example, The grades of C, M, E and A - Average of 4 students are given as the following:

StudentID  C  M  E  A
310101     98 85 88 90
310102     70 95 88 84
310103     82 87 94 88
310104     91 91 91 91

Then the best ranks for all the students are No.1 since the 1st one has done the best in C Programming Language, while the 2nd one in Mathematics, the 3rd one in English, and the last one in average.
Input Specification:

Each input file contains one test case. Each case starts with a line containing 2 numbers N and M (≤2000), which are the total number of students, and the number of students who would check their ranks, respectively. Then N lines follow, each contains a student ID which is a string of 6 digits, followed by the three integer grades (in the range of [0, 100]) of that student in the order of C, M and E. Then there are M lines, each containing a student ID.
Output Specification:

For each of the M students, print in one line the best rank for him/her, and the symbol of the corresponding rank, separated by a space.

The priorities of the ranking methods are ordered as A > C > M > E. Hence if there are two or more ways for a student to obtain the same best rank, output the one with the highest priority.

If a student is not on the grading list, simply output N/A.
Sample Input:

5 6
310101 98 85 88
310102 70 95 88
310103 82 87 94
310104 91 91 91
310105 85 90 90
310101
310102
310103
310104
310105
999999

Sample Output:

1 C
1 M
1 E
1 A
3 A
N/A
"""

###################################################
"""
问题：
1. 一开始做法，设立6位数数组，运行超时，所以下次要注意python桶排序的空间问题
2. 需注意若有排名重叠现象，则下一名次需加上上一名次人数-1，如1,2,2,3,4，则相应的排名为1,2,2,4,5
"""
###################################################

ID_grade = {}
A_grade = [0] * 301
C_grade = [0] * 101
M_grade = [0] * 101
E_grade = [0] * 101
N, M = [int(i) for i in input().split()]
for _ in range(N):
    temp = [int(i) for i in input().split()]
    ID_grade[temp[0]] = temp[1:4]
    C_grade[temp[1]] += 1
    M_grade[temp[2]] += 1
    E_grade[temp[3]] += 1
    A_grade[sum(temp[1:4])] += 1
rank = 1
for _ in range(100,-1,-1):
    if C_grade[_]!=0:
        temp = C_grade[_]
        C_grade[_] = rank
        rank += temp
rank = 1
for _ in range(100,-1,-1):
    if M_grade[_]!=0:
        temp = M_grade[_]
        M_grade[_] = rank
        rank += temp
rank = 1
for _ in range(100,-1,-1):
    if E_grade[_]!=0:
        temp = E_grade[_]
        E_grade[_] = rank
        rank += temp
rank = 1
for _ in range(300,-1,-1):
    if A_grade[_]!=0:
        temp = A_grade[_]
        A_grade[_] = rank
        rank += temp
for _ in range(M):
    temp = int(input())
    try:
        if ID_grade[temp]:
            C = C_grade[ID_grade[temp][0]]
            M = M_grade[ID_grade[temp][1]]
            E = E_grade[ID_grade[temp][2]]
            A = A_grade[sum(ID_grade[temp])]
            if A <= C and A <= M and A <= E:
                print(A,'A')
            elif C <= A and C <= M and C <= E:
                print(C,'C')
            elif M <= A and M <= C and M <= E:
                print(M,'M')
            else:
                print(E,'E')
    except:
        print(r"N/A")

##################################################
"""
ID_grade = {}
A_grade = [[] for i in range(301)]
C_grade = [[] for i in range(101)]
M_grade = [[] for i in range(101)]
E_grade = [[] for i in range(101)]
N, M = [int(i) for i in input().split()]
for _ in range(N):
    temp = [int(i) for i in input().split()]
    ID_grade[temp[0]] = temp[1:4]
    C_grade[temp[1]] = 1
    M_grade[temp[2]] = 1
    E_grade[temp[3]] = 1
    A_grade[sum(temp[1:4])] = 1
rank = 1
for _ in range(100,-1,-1):
    if C_grade[_]:
        C_grade[_] = rank
        rank += 1
rank = 1
for _ in range(100,-1,-1):
    if M_grade[_]:
        M_grade[_] = rank
        rank += 1
rank = 1
for _ in range(100,-1,-1):
    if E_grade[_]:
        E_grade[_] = rank
        rank += 1
rank = 1
for _ in range(300,-1,-1):
    if A_grade[_]:
        A_grade[_] = rank
        rank += 1
for _ in range(M):
    temp = int(input())
    try:
        if ID_grade[temp]:
            C = C_grade[ID_grade[temp][0]]
            M = M_grade[ID_grade[temp][1]]
            E = E_grade[ID_grade[temp][2]]
            A = A_grade[sum(ID_grade[temp])]
            if A <= C and A <= M and A <= E:
                print(A,'A')
            elif C <= A and C <= M and C <= E:
                print(C,'C')
            elif M <= A and M <= C and M <= E:
                print(M,'M')
            else:
                print(E,'E')
    except:
        print(r"N/A")
"""
##################################################

##################################################
"""
ID_grade = [[] for i in range(1000000)]
A_grade = [[] for i in range(301)]
C_grade = [[] for i in range(101)]
M_grade = [[] for i in range(101)]
E_grade = [[] for i in range(101)]
N, M = [int(i) for i in input().split()]
for _ in range(N):
    temp = [int(i) for i in input().split()]
    ID_grade[temp[0]] = temp[1:4]
    C_grade[temp[1]] = 1
    M_grade[temp[2]] = 1
    E_grade[temp[3]] = 1
    A_grade[sum(temp[1:4])] = 1
rank = 1
for _ in range(100,-1,-1):
    if C_grade[_]:
        C_grade[_] = rank
        rank += 1
rank = 1
for _ in range(100,-1,-1):
    if M_grade[_]:
        M_grade[_] = rank
        rank += 1
rank = 1
for _ in range(100,-1,-1):
    if E_grade[_]:
        E_grade[_] = rank
        rank += 1
rank = 1
for _ in range(300,-1,-1):
    if A_grade[_]:
        A_grade[_] = rank
        rank += 1
for _ in range(M):
    temp = int(input())
    if ID_grade[temp]:
        C = C_grade[ID_grade[temp][0]]
        M = M_grade[ID_grade[temp][1]]
        E = E_grade[ID_grade[temp][2]]
        A = A_grade[sum(ID_grade[temp])]
        if A <= C and A <= M and A <= E:
            print(A,'A')
        elif C <= A and C <= M and C <= E:
            print(C,'C')
        elif M <= A and M <= C and M <= E:
            print(M,'M')
        else:
            print(E,'E')
    else:
        print(r"N/A")
"""
#################################################