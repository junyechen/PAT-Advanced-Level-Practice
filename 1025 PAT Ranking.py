"""
Programming Ability Test (PAT) is organized by the College of Computer Science and Technology of Zhejiang University. Each test is supposed to run simultaneously in several places, and the ranklists will be merged immediately after the test. Now it is your job to write a program to correctly merge all the ranklists and generate the final rank.

Input Specification:

Each input file contains one test case. For each case, the first line contains a positive number N (≤100), the number of test locations. Then N ranklists follow, each starts with a line containing a positive integer K (≤300), the number of testees, and then K lines containing the registration number (a 13-digit number) and the total score of each testee. All the numbers in a line are separated by a space.

Output Specification:

For each test case, first print in one line the total number of testees. Then print the final ranklist in the following format:

registration_number final_rank location_number local_rank
The locations are numbered from 1 to N. The output must be sorted in nondecreasing order of the final ranks. The testees with the same score must have the same rank, and the output must be sorted in nondecreasing order of their registration numbers.

Sample Input:

2
5
1234567890001 95
1234567890005 100
1234567890003 95
1234567890002 77
1234567890004 85
4
1234567890013 65
1234567890011 25
1234567890014 100
1234567890012 85
Sample Output:

9
1234567890005 1 1 1
1234567890014 1 2 1
1234567890001 3 1 2
1234567890003 3 1 2
1234567890004 5 1 4
1234567890012 5 2 2
1234567890002 7 1 5
1234567890013 8 2 3
1234567890011 9 2 4
"""


########################
"""
题目非常简单，一次通过。
需注意并列名次问题。
"""
########################


n = int(input())
testee = []
for _ in range(n):
    k = int(input())
    test = []
    for i in range(k):
        reg, score = input().split()
        test.append([reg, _ + 1, int(score), 0])
    test.sort(key=lambda x: (-x[2], x[0]))
    temp_rank = 1
    rank_remain = 1
    temp_score = test[0][2]
    test[0][3] = 1
    for i in range(1, len(test)):
        if test[i][2] == temp_score:
            test[i][3] = temp_rank
            rank_remain += 1
        else:
            temp_rank += rank_remain
            rank_remain = 1
            test[i][3] = temp_rank
            temp_score = test[i][2]
    testee += test
testee.sort(key=lambda x: (-x[2], x[0]))
print(len(testee))
temp_rank = 1
rank_remain = 1
temp_score = testee[0][2]
print(testee[0][0], temp_rank, testee[0][1], testee[0][3])
for i in range(1, len(testee)):
    if testee[i][2] == temp_score:
        print(testee[i][0], temp_rank, testee[i][1], testee[i][3])
        rank_remain += 1
    else:
        temp_rank += rank_remain
        rank_remain = 1
        print(testee[i][0], temp_rank, testee[i][1], testee[i][3])
        temp_score = testee[i][2]
