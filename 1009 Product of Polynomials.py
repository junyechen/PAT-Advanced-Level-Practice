"""
This time, you are supposed to find A×B where A and B are two polynomials.
Input Specification:

Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial:

K N​1​​ a​N​1​​​​ N​2​​ a​N​2​​​​ ... N​K​​ a​N​K​​​​

where K is the number of nonzero terms in the polynomial, N​i​​ and a​N​i​​​​ (i=1,2,⋯,K) are the exponents and coefficients, respectively. It is given that 1≤K≤10, 0≤N​K​​<⋯<N​2​​<N​1​​≤1000.
Output Specification:

For each test case you should output the product of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate up to 1 decimal place.
Sample Input:

2 1 2.4 0 3.2
2 2 1.5 1 0.5

Sample Output:

3 3 3.6 2 6.0 1 1.6
"""

#######################################################
"""
这题也很简单，但是没有一次通过，需注意到虽然给的例子里，指数均≤1000，但是乘积的指数会＞1000！
"""
#######################################################

poly = [[] for i in range(2001)]
A = input().split()
B = input().split()
for i in range(int(A[0])):
    for j in range(int(B[0])):
        exp = int(A[i * 2 + 1]) + int(B[j * 2 + 1])
        co = float(A[i * 2 + 2]) * float(B[j * 2 + 2])
        if poly[exp]:
            poly[exp] += co
        else:
            poly[exp] = co
out = []
num = 0
for i in range(1000,-1,-1):
    if poly[i]:
        out += [str(i), "%.1f" % poly[i]]
        num += 1
out.insert(0,str(num))
print(' '.join(out))