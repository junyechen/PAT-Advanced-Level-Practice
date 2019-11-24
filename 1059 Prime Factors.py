"""
Given any positive integer N, you are supposed to find all of its prime factors, and write them in the format N = p​1​​​k​1​​​​×p​2​​​k​2​​​​×⋯×p​m​​​k​m​​​​.
Input Specification:

Each input file contains one test case which gives a positive integer N in the range of long int.
Output Specification:

Factor N in the format N = p​1​​^k​1​​*p​2​​^k​2​​*…*p​m​​^k​m​​, where p​i​​'s are prime factors of N in increasing order, and the exponent k​i​​ is the number of p​i​​ -- hence when there is only one p​i​​, k​i​​ is 1 and must NOT be printed out.
Sample Input:

97532468

Sample Output:

97532468=2^2*11*17*101*1291
"""

###################################################
"""
本题注意学习的点有：
1. long int即long，占4个字节，共32bits，算上正负符号，故最大为2^31-1
2. 本题考查质因数分解，实际上就是考查求素数，可建立素数表的方式得到所有素数
    a. 不需要求得long int范围内的所有素数表，因为必然会超时！
    b. 只要求long int根号范围内的所有素数表，只要求解质因数过程中，出现素数表用完，但原数没除到1，则必然表明剩下的数为素数（大小超过long int根号的值）
3. 原数为1时需单独考虑！
"""
###################################################

long_int = 2 ** 31 - 1
long_int_sq = 46341  # square root of long_int
primes = [1] * (long_int_sq + 1)
prime = [2]
for i in range(3, long_int_sq+1, 2):
    if primes[i] == 1:
        prime.append(i)
        for j in range(i*3, long_int_sq+1, i*2):
            primes[j] = 0
i, k, out = 0, 0, []
N = n = int(input())
if n == 1:
    out = ['1']
else:
    while n != 1:
        while n % prime[i] == 0:
            n = n // prime[i]
            k += 1
        if k != 0:
            if k == 1:
                out.append(str(prime[i]))
            else:
                out.append('%d^%d' % (prime[i], k))
        i += 1
        k = 0
        if i == len(prime):
            out.append(str(n))
            break
print('%d=%s' % (N, '*'.join(out)))
