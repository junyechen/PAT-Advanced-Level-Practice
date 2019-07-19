"""
Given a non-negative integer N, your task is to compute the sum of all the digits of N, and output every digit of the sum in English.
Input Specification:

Each input file contains one test case. Each case occupies one line which contains an N (≤10​100​​).
Output Specification:

For each test case, output in one line the digits of the sum in English words. There must be one space between two consecutive words, but no extra space at the end of a line.
Sample Input:

12345

Sample Output:

one five
"""

########################################################################################################################
"""
简单，一次通过
善用map函数
"""
########################################################################################################################

trans = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

def trans_(num):
    return trans[num]

N = [int(i) for i in input()]
sum_ = str(sum(N))
sum_ = list(map(trans_,sum_))
print(' '.join(sum_))