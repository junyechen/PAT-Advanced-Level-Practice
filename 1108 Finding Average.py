"""
The basic task is simple: given N real numbers, you are supposed to calculate their average. But what makes it complicated is that some of the input numbers might not be legal. A legal input is a real number in [−1000,1000] and is accurate up to no more than 2 decimal places. When you calculate the average, those illegal numbers must not be counted in.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤100). Then N numbers are given in the next line, separated by one space.
Output Specification:

For each illegal input number, print in a line ERROR: X is not a legal number where X is the input. Then finally print in a line the result: The average of K numbers is Y where K is the number of legal inputs and Y is their average, accurate to 2 decimal places. In case the average cannot be calculated, output Undefined instead of Y. In case K is only 1, output The average of 1 number is Y instead.
Sample Input 1:

7
5 -3.2 aaa 9999 2.3.4 7.123 2.35

Sample Output 1:

ERROR: aaa is not a legal number
ERROR: 9999 is not a legal number
ERROR: 2.3.4 is not a legal number
ERROR: 7.123 is not a legal number
The average of 3 numbers is 1.38

Sample Input 2:

2
aaa -9999

Sample Output 2:

ERROR: aaa is not a legal number
ERROR: -9999 is not a legal number
The average of 0 numbers is Undefined
"""

#########################################
"""
非常简单，利用异常机制
"""
#########################################

N = int(input())
number = input().split()
total, amount = 0, 0
for i in range(N):
    try:
        number_int = int(number[i])
        if -1000 <= number_int <= 1000:
            total += number_int
            amount += 1
        else:
            print("ERROR: %s is not a legal number" % number[i])
    except:
        try:
            number_float = float(number[i])
            number_split = number[i].split('.')
            if len(number_split[1]) > 2:
                print("ERROR: %s is not a legal number" % number[i])
            else:
                if -1000 <= number_float <= 1000:
                    total += number_float
                    amount += 1
                else:
                    print("ERROR: %s is not a legal number" % number[i])
        except:
            print("ERROR: %s is not a legal number" % number[i])
if amount == 0:
    print("The average of 0 numbers is Undefined")
elif amount == 1:
    print("The average of 1 number is %.2f" % total)
else:
    print("The average of %d numbers is %.2f" % (amount, total/amount))
