"""
Scientific notation is the way that scientists easily handle very large numbers or very small numbers. The notation matches the regular expression [+-][1-9].[0-9]+E[+-][0-9]+ which means that the integer portion has exactly one digit, there is at least one digit in the fractional portion, and the number and its exponent's signs are always provided even when they are positive.

Now given a real number A in scientific notation, you are supposed to print A in the conventional notation while keeping all the significant figures.
Input Specification:

Each input contains one test case. For each case, there is one line containing the real number A in scientific notation. The number is no more than 9999 bytes in length and the exponent's absolute value is no more than 9999.
Output Specification:

For each test case, print in one line the input number A in the conventional notation, with all the significant figures kept, including trailing zeros.
Sample Input 1:

+1.23400E-03

Sample Output 1:

0.00123400

Sample Input 2:

-1.2E+10

Sample Output 2:

-12000000000
"""

#############################
"""
非常简单，一次通过
"""
#############################

a, b = input().split('E')
b = int(b)
if b == 0:
    if a[0] == '+':
        print(a[1:])
    else:
        print(a)
elif b > 0:
    if len(a) - 3 <= b:
        a = a[:2]+a[3:]+'0'*(b-(len(a)-3))
    else:
        a = a[:2]+a[3:3+b]+'.'+a[3+b:]
    if a[0] == '+':
        print(a[1:])
    else:
        print(a)
else:
    a = a[0] + '0.' + '0'*(-b-1) + a[1] + a[3:]
    if a[0] == '+':
        print(a[1:])
    else:
        print(a)
