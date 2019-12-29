"""
Given an integer with no more than 9 digits, you are supposed to read it in the traditional Chinese way. Output Fu first if it is negative. For example, -123456789 is read as Fu yi Yi er Qian san Bai si Shi wu Wan liu Qian qi Bai ba Shi jiu. Note: zero (ling) must be handled correctly according to the Chinese tradition. For example, 100800 is yi Shi Wan ling ba Bai.
Input Specification:

Each input file contains one test case, which gives an integer with no more than 9 digits.
Output Specification:

For each test case, print in a line the Chinese way of reading the number. The characters are separated by a space and there must be no extra space at the end of the line.
Sample Input 1:
-123456789

Sample Output 1:
Fu yi Yi er Qian san Bai si Shi wu Wan liu Qian qi Bai ba Shi jiu

Sample Input 2:
100800

Sample Output 2:
yi Shi Wan ling ba Bai
"""

#######################################################################################
"""
本题看起来简单，难度在0的处理
关键：只有非零数前的那个0才读0
    因此，以100800为例
        最后2个0，后面没有非零数，则不读
        中间2个0，后面为'8'，仅读'8'前面的那个0
其余：
    以逆序处理字符串为宜，数位%4=1的为十，%4=2的为百，%4=3的为千，=4的为万，=8的为亿
    前面3个都需判断是否为0，如果为0，则不输出该位进制
    对于关键问题，逆序时，前一个数非零，则该位输出'ling'，否则不输出
"""
#######################################################################################

number = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'ling']
n = input()
if n == '0':
    print('ling')
else:
    if n[0] == '-':
        n = n[1:]
        print('Fu', end=' ')
    n = n[::-1]
    res = []
    for i, j in enumerate(n):
        if i % 4 == 1 and j != '0':
            res.append('Shi')
        elif i % 4 == 2 and j != '0':
            res.append('Bai')
        elif i % 4 == 3 and j != '0':
            res.append('Qian')
        elif i == 4:
            res.append("Wan")
        elif i == 8:
            res.append('Yi')
        if j != '0' or (i >= 1 and n[i-1] != '0'):
            res.append(number[int(j)])
    res = res[::-1]
    print(' '.join(res))
