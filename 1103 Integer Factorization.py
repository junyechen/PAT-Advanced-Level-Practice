"""
The K−P factorization of a positive integer N is to write N as the sum of the P-th power of K positive integers. You are supposed to write a program to find the K−P factorization of N for any positive integers N, K and P.
Input Specification:

Each input file contains one test case which gives in a line the three positive integers N (≤400), K (≤N) and P (1<P≤7). The numbers in a line are separated by a space.
Output Specification:

For each case, if the solution exists, output in the format:

N = n[1]^P + ... n[K]^P

where n[i] (i = 1, ..., K) is the i-th factor. All the factors must be printed in non-increasing order.

Note: the solution may not be unique. For example, the 5-2 factorization of 169 has 9 solutions, such as 12​2​​+4​2​​+2​2​​+2​2​​+1​2​​, or 11​2​​+6​2​​+2​2​​+2​2​​+2​2​​, or more. You must output the one with the maximum sum of the factors. If there is a tie, the largest factor sequence must be chosen -- sequence { a​1​​,a​2​​,⋯,a​K​​ } is said to be larger than { b​1​​,b​2​​,⋯,b​K​​ } if there exists 1≤L≤K such that a​i​​=b​i​​ for i<L and a​L​​>b​L​​.

If there is no solution, simple output Impossible.
Sample Input 1:

169 5 2

Sample Output 1:

169 = 6^2 + 6^2 + 6^2 + 6^2 + 5^2

Sample Input 2:

169 167 3

Sample Output 2:

Impossible
"""

##########################################
"""
本题可采用穷举法，注意递归回溯时的边界条件设置：
    1. 数字个数用完
        1. 刚好和为所求数，输出等式
        2. 和不为所求数，返回
    2. 数字个数没用完，但和已穷尽，返回
    3. 每一层递归，都是因数从大到小回溯，记录上一级因数，若本级因数大于上一级因数，跳过该本级因数的后续操作

python有超时，无法解决
"""
##########################################


def k_p(n, k, p, max_fac, temp_sec):
    global ans, res
    if k == 0:
        if n == 0:
            if sum(temp_sec) > ans:
                ans = sum(temp_sec)
                res = temp_sec.copy()
            return
        else:
            return
    elif n <= 0:
        return
    else:
        for i in range(int(n**(1/p)), int((n/k)**(1/p))-1, -1):
            if i > max_fac or i == 0:
                continue
            k_p(n-i**p, k-1, p, i, temp_sec+[i])


N, K, P = map(int, input().split())
ans = 0
res = []
k_p(N, K, P, int(N**(1/P)), [])
if res:
    print(N, '=', ' + '.join(map(lambda x: str(x) + '^' + str(P), res)))
else:
    print("Impossible")
