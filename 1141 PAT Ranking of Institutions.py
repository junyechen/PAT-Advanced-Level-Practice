"""
After each PAT, the PAT Center will announce the ranking of institutions based on their students' performances. Now you are asked to generate the ranklist.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10​5​​), which is the number of testees. Then N lines follow, each gives the information of a testee in the following format:

ID Score School

where ID is a string of 6 characters with the first one representing the test level: B stands for the basic level, A the advanced level and T the top level; Score is an integer in [0, 100]; and School is the institution code which is a string of no more than 6 English letters (case insensitive). Note: it is guaranteed that ID is unique for each testee.
Output Specification:

For each case, first print in a line the total number of institutions. Then output the ranklist of institutions in nondecreasing order of their ranks in the following format:

Rank School TWS Ns

where Rank is the rank (start from 1) of the institution; School is the institution code (all in lower case); ; TWS is the total weighted score which is defined to be the integer part of ScoreB/1.5 + ScoreA + ScoreT*1.5, where ScoreX is the total score of the testees belong to this institution on level X; and Ns is the total number of testees who belong to this institution.

The institutions are ranked according to their TWS. If there is a tie, the institutions are supposed to have the same rank, and they shall be printed in ascending order of Ns. If there is still a tie, they shall be printed in alphabetical order of their codes.
Sample Input:

10
A57908 85 Au
B57908 54 LanX
A37487 60 au
T28374 67 CMU
T32486 24 hypu
A66734 92 cmu
B76378 71 AU
A47780 45 lanx
A72809 100 pku
A03274 45 hypu

Sample Output:

5
1 cmu 192 2
1 au 192 3
3 pku 100 1
4 hypu 81 2
4 lanx 81 2
"""

###########################################################
"""
python超时无法解决，但是有说有时候可以在时间内解决问题，或许在成绩相加时，在最后进行乘除处理，即先按类别进行相加，最后再进行乘除处理得到最后的数
"""
###########################################################

res = {}
for _ in range(int(input())):
    ID, score, school = input().split()
    if ID[0] == 'A':
        score = int(score)
    elif ID[0] == 'B':
        score = int(score) / 1.5
    else:
        score = int(score) * 1.5
    school = school.lower()
    if school in res:
        res[school][0] += score
        res[school][1] += 1
    else:
        res[school] = [score, 1]
res = [[key] + values for key, values in res.items()]
res.sort(key=lambda x: (-int(x[1]), x[2], x[0]))
print(len(res))
print('1', res[0][0], int(res[0][1]), res[0][2])
last = int(res[0][1])
rank = 1
for i in range(1, len(res)):
    if int(res[i][1]) == last:
        print(rank, res[i][0], last, res[i][2])
    else:
        rank = i + 1
        last = int(res[i][1])
        print(rank, res[i][0], last, res[i][2])
