"""
Given a pair of positive integers, for example, 6 and 110, can this equation 6 = 110 be true? The answer is yes, if 6 is a decimal number and 110 is a binary number.

Now for any pair of positive integers N​1​​ and N​2​​, your task is to find the radix of one number while that of the other is given.
Input Specification:

Each input file contains one test case. Each case occupies a line which contains 4 positive integers:


N1 N2 tag radix

Here N1 and N2 each has no more than 10 digits. A digit is less than its radix and is chosen from the set { 0-9, a-z } where 0-9 represent the decimal numbers 0-9, and a-z represent the decimal numbers 10-35. The last number radix is the radix of N1 if tag is 1, or of N2 if tag is 2.
Output Specification:

For each test case, print in one line the radix of the other number so that the equation N1 = N2 is true. If the equation is impossible, print Impossible. If the solution is not unique, output the smallest possible radix.
Sample Input 1:

6 110 1 10

Sample Output 1:

2

Sample Input 2:

1 ab 1 2

Sample Output 2:

Impossible
"""

##############################################
"""
本题看起来简单，实际有比较多的坑
1. 数字最大到'z'，但不代表最大进制是36
2. python问题就在于超时
    缩短时间方法1: 先遍历N2，得到最大数，然后最大数+1开始遍历进制
    缩短时间方法2：因为n位数最大可以得到radix^n-1，所以可以对得到的基准数做n次根号求整，与方法1得到的最小进制比较，取大者开始遍历进制
    缩短时间方法3：因为n位数最小为radix^(n-1)，所以可以对得到的基准数做(n-1)次根号求整+1（注意只有1位时的处理，直接写range中要变为+2）作为最大进制
    以上缩短方法使用后，测试点7始终超时，只能用C++解决
"""

##############################################
N1, N2, tag, radix = input().split()
if tag == '2':
    temp = N1
    N1 = N2
    N2 = temp
radix = int(radix)
dic = {}
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(i + 97)] = i + 10
N = 0
for i in N1:
    N = N * radix + dic[i]
if N == 0 and N2 == '0':
    print(2)
    exit(0)
elif N == 0 and N2 != '0':
    print("Impossible")
    exit(0)
radix_ = int(dic[max(N2)])
temp = int(N ** (1 / (len(N2))))
radix_ = max(temp,radix_)
for radix_ in range(radix_ + 1,int(N ** (1 / (len(N2)-1) if len(N2)!= 1 else 1)) + 2):
    N_ = 0
    for i in N2:
        N_ = N_ * radix_ + dic[i]
    if N_ == N:
        print(radix_)
        exit(0)
    if N_ > N:
        print("Impossible")
        exit(0)
print("Impossible")
##############################################

##############################################

N1, N2, tag, radix = input().split()
if tag == '2':
    temp = N1
    N1 = N2
    N2 = temp
radix = int(radix)
dic = {}
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(i + 97)] = i + 10
N = 0
for i in N1:
    N = N * radix + dic[i]
if N == 0 and N2 == '0':
    print(2)
    exit(0)
elif N == 0 and N2 != '0':
    print("Impossible")
    exit(0)
radix_ = int(dic[max(N2)])
temp = int(N ** (1 / (len(N2))))
radix_ = max(temp,radix_)
while True:
    radix_ += 1
    N_ = 0
    for i in N2:
        N_ = N_ * radix_ + dic[i]
    if N_ == N:
        print(radix_)
        exit(0)
    if N_ > N:
        print("Impossible")
        exit(0)

########################################
"""
N1, N2, tag, radix = input().split()
if tag == '2':
    temp = N1
    N1 = N2
    N2 = temp
radix = int(radix)
dic = {}
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(i + 97)] = i + 10
N = 0
for i in N1:
    N = N * radix + dic[i]
if N == 0 and N2 == '0':
    print(2)
    exit(0)
elif N == 0 and N2 != '0':
    print("Impossible")
    exit(0)
radix_ = 1
while True:
    radix_ += 1
    N_ = 0
    flag = True
    for i in N2:
        if dic[i] >= radix_:
            flag = False
            break
        N_ = N_ * radix_ + dic[i]
    if flag:
        if N_ == N:
            print(radix_)
            exit(0)
        if N_ > N:
            print("Impossible")
            exit(0)
"""
########################################

########################################
"""
N1, N2, tag, radix = input().split()
if tag == '2':
    temp = N1
    N1 = N2
    N2 = temp
radix = int(radix)
dic = {}
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(i + 97)] = i + 10
N = 0
for i in N1:
    N = N * radix + dic[i]
if N == 0 and N2 == '0':
    print(2)
    exit(0)
elif N == 0 and N2 != '0':
    print("Impossible")
    exit(0)
for radix_ in range(2,37,1):
    N_ = 0
    flag = True
    for i in N2:
        if dic[i] >= radix_:
            flag = False
            break
        N_ = N_ * radix_ + dic[i]
    if flag:
        if N_ == N:
            print(radix_)
            exit(0)
        if N_ > N:
            print("Impossible")
            exit(0)
"""
########################################