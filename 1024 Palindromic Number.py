"""
A number that will be the same when it is written forwards or backwards is known as a Palindromic Number. For example, 1234321 is a palindromic number. All single digit numbers are palindromic numbers.

Non-palindromic numbers can be paired with palindromic ones via a series of operations. First, the non-palindromic number is reversed and the result is added to the original number. If the result is not a palindromic number, this is repeated until it gives a palindromic number. For example, if we start from 67, we can obtain a palindromic number in 2 steps: 67 + 76 = 143, and 143 + 341 = 484.

Given any positive integer N, you are supposed to find its paired palindromic number and the number of steps taken to find it.

Input Specification:

Each input file contains one test case. Each case consists of two positive numbers N and K, where N (≤10
​10
​​ ) is the initial numer and K (≤100) is the maximum number of steps. The numbers are separated by a space.

Output Specification:

For each test case, output two numbers, one in each line. The first number is the paired palindromic number of N, and the second number is the number of steps taken to find the palindromic number. If the palindromic number is not found after K steps, just output the number obtained at the Kth step and K instead.

Sample Input 1:

67 3
Sample Output 1:

484
2
Sample Input 2:

69 3
Sample Output 2:

1353
3
"""


############################################
"""
利用python的大数计算功能，本题非常简单
"""
############################################


N, K = [int(_) for _ in input().split()]
step = 0
while step <= K:
    N = str(N)
    flag = True
    for i in range(len(N)//2):
        if N[i] == N[len(N)-1-i]:
            pass
        else:
            flag = False
            break
    if flag:
        print(N)
        print(step)
        break
    else:
        if step == K:
            print(N)
            print(step)
            break
        else:
            N = int(N) + int(N[::-1])
            step += 1
