"""
Cutting an integer means to cut a K digits lone integer Z into two integers of (K/2) digits long integers A and B. For example, after cutting Z = 167334, we have A = 167 and B = 334. It is interesting to see that Z can be devided by the product of A and B, as 167334 / (167 × 334) = 3. Given an integer Z, you are supposed to test if it is such an integer.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤ 20). Then N lines follow, each gives an integer Z (10 ≤ Z <2​31​​). It is guaranteed that the number of digits of Z is an even number.
Output Specification:

For each case, print a single line Yes if it is such a number, or No if not.
Sample Input:

3
167334
2333
12345678

Sample Output:

Yes
No
No
"""

#############################################
"""
非常简单，利用python的大数运算功能，不用考虑数位问题

需注意除数是0的情况
"""
#############################################

for _ in range(int(input())):
    z = input()
    a = z[:len(z) // 2]
    b = z[len(z) // 2:]
    try:
        if int(z) % (int(a) * int(b)) == 0:
            print('Yes')
        else:
            print('No')
    except:
        print('No')
