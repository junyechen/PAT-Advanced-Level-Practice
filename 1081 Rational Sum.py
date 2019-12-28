"""
Given N rational numbers in the form numerator/denominator, you are supposed to calculate their sum.
Input Specification:

Each input file contains one test case. Each case starts with a positive integer N (≤100), followed in the next line N rational numbers a1/b1 a2/b2 ... where all the numerators and denominators are in the range of long int. If there is a negative number, then the sign must appear in front of the numerator.
Output Specification:

For each test case, output the sum in the simplest form integer numerator/denominator where integer is the integer part of the sum, numerator < denominator, and the numerator and the denominator have no common factor. You must output only the fractional part if the integer part is 0.
Sample Input 1:
5
2/5 4/15 1/30 -2/60 8/3

Sample Output 1:
3 1/3

Sample Input 2:
2
4/3 2/3

Sample Output 2:
2

Sample Input 3:
3
1/3 -1/6 1/8

Sample Output 3:

7/24
"""

##############################################################
"""
非常简单，一次通过

后面查询得知，python有fraction类，可以直接作分数运算
"""
##############################################################

N = int(input())
number = input().split()
numbers = [[] for _ in range(N)]
for i in range(N):
    numerator, denominator = map(int, number[i].split('/'))
    numbers[i] = [numerator, denominator]
denominator = 1
numerator = 0
for number in numbers:
    denominator *= number[1]
for number in numbers:
    numerator += number[0]*denominator//number[1]
if numerator == 0:
    print(0)
elif numerator % denominator == 0:
    print(numerator//denominator)
else:
    flag = numerator/abs(numerator)
    integer = abs(numerator)//denominator
    numerator = abs(numerator) % denominator
    dividend = denominator
    divisor = numerator
    while dividend % divisor != 0:
        temp = dividend % divisor
        dividend = divisor
        divisor = temp
    numerator /= divisor
    denominator /= divisor
    if integer == 0:
        if flag == 1:
            print('%d/%d' % (numerator, denominator))
        else:
            print('-%d/%d' % (numerator, denominator))
    else:
        if flag == 1:
            print('%d %d/%d' % (integer, numerator, denominator))
        else:
            print('-%d %d/%d' % (integer, numerator, denominator))


