"""
The "eight queens puzzle" is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general N queens problem of placing N non-attacking queens on an N×N chessboard. (From Wikipedia - "Eight queens puzzle".)

Here you are NOT asked to solve the puzzles. Instead, you are supposed to judge whether or not a given configuration of the chessboard is a solution. To simplify the representation of a chessboard, let us assume that no two queens will be placed in the same column. Then a configuration can be represented by a simple integer sequence (Q​1​​,Q​2​​,⋯,Q​N​​), where Q​i​​ is the row number of the queen in the i-th column. For example, Figure 1 can be represented by (4, 6, 8, 2, 7, 1, 3, 5) and it is indeed a solution to the 8 queens puzzle; while Figure 2 can be represented by (4, 6, 7, 2, 8, 1, 9, 5, 3) and is NOT a 9 queens' solution.
8q.jpg 		9q.jpg
Figure 1 		Figure 2
Input Specification:

Each input file contains several test cases. The first line gives an integer K (1<K≤200). Then K lines follow, each gives a configuration in the format "N Q​1​​ Q​2​​ ... Q​N​​", where 4≤N≤1000 and it is guaranteed that 1≤Q​i​​≤N for all i=1,⋯,N. The numbers are separated by spaces.
Output Specification:

For each configuration, if it is a solution to the N queens problem, print YES in a line; or NO if not.
Sample Input:

4
8 4 6 8 2 7 1 3 5
9 4 6 7 2 8 1 9 5 3
6 1 5 2 6 4 3
5 1 3 5 2 4

Sample Output:

YES
NO
NO
YES
"""

###################################################################################
"""
题目较为简单，我的做法是，每放置一颗棋子，就对该棋子在棋盘上的对角线位置进行标记，如果下一颗棋子在标记位置上，表明无解

python超时无法解决
"""
###################################################################################

for _ in range(int(input())):
    data = list(map(int, input().split()))
    if data[0] != len(set(data[1:])):
        print('NO')
    else:
        chessboard = [[0 for _ in range(data[0]+2)] for _ in range(data[0]+2)]
        for i in range(1, data[0]+1):
            if chessboard[data[i]][i] == 1:
                print('NO')
                break
            else:
                chessboard[data[i]][i] = 1
                x, y = data[i], i
                while y >= 1 and x <= data[0]:
                    chessboard[x][y] = 1
                    y -= 1
                    x += 1
                x, y = data[i], i
                while y >= 1 and x >= 1:
                    chessboard[x][y] = 1
                    y -= 1
                    x -= 1
                x, y = data[i], i
                while y <= data[0] and x <= data[0]:
                    chessboard[x][y] = 1
                    y += 1
                    x += 1
                x, y = data[i], i
                while y <= data[0] and x >= 1:
                    chessboard[x][y] = 1
                    y += 1
                    x -= 1
        else:
            print('YES')
