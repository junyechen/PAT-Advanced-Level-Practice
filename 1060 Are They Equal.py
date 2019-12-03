"""
If a machine can save only 3 significant digits, the float numbers 12300 and 12358.9 are considered equal since they are both saved as 0.123×10​5​​ with simple chopping. Now given the number of significant digits on a machine and two float numbers, you are supposed to tell if they are treated equal in that machine.
Input Specification:

Each input file contains one test case which gives three numbers N, A and B, where N (<100) is the number of significant digits, and A and B are the two float numbers to be compared. Each float number is non-negative, no greater than 10​100​​, and that its total digit number is less than 100.
Output Specification:

For each test case, print in a line YES if the two numbers are treated equal, and then the number in the standard form 0.d[1]...d[N]*10^k (d[1]>0 unless the number is 0); or NO if they are not treated equal, and then the two numbers in their standard form. All the terms must be separated by a space, with no extra space at the end of a line.

Note: Simple chopping is assumed without rounding.
Sample Input 1:

3 12300 12358.9

Sample Output 1:

YES 0.123*10^5

Sample Input 2:

3 120 128

Sample Output 2:

NO 0.120*10^3 0.128*10^3
"""

#######################################################
"""
本题一开始想的过于简单，但本质上就是数字的标准化，但题目需要考查的变量较多：
    关键在于小数点dot和第一个有效数字位val
    1. 因为0.0等0的特殊情况，我们可以先排除掉
    2. 当没有小数点时（即dot==-1）:
        则找到第一个有效数字位，往后取n位，如果不够则补0，最终幂次为len(s)-val -- 可能存在00100这样形式的数字
    3. 当有小数点时：
        1. 当有效数字位数大于小数点，即0.00···x的形式，则找到第一个有效数字位，往后取n位，如果不够则补0，最终幂次为-(val-dot-1)
        2. 当有效数字位数小于小数点，即xxx.yy的形式
            1. 当小数点-有效数字位数，即有效整数xxx的长度大于n，则找到第一个有效数字位，往后取n位，最终幂次为dot-val
            2. 当小数点-有效数字位数，即有效整数xxx的长度小于n，则找到第一个有效数字位，往后取n+1位（越过dot位）,如果不够则补0，最终幂次为dot-val`
"""
#######################################################


def normalize(s):
    global n
    if float(s) == 0:
        return '0.' + '0' * n + '*10^0'
    else:
        dot = s.find('.')
        for i in range(len(s)):
            if s[i] == '0' or s[i] == '.':
                pass
            else:
                val = i
                break
        if dot == -1:
            if len(s) - val >= n:
                return '0.' + s[val:val+n] + '*10^%d' % len(s)
            else:
                return '0.' + s[val:] + '0' * (n - len(s) + val) + '*10^%d' % (len(s) - val)
        else:
            if dot < val:
                if len(s) - val >= n:
                    return '0.' + s[val:val + n] + '*10^%d' % (dot - val + 1)
                else:
                    return '0.' + s[val:] + '0' * (n - len(s) + val) + '*10^%d' % (dot - val + 1)
            else:
                if len(s) - val - 1 >= n:
                    if dot - val >= n:
                        return '0.' + s[val:val + n] + '*10^%d' % (dot - val)
                    else:
                        return '0.' + s[val:dot] + s[dot + 1:val + n + 1] + '*10^%d' % (dot - val)
                else:
                    return '0.' + s[val:dot] + s[dot + 1:] + '0' * (n - len(s) + val) + '*10^%d' % (dot - val)


n, a, b = input().split()
n = int(n)
a = normalize(a)
b = normalize(b)
if a == b:
    print('YES', a)
else:
    print('NO', a, b)

"""
n, a, b = input().split()
n = int(n)
if len(a) >= n and len(b) >= n:
    if a[:n] == b[:n]:
        print('YES 0.%s*10^%d' % (a[:n], len(a)))
    else:
        print('NO 0.%s*10^%d 0.%s*10^%d' % (a[:n], len(a), b[:n], len(b)))
elif len(a) < n and len(b) < n:
    if a == b and a != '0':
        print('YES 0.%s*10^%d' % (a, len(a)))
    elif a == b:
        print('YES 0 0')
    else:
        if float(a) == 0:
            print('NO 0 0.%s*10^%d' % (b, len(b)))
        elif float(b) == 0:
            print('NO 0 0.%s*10^%d' % (a, len(a)))
        else:
            print('NO 0.%s*10^%d 0.%s*10^%d' % (a, len(a), b, len(b)))
else:
    if float(a) == float(b):
        if len(a) > len(b):
            print('YES 0.%s*10^%d' % (a[:n], len(a)))
        else:
            print('YES 0.%s*10^%d' % (b[:n], len(b)))
    else:
        if len(a) > len(b):
            print('NO 0.%s*10^%d 0.%s*10^%d' % (a[:n], len(a), b, len(b)))
        else:
            print('NO 0.%s*10^%d 0.%s*10^%d' % (a, len(a), b[:n], len(b)))
"""
