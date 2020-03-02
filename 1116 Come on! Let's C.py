"""
"Let's C" is a popular and fun programming contest hosted by the College of Computer Science and Technology, Zhejiang University. Since the idea of the contest is for fun, the award rules are funny as the following:

    0、 The Champion will receive a "Mystery Award" (such as a BIG collection of students' research papers...).
    1、 Those who ranked as a prime number will receive the best award -- the Minions (小黄人)!
    2、 Everyone else will receive chocolates.

Given the final ranklist and a sequence of contestant ID's, you are supposed to tell the corresponding awards.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10​4​​), the total number of contestants. Then N lines of the ranklist follow, each in order gives a contestant's ID (a 4-digit number). After the ranklist, there is a positive integer K followed by K query ID's.
Output Specification:

For each query, print in a line ID: award where the award is Mystery Award, or Minion, or Chocolate. If the ID is not in the ranklist, print Are you kidding? instead. If the ID has been checked before, print ID: Checked.
Sample Input:

6
1111
6666
8888
1234
5555
0001
6
8888
0001
1111
2222
8888
2222

Sample Output:

8888: Minion
0001: Chocolate
1111: Mystery Award
2222: Are you kidding?
8888: Checked
2222: Are you kidding?
"""


###################################################
"""
又是边界坑爹的一题，≤10000，最后真有10000个数据，debug了半天、、、
"""
###################################################


max_num = 10001
primes = [1] * max_num
primes[0], primes[1] = 0, 0
for i in range(4, max_num, 2):
    primes[i] = 0
for i in range(3, max_num, 2):
    if primes[i] == 1:
        for j in range(i*3, max_num, i*2):
            primes[j] = 0
contestants = [0] * max_num
for i in range(int(input())):
    contestants[int(input())] = i + 1
for i in range(int(input())):
    query = int(input())
    if contestants[query] == 0:
        print('%04d: Are you kidding?' % query)
        continue
    elif contestants[query] == -1:
        print('%04d: Checked' % query)
    elif contestants[query] == 1:
        print('%04d: Mystery Award' % query)
    elif primes[contestants[query]] == 1:
        print('%04d: Minion' % query)
    else:
        print('%04d: Chocolate' % query)
    contestants[query] = -1
