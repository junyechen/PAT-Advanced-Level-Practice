"""
Some scientists took pictures of thousands of birds in a forest. Assume that all the birds appear in the same picture belong to the same tree. You are supposed to help the scientists to count the maximum number of trees in the forest, and for any pair of birds, tell if they are on the same tree.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive number N (≤10​4​​) which is the number of pictures. Then N lines follow, each describes a picture in the format:

K B​1​​ B​2​​ ... B​K​​

where K is the number of birds in this picture, and B​i​​'s are the indices of birds. It is guaranteed that the birds in all the pictures are numbered continuously from 1 to some number that is no more than 10​4​​.

After the pictures there is a positive number Q (≤10​4​​) which is the number of queries. Then Q lines follow, each contains the indices of two birds.
Output Specification:

For each test case, first output in a line the maximum possible number of trees and the number of birds. Then for each query, print in a line Yes if the two birds belong to the same tree, or No if not.
Sample Input:

4
3 10 1 2
2 3 4
4 1 5 7 8
3 9 6 4
2
10 5
3 7

Sample Output:

2 10
Yes
No
"""


#############################################################
"""
使用并查集，经过历练，这次20min代码就写完，并且只有1个测试点不能通过
python超时无法解决
"""
#############################################################


class Bird:
    def __init__(self, index):
        self.index = index
        self.father = index
        self.num = 1
        self.marked = False


n = int(input())
birds = [Bird(_) for _ in range(10001)]
for _ in range(n):
    pic = list(map(int, input().split()))
    birds[pic[1]].marked = True
    common_father = birds[pic[1]].father
    while common_father != birds[common_father].father:
        common_father = birds[common_father].father
    for bird in pic[2:]:
        birds[bird].marked = True
        father = birds[bird].father
        while father != birds[father].father:
            father = birds[father].father
        if father != common_father:
            birds[common_father].father = father
            birds[bird].father = father
            birds[father].num += birds[common_father].num
            birds[common_father].num = 0
            common_father = father

total_tree, total_bird = 0, 0
for i in range(10001):
    if birds[i].marked and birds[i].num != 0:
        total_tree += 1
        total_bird += birds[i].num
print(total_tree, total_bird)
for _ in range(int(input())):
    a, b = map(int, input().split())
    while a != birds[a].father:
        a = birds[a].father
    while b != birds[b].father:
        b = birds[b].father
    if a == b:
        print("Yes")
    else:
        print("No")
