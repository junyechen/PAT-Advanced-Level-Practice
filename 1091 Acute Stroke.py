"""
One important factor to identify acute stroke (急性脑卒中) is the volume of the stroke core. Given the results of image analysis in which the core regions are identified in each MRI slice, your job is to calculate the volume of the stroke core.
Input Specification:

Each input file contains one test case. For each case, the first line contains 4 positive integers: M, N, L and T, where M and N are the sizes of each slice (i.e. pixels of a slice are in an M×N matrix, and the maximum resolution is 1286 by 128); L (≤60) is the number of slices of a brain; and T is the integer threshold (i.e. if the volume of a connected core is less than T, then that core must not be counted).

Then L slices are given. Each slice is represented by an M×N matrix of 0's and 1's, where 1 represents a pixel of stroke, and 0 means normal. Since the thickness of a slice is a constant, we only have to count the number of 1's to obtain the volume. However, there might be several separated core regions in a brain, and only those with their volumes no less than T are counted. Two pixels are connected and hence belong to the same region if they share a common side, as shown by Figure 1 where all the 6 red pixels are connected to the blue one.

figstroke.jpg

Figure 1
Output Specification:

For each case, output in a line the total volume of the stroke core.

Sample Input:
3 4 5 2
1 1 1 1
1 1 1 1
1 1 1 1
0 0 1 1
0 0 1 1
0 0 1 1
1 0 1 1
0 1 0 0
0 0 0 0
1 0 1 1
0 0 0 0
0 0 0 0
0 0 0 1
0 0 0 1
1 0 0 0

Sample Output:
26
"""

##############################################################################
"""
理解题目花了很长时间，最后还不得不求助于网上已有的解答，才意识到，给的是三维堆叠的数据，最后要求的是三维无向量空间的连通分量
考虑到数据量应该很大，python采用递归的方式极有可能超时，故采用非递归的（借用队列）广度优先搜索
此外，为了排除边界的判断，将模型空间往外扩大了一圈

这里需注意python的列表赋值问题，之前了解到可以用list.copy()来解决list的赋值只赋给新list以单纯值，而非地址，然而本题中测试mark=pixel.copy()，仍发现对pixel修改，mark也会有相应的更改，搜索网上相关资料后发现， mark=pixel.copy()在python中仍是浅拷贝，对于列表里嵌套列表的，其拷贝给新列的仍是2层列表的地址，而非2层列表。

最后python仍然超时

对于第一个版本的方向搜索的“重复代码”，可以利用for + zip进行简化，注意需用‘()’来得到zip中的单个元组的分向量
"""
##############################################################################

M, N, L, T = map(int, input().split())
pixel = [[[0 for _ in range(N + 2)] for _ in range(M + 2)] for _ in range(L + 2)]
mark = [[[0 for _ in range(N + 2)] for _ in range(M + 2)] for _ in range(L + 2)]
for i in range(L):
    for j in range(M):
        pixel[i + 1][j + 1][1:N + 1] = map(int, input().split())
ans = 0
for i in range(1, L + 1):
    for j in range(1, M + 1):
        for k in range(1, N + 1):
            if pixel[i][j][k] == 1 and mark[i][j][k] == 0:
                seq = [[i, j, k]]
                mark[i][j][k] = 1
                volume = 1
                while seq:
                    temp = []
                    for child in seq:
                        ii, jj, kk = child
                        for (xi, yi, zi) in zip([1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, -1]):
                            if pixel[ii + xi][jj + yi][kk + zi] == 1 and mark[ii + xi][jj + yi][kk + zi] == 0:
                                temp.append([ii + xi, jj + yi, kk + zi])
                                mark[ii + xi][jj + yi][kk + zi] = 1
                                volume += 1
                    seq = temp
                if volume >= T:
                    ans += volume
print(ans)

'''
M, N, L, T = map(int, input().split())
pixel = [[[0 for _ in range(N+2)] for _ in range(M+2)] for _ in range(L+2)]
mark = [[[0 for _ in range(N+2)] for _ in range(M+2)] for _ in range(L+2)]
for i in range(L):
    for j in range(M):
        pixel[i+1][j+1][1:N+1] = map(int, input().split())
ans = 0
for i in range(1, L+1):
    for j in range(1, M+1):
        for k in range(1, N+1):
            if pixel[i][j][k] == 1 and mark[i][j][k] == 0:
                seq = [[i, j, k]]
                mark[i][j][k] = 1
                volume = 1
                while seq:
                    temp = []
                    for child in seq:
                        ii, jj, kk = child
                        if pixel[ii+1][jj][kk] == 1 and mark[ii+1][jj][kk] == 0:
                            temp.append([ii+1, jj, kk])
                            mark[ii+1][jj][kk] = 1
                            volume += 1
                        if pixel[ii-1][jj][kk] == 1 and mark[ii-1][jj][kk] == 0:
                            temp.append([ii-1, jj, kk])
                            mark[ii-1][jj][kk] = 1
                            volume += 1
                        if pixel[ii][jj+1][kk] == 1 and mark[ii][jj+1][kk] == 0:
                            temp.append([ii, jj+1, kk])
                            mark[ii][jj+1][kk] = 1
                            volume += 1
                        if pixel[ii][jj-1][kk] == 1 and mark[ii][jj-1][kk] == 0:
                            temp.append([ii, jj-1, kk])
                            mark[ii][jj-1][kk] = 1
                            volume += 1
                        if pixel[ii][jj][kk+1] == 1 and mark[ii][jj][kk+1] == 0:
                            temp.append([ii, jj, kk+1])
                            mark[ii][jj][kk+1] = 1
                            volume += 1
                        if pixel[ii][jj][kk-1] == 1 and mark[ii][jj][kk-1] == 0:
                            temp.append([ii, jj, kk-1])
                            mark[ii][jj][kk-1] = 1
                            volume += 1
                    seq = temp
                if volume >= T:
                    ans += volume
print(ans)
'''
