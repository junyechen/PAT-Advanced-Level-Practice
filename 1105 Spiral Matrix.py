"""
This time your job is to fill a sequence of N positive integers into a spiral matrix in non-increasing order. A spiral matrix is filled in from the first element at the upper-left corner, then move in a clockwise spiral. The matrix has m rows and n columns, where m and n satisfy the following: m×n must be equal to N; m≥n; and m−n is the minimum of all the possible values.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N. Then the next line contains N positive integers to be filled into the spiral matrix. All the numbers are no more than 10​4​​. The numbers in a line are separated by spaces.
Output Specification:

For each test case, output the resulting matrix in m lines, each contains n numbers. There must be exactly 1 space between two adjacent numbers, and no extra space at the end of each line.
Sample Input:

12
37 76 20 98 76 42 53 95 60 81 58 93

Sample Output:

98 95 93
42 37 81
53 20 76
58 60 76
"""

#######################################################
"""
简单的题目还调试了很久，最终发现符号逻辑错误，真是太菜了！
"""
#######################################################

N = int(input())
data = sorted(map(int, input().split()), reverse=True)
for i in range(int(N**0.5), 0, -1):
    if N % i == 0:
        m = N // i
        n = i
        break
matrix = [[0 for _ in range(n)] for _ in range(m)]
up = left = 0
bottom = m - 1
right = n - 1
x, y, loc = -1, 0, 0
direction = 0
while loc != N:
    if direction == 0:
        x += 1
        if x > right:
            x -= 1
            y += 1
            direction = 1
            up += 1
    elif direction == 1:
        y += 1
        if y > bottom:
            x -= 1
            y -= 1
            direction = 2
            right -= 1
    elif direction == 2:
        x -= 1
        if x < left:
            x += 1
            y -= 1
            direction = 3
            bottom -= 1
    else:
        y -= 1
        if y < up:
            x += 1
            y += 1
            direction = 0
            left += 1
    matrix[y][x] = data[loc]
    loc += 1
for i in range(m):
    print(' '.join(map(str, matrix[i])))
