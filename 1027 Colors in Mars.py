"""
People in Mars represent the colors in their computers in a similar way as the Earth people. That is, a color is represented by a 6-digit number, where the first 2 digits are for Red, the middle 2 digits for Green, and the last 2 digits for Blue. The only difference is that they use radix 13 (0-9 and A-C) instead of 16. Now given a color in three decimal numbers (each between 0 and 168), you are supposed to output their Mars RGB values.

Input Specification:

Each input file contains one test case which occupies a line containing the three decimal color values.

Output Specification:

For each test case you should output the Mars RGB value in the following format: first output #, then followed by a 6-digit number where all the English characters must be upper-cased. If a single color is only 1-digit long, you must print a 0 to its left.

Sample Input:

15 43 71
Sample Output:

#123456
"""


########################################################################
"""
非常简单的题目，一次通过
学习了map(func, list)的用法，注意第一个参数使用的是函数，不能是list或者dict
"""
########################################################################


def trans(digit):
    return t[digit]


def tran(digit):
    num = []
    for _ in range(2):
        num.insert(0, digit % 13)
        digit = digit // 13
    return ''.join(list(map(trans, num)))


t = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']
color = [int(_) for _ in input().split()]
print('#%s%s%s' % (tran(color[0]), tran(color[1]), tran(color[2])))
