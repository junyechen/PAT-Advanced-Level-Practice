"""
There is a classical process named partition in the famous quick sort algorithm. In this process we typically choose one element as the pivot. Then the elements less than the pivot are moved to its left and those larger than the pivot to its right. Given N distinct positive integers after a run of partition, could you tell how many elements could be the selected pivot for this partition?

For example, given N=5 and the numbers 1, 3, 2, 4, and 5. We have:

    1 could be the pivot since there is no element to its left and all the elements to its right are larger than it;
    3 must not be the pivot since although all the elements to its left are smaller, the number 2 to its right is less than it as well;
    2 must not be the pivot since although all the elements to its right are larger, the number 3 to its left is larger than it as well;
    and for the similar reason, 4 and 5 could also be the pivot.

Hence in total there are 3 pivot candidates.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤10​5​​). Then the next line contains N distinct positive integers no larger than 10​9​​. The numbers in a line are separated by spaces.
Output Specification:

For each test case, output in the first line the number of pivot candidates. Then in the next line print these candidates in increasing order. There must be exactly 1 space between two adjacent numbers, and no extra space at the end of each line.
Sample Input:

5
1 3 2 4 5

Sample Output:

3
1 4 5
"""

###########################################
"""
直接使用暴力，与左边最大，右边最小比较，必然会超时
    一开始采用两趟算法，先从左往右得到比左边大的序列，再从右往左得到比右边小的序列，两个序列合并即为所求的序列，但仍有超时

之后查看网上的教程，可以对原数据直接排序，如果排序后序列的数据位置不变，且该数据比左边序列大，则表明该数据为pivot元素：
    因为给的数据大小不等，所以在原序列中若该数比左边序列都大，比右边序列都小，则该数据的位置必然等同于排序后序列的位置，反证法可证的
    但若只通过位置不变，则很有可能左边序列中有大于该数（右边序列中有小于该数）的情况，故除了判断位置相等，还需判断该数是否大于原序列的左边序列
"""
###########################################

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(data)
left_biggest = -1
res = []
for i in range(n):
    if data[i] > left_biggest:
        left_biggest = data[i]
        if data[i] == sorted_data[i]:
            res.append(data[i])
print(len(res))
print(' '.join(map(str, res)))


"""
n = int(input())
data = list(map(int, input().split()))
left_biggest = -1
left_right = []
for i in range(n):
    if left_biggest < data[i]:
        left_right.append(i)
        left_biggest = data[i]
right_smallest = 1000000000
right_left = []
for i in range(n-1, -1, -1):
    if right_smallest > data[i]:
        right_left.append(i)
        right_smallest = data[i]
res = []
for i in left_right:
    if i in right_left:
        res.append(data[i])
print(len(res))
print(' '.join(map(str, res)))
"""
