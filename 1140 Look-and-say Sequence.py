"""
Look-and-say sequence is a sequence of integers as the following:

D, D1, D111, D113, D11231, D112213111, ...

where D is in [0, 9] except 1. The (n+1)st number is a kind of description of the nth number. For example, the 2nd number means that there is one D in the 1st number, and hence it is D1; the 2nd number consists of one D (corresponding to D1) and one 1 (corresponding to 11), therefore the 3rd number is D111; or since the 4th number is D113, it consists of one D, two 1's, and one 3, so the next number must be D11231. This definition works for D = 1 as well. Now you are supposed to calculate the Nth number in a look-and-say sequence of a given digit D.
Input Specification:

Each input file contains one test case, which gives D (in [0, 9]) and a positive integer N (≤ 40), separated by a space.
Output Specification:

Print in a line the Nth number in a look-and-say sequence of D.
Sample Input:

1 8

Sample Output:

1123123111
"""

###################################################
"""
题目简单，但做题代码需优化，优化前有超时，优化后无超时

利用for而不是while有利于所有数字遍历，且无需判断终点条件
"""
###################################################

d, n = map(int, input().split())
seq = str(d)
for _ in range(1, n):
    last = seq[0]
    start = 0
    temp = ''
    for i in range(len(seq)):
        if last != seq[i]:
            temp += last + str(i-start)
            last = seq[i]
            start = i
    temp += last + str(i-start+1)
    seq = temp
print(seq)

###################################################
"""
d, n = map(int, input().split())
seq = str(d)
for _ in range(1, n):
    last = seq[0]
    i = j = 0
    temp = ''
    while i < len(seq):
        while i < len(seq) and seq[i] == last:
            i += 1
        temp += last + str(i-j)
        j = i
        if i == len(seq):
            break
        else:
            last = seq[i]
    seq = temp
print(seq)
"""
###################################################
