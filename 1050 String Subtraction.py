"""
Given two strings S​1​​ and S​2​​, S=S​1​​−S​2​​ is defined to be the remaining string after taking all the characters in S​2​​ from S​1​​. Your task is simply to calculate S​1​​−S​2​​ for any given strings. However, it might not be that simple to do it fast.
Input Specification:

Each input file contains one test case. Each case consists of two lines which gives S​1​​ and S​2​​, respectively. The string lengths of both strings are no more than 10​4​​. It is guaranteed that all the characters are visible ASCII codes and white space, and a new line character signals the end of a string.
Output Specification:

For each test case, print S​1​​−S​2​​ in one line.
Sample Input:

They are students.
aeiou

Sample Output:

Thy r stdnts.
"""

####################################
"""
本题非常简单，一次通过
可用set()将字符串s2压缩成单字符集，然后与s1逐个比较
"""
####################################

s1 = input()
s2 = set(input())
s = ''
for _ in s1:
    if _ in s2:
        continue
    else:
        s += _
print(s)
