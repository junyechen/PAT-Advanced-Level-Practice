"""
This time, you are supposed to find A+B where A and B are two polynomials.
Input Specification:

Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial:

K N​1​​ a​N​1​​​​ N​2​​ a​N​2​​​​ ... N​K​​ a​N​K​​​​

where K is the number of nonzero terms in the polynomial, N​i​​ and a​N​i​​​​ (i=1,2,⋯,K) are the exponents and coefficients, respectively. It is given that 1≤K≤10，0≤N​K​​<⋯<N​2​​<N​1​​≤1000.
Output Specification:

For each test case you should output the sum of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate to 1 decimal place.
Sample Input:

2 1 2.4 0 3.2
2 2 1.5 1 0.5

Sample Output:

3 2 1.5 1 2.9 0 3.2
"""
###############################################################
"""
不清楚第一次提交哪里出现问题，不过下次可以注意到底有多少数，可以通过建立数组方式，简化编程
"""
###############################################################

###############################################################
a = input().split()
b = input().split()
poly = [0] * 1001
for i in range(1,len(a),2):
    poly[int(a[i])]+=float(a[i + 1])
for i in range(1,len(b),2):
    poly[int(b[i])]+=float(b[i + 1])
poly_ = []
for i in range(1000,-1,-1):
    if poly[i] != 0:
        poly_.append(str(i))
        poly_.append('{:.1f}'.format(poly[i]))
if len(poly_) == 0:
    print(0)
else:
    print(int(len(poly_) / 2),end=' ')
    print(' '.join(poly_))
###############################################################

###############################################################
"""
a = input().split()
b = input().split()
poly = {}
for i in range(1,len(a),2):
    if poly.__contains__(int(a[i])):
        poly[int(a[i])]+=float(a[i + 1])
    else:
        poly[int(a[i])] = float(a[i + 1])
for i in range(1,len(b),2):
    if poly.__contains__(int(b[i])):
        poly[int(b[i])]+=float(b[i + 1])
    else:
        poly[int(b[i])] = float(b[i + 1])
for v,k in poly.items():
    if k == 0:
        poly.popitem(v,k)
poly = sorted(poly.items(),key=lambda x:-x[0])
print(len(poly),end=' ')
for i in range(0,len(poly) - 1):
    print(poly[i][0],'{:.1f}'.format(poly[i][1]), end=' ')
print(poly[-1][0],'{:.1f}'.format(poly[-1][1]))
"""
#################################################################