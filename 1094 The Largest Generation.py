"""
A family hierarchy is usually presented by a pedigree tree where all the nodes on the same level belong to the same generation. Your task is to find the generation with the largest population.
Input Specification:

Each input file contains one test case. Each case starts with two positive integers N (<100) which is the total number of family members in the tree (and hence assume that all the members are numbered from 01 to N), and M (<N) which is the number of family members who have children. Then M lines follow, each contains the information of a family member in the following format:

ID K ID[1] ID[2] ... ID[K]

where ID is a two-digit number representing a family member, K (>0) is the number of his/her children, followed by a sequence of two-digit ID's of his/her children. For the sake of simplicity, let us fix the root ID to be 01. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in one line the largest population number and the level of the corresponding generation. It is assumed that such a generation is unique, and the root level is defined to be 1.

Sample Input:

23 13
21 1 23
01 4 03 02 04 05
03 3 06 07 08
06 2 12 13
13 1 21
08 2 15 16
02 2 09 10
11 2 19 20
17 1 22
05 1 11
07 1 14
09 1 17
10 1 18

Sample Output:

9 4
"""

##################################################
"""
写的代码不够严谨，没按照规定先把根节点入组，而是直接将根节点的儿子入组，导致测试点1出现返回非零，因为测试点1只有根节点，直接将根节点的儿子入组导致非零返回
"""
##################################################

n, m = map(int, input().split())
pedigree = {}
for _ in range(m):
    line = list(map(int, input().split()))
    if line[1] == 1:
        pedigree[line[0]] = [line[2]]
    else:
        pedigree[line[0]] = line[2:]
child = [1]
largest_pop, largest_pop_level, level = 1, 1, 1
while child:
    if len(child) > largest_pop:
        largest_pop = len(child)
        largest_pop_level = level
    temp = []
    for father in child:
        if father in pedigree:
            temp += pedigree[father]
    child = temp
    level += 1
print(largest_pop, largest_pop_level)
