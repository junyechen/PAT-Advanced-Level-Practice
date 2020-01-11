"""
For two rational numbers, your task is to implement the basic arithmetics, that is, to calculate their sum, difference, product and quotient.
Input Specification:

Each input file contains one test case, which gives in one line the two rational numbers in the format a1/b1 a2/b2. The numerators and the denominators are all in the range of long int. If there is a negative sign, it must appear only in front of the numerator. The denominators are guaranteed to be non-zero numbers.
Output Specification:

For each test case, print in 4 lines the sum, difference, product and quotient of the two rational numbers, respectively. The format of each line is number1 operator number2 = result. Notice that all the rational numbers must be in their simplest form k a/b, where k is the integer part, and a/b is the simplest fraction part. If the number is negative, it must be included in a pair of parentheses. If the denominator in the division is zero, output Inf as the result. It is guaranteed that all the output integers are in the range of long int.
Sample Input 1:
2/3 -4/2

Sample Output 1:
2/3 + (-2) = (-1 1/3)
2/3 - (-2) = 2 2/3
2/3 * (-2) = (-1 1/3)
2/3 / (-2) = (-1/3)

Sample Input 2:
5/3 0/6

Sample Output 2:
1 2/3 + 0 = 1 2/3
1 2/3 - 0 = 1 2/3
1 2/3 * 0 = 0
1 2/3 / 0 = Inf
"""

#########################################
"""
繁琐，但一次通过
"""
#########################################


def reduction(num, den):
    temp = num % den
    divisor = den
    while temp != 0:
        dividend = divisor
        divisor = temp
        temp = dividend % divisor
    num //= divisor
    den //= divisor
    return num, den


def trans(num, den):
    if num == 0:
        return '0'
    elif den == 0:
        return 'Inf'
    else:
        if num < 0:
            flag = True
            num = -num
        else:
            flag = False
        integer = num//den
        temp = num % den
        if temp == 0:
            if flag:
                return '(-%d)' % integer
            else:
                return str(integer)
        else:
            [num, den] = reduction(temp, den)
            if integer == 0:
                if flag:
                    return '(-%d/%d)' % (num, den)
                else:
                    return '%d/%d' % (num, den)
            else:
                if flag:
                    return '(-%d %d/%d)' % (integer, num, den)
                else:
                    return '%d %d/%d' % (integer, num, den)


a, b = input().split()
a1, b1 = map(int, a.split('/'))
a2, b2 = map(int, b.split('/'))
a = trans(a1, b1)
b = trans(a2, b2)
print(a, '+', b, '=', trans(a1*b2+a2*b1, b1*b2))
print(a, '-', b, '=', trans(a1*b2-a2*b1, b1*b2))
print(a, '*', b, '=', trans(a1*a2, b1*b2))
try:
    print(a, '/', b, '=', trans((a1*a2//abs(a1)//abs(a2))*abs(a1*b2), abs(a2*b1)))
except:
    print(a, '/', b, '=', 'Inf')
