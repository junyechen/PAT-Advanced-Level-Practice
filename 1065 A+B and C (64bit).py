"""
Given three integers A, B and C in [−2​63​​,2​63​​], you are supposed to tell whether A+B>C.
Input Specification:

The first line of the input gives the positive number of test cases, T (≤10). Then T test cases follow, each consists of a single line containing three integers A, B and C, separated by single spaces.
Output Specification:

For each test case, output in one line Case #X: true if A+B>C, or Case #X: false otherwise, where X is the case number (starting from 1).
Sample Input:

3
1 2 3
2 3 4
9223372036854775807 -9223372036854775808 0

Sample Output:

Case #1: false
Case #2: true
Case #3: false
"""

#############################################
"""
本题考查C++的数位溢出问题，但是用python的大数计算直接规避
导致非常简单，一次通过
"""
#############################################

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b > c:
        print('Case #%d: true' % (i + 1))
    else:
        print('Case #%d: false' % (i + 1))
