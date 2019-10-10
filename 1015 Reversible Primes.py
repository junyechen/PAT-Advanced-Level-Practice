"""
A reversible prime in any number system is a prime whose "reverse" in that number system is also a prime. For example in the decimal system 73 is a reversible prime because its reverse 37 is also a prime.

Now given any two positive integers N (<10
​5
​​ ) and D (1<D≤10), you are supposed to tell if N is a reversible prime with radix D.

Input Specification:

The input file consists of several test cases. Each case occupies a line which contains two integers N and D. The input is finished by a negative N.

Output Specification:

For each test case, print in one line Yes if N is a reversible prime with radix D, or No if not.

Sample Input:

73 10
23 2
23 10
-2
Sample Output:

Yes
Yes
No
"""

###########################################################
"""
本题简单
用python建立素数表，数字范围为＜10^5，则进制逆转后，最大为16^4-1，因n若转成16进制，则最多4位
进制转换非常简单
注意本身数字是否为素数！
"""
###########################################################

prime = [1] * 65536
prime[0] = 0
prime[1] = 0
for i in range(4, 65536, 2):
    prime[i] = 0
for i in range(3, 65536, 2):
    if prime[i] == 1:
        if i * 3 < 65536:
            for j in range(i*3, 65536, i * 2):
                prime[j] = 0
while True:
    line = input()
    if line[0] == '-':
        break
    else:
        num, radix = [int(i) for i in line.split()]
        if prime[num] == 1:
            num_ = 0
            while num != 0:
                num_ = num_ * radix + num % radix
                num = num // radix
            if prime[num_] == 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
