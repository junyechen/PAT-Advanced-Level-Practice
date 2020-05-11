"""
In July 2004, Google posted on a giant billboard along Highway 101 in Silicon Valley (shown in the picture below) for recruitment. The content is super-simple, a URL consisting of the first 10-digit prime found in consecutive digits of the natural constant e. The person who could find this prime number could go to the next step in Google's hiring process by visiting this website.

prime.jpg

The natural constant e is a well known transcendental number（超越数）. The first several digits are: e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921... where the 10 digits in bold are the answer to Google's question.

Now you are asked to solve a more general problem: find the first K-digit prime in consecutive digits of any given L-digit number.
Input Specification:

Each input file contains one test case. Each case first gives in a line two positive integers: L (≤ 1,000) and K (< 10), which are the numbers of digits of the given number and the prime to be found, respectively. Then the L-digit number N is given in the next line.
Output Specification:

For each test case, print in a line the first K-digit prime in consecutive digits of N. If such a number does not exist, output 404 instead. Note: the leading zeroes must also be counted as part of the K digits. For example, to find the 4-digit prime in 200236, 0023 is a solution. However the first digit 2 must not be treated as a solution 0002 since the leading zeroes are not in the original number.
Sample Input 1:

20 5
23654987725541023819

Sample Output 1:

49877

Sample Input 2:

10 3
2468024680

Sample Output 2:

404
"""

###################################################
"""
一开始想着建素数表，但最后一个测试点内存超限
转为直接暴力求解是否素数，能全部通过
"""
###################################################


def is_prime(p):
    p = int(p)
    if p == 0 or p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for j in range(3, int(p ** 0.5), 2):
        if p % j == 0:
            return False
    return True


l, k = map(int, input().split())
n = input()
for i in range(l - k + 1):
    if is_prime(n[i:i + k]):
        print(n[i:i + k])
        break
else:
    print(404)

###################################################
"""
l, k = map(int, input().split())
primes = [1] * int(10 ** k)
primes[0] = primes[1] = 0
for i in range(4, len(primes), 2):
    primes[i] = 0
for i in range(3, len(primes) // 3, 2):
    if primes[i] == 1:
        for j in range(i * 3, len(primes), i * 2):
            primes[j] = 0
n = input()
for i in range(l - k + 1):
    if primes[int(n[i:i + k])] == 1:
        print(n[i:i + k])
        break
else:
    print(404)
"""
###################################################
