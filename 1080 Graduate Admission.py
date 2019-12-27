"""
It is said that in 2011, there are about 100 graduate schools ready to proceed over 40,000 applications in Zhejiang Province. It would help a lot if you could write a program to automate the admission procedure.

Each applicant will have to provide two grades: the national entrance exam grade G​E​​, and the interview grade G​I​​. The final grade of an applicant is (G​E​​+G​I​​)/2. The admission rules are:

    The applicants are ranked according to their final grades, and will be admitted one by one from the top of the rank list.

    If there is a tied final grade, the applicants will be ranked according to their national entrance exam grade G​E​​. If still tied, their ranks must be the same.

    Each applicant may have K choices and the admission will be done according to his/her choices: if according to the rank list, it is one's turn to be admitted; and if the quota of one's most preferred shcool is not exceeded, then one will be admitted to this school, or one's other choices will be considered one by one in order. If one gets rejected by all of preferred schools, then this unfortunate applicant will be rejected.

    If there is a tied rank, and if the corresponding applicants are applying to the same school, then that school must admit all the applicants with the same rank, even if its quota will be exceeded.

Input Specification:

Each input file contains one test case.

Each case starts with a line containing three positive integers: N (≤40,000), the total number of applicants; M (≤100), the total number of graduate schools; and K (≤5), the number of choices an applicant may have.

In the next line, separated by a space, there are M positive integers. The i-th integer is the quota of the i-th graduate school respectively.

Then N lines follow, each contains 2+K integers separated by a space. The first 2 integers are the applicant's G​E​​ and G​I​​, respectively. The next K integers represent the preferred schools. For the sake of simplicity, we assume that the schools are numbered from 0 to M−1, and the applicants are numbered from 0 to N−1.
Output Specification:

For each test case you should output the admission results for all the graduate schools. The results of each school must occupy a line, which contains the applicants' numbers that school admits. The numbers must be in increasing order and be separated by a space. There must be no extra space at the end of each line. If no applicant is admitted by a school, you must output an empty line correspondingly.
Sample Input:

11 6 3
2 1 2 2 2 3
100 100 0 1 2
60 60 2 3 5
100 90 0 3 4
90 100 1 2 0
90 90 5 1 3
80 90 1 0 2
80 80 0 1 2
80 80 0 1 2
80 70 1 3 2
70 80 1 2 3
100 100 0 2 4

Sample Output:

0 10
3
5 6 7
2 8

1 4
"""

##########################################################################
"""
本题在一开始对应志愿时想复杂，看了别人的代码，只要比较进入志愿队列的最后一个就可以，而无需对相同分数划立同名次队列。

本题利用python重复测试多次后，所有都能通过，最长测试点为220ms，但大多时候是不能通过的
"""
##########################################################################

students, schools, choices = map(int, input().split())
school_quota = list(map(int, input().split()))
student_application, school_application = [], [[] for _ in range(schools)]
for i in range(students):
    student_application.append([i]+list(map(int, input().split())))
student_application.sort(key=lambda x: (-(x[1]+x[2]), -x[1]))
for application in student_application:
    for choice in application[3:]:
        if len(school_application[choice]) < school_quota[choice] or (school_application[choice][-1][1] == application[1] and school_application[choice][-1][2] == application[2]):
            school_application[choice].append(application[:3])
            break
for application in school_application:
    print(' '.join((map(str, sorted(i[0] for i in application)))))

'''
students, schools, choices = map(int, input().split())
school_quota = list(map(int, input().split()))
student_application, school_application = [], [[] for _ in range(schools)]
for i in range(students):
    student_application.append([i]+list(map(int, input().split())))
student_application.sort(key=lambda x: (-(x[1]+x[2]), -x[1]))
i = 0
while i < students:
    same_rank = [i]
    same_total_score = student_application[i][1]+student_application[i][2]
    same_entrance_score = student_application[i][1]
    for j in range(i+1, students):
        if student_application[j][1]+student_application[j][2] == same_total_score and student_application[j][1] == same_entrance_score:
            same_rank.append(j)
        else:
            break
    else:
        i = j + 1
    if i != j + 1:
        i = j
    temp = {}
    for j in same_rank:
        for app in student_application[j][3:]:
            if len(school_application[app]) < school_quota[app]:
                try:
                    temp[app].append(student_application[j][0])
                except:
                    temp[app] = [student_application[j][0]]
                break
    for key, value in temp.items():
        school_application[key] += value
    if i == students - 1 and j == students - 1:
        break
for i in range(schools):
    if school_application[i]:
        print(' '.join(map(str, sorted(school_application[i]))))
    else:
        print('')
'''
