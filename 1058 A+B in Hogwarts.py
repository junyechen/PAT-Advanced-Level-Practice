"""
If you are a fan of Harry Potter, you would know the world of magic has its own currency system -- as Hagrid explained it to Harry, "Seventeen silver Sickles to a Galleon and twenty-nine Knuts to a Sickle, it's easy enough." Your job is to write a program to compute A+B where A and B are given in the standard form of Galleon.Sickle.Knut (Galleon is an integer in [0,10​7​​], Sickle is an integer in [0, 17), and Knut is an integer in [0, 29)).
Input Specification:

Each input file contains one test case which occupies a line with A and B in the standard form, separated by one space.
Output Specification:

For each test case you should output the sum of A and B in one line, with the same format as the input.
Sample Input:

3.2.1 10.16.27

Sample Output:

14.1.28
"""

#############################################
"""
本题非常简单，一次通过
python无需考虑数位溢出问题
"""
#############################################

A, B = input().split()
A = list(map(int, A.split('.')))
B = list(map(int, B.split('.')))
C = [0] * 3
if A[2] + B[2] >= 29:
    C[2] = A[2] + B[2] - 29
    C[1] = 1
else:
    C[2] = A[2] + B[2]
if A[1] + B[1] + C[1] >= 17:
    C[1] += A[1] + B[1] - 17
    C[0] = 1
else:
    C[1] += A[1] + B[1]
C[0] += A[0] + B[0]
print('%d.%d.%d' % (C[0], C[1], C[2]))
