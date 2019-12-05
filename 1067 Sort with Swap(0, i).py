"""
Given any permutation of the numbers {0, 1, 2,..., N−1}, it is easy to sort them in increasing order. But what if Swap(0, *) is the ONLY operation that is allowed to use? For example, to sort {4, 0, 2, 1, 3} we may apply the swap operations in the following way:

Swap(0, 1) => {4, 1, 2, 0, 3}
Swap(0, 3) => {4, 1, 2, 3, 0}
Swap(0, 4) => {0, 1, 2, 3, 4}

Now you are asked to find the minimum number of swaps need to sort the given permutation of the first N nonnegative integers.
Input Specification:

Each input file contains one test case, which gives a positive N (≤10​5​​) followed by a permutation sequence of {0, 1, ..., N−1}. All the numbers in a line are separated by a space.
Output Specification:

For each case, simply print in a line the minimum number of swaps need to sort the given permutation.
Sample Input:

10
3 5 7 2 6 4 9 0 8 1

Sample Output:

9
"""

##########################################
"""
本题测试数据有问题，输入只有1行，而非2行
本题题目为找圈子，即选定某个位置的数，纳入圈子，以其为始，找到该数对应位置的数，纳入圈子，依次纳入，直到回到起始。
假设圈子里有m个数，因为题目要求只能和0交换，故圈子中如果有0，则次数减少1次，因为圈子里首先和0调换位置，为m-1次；
    如果圈子中没有0，则次数增加1次，因为必须要有一个数和0交换，将0调入圈子，完成相应位置后，最后与0调回来，为m+1次

以题目例子为例：
例1：4 0 2 1 3：
    从位置0开始，将4纳入圈子；位置4的3纳入圈子；位置3的1纳入圈子；位置1的0纳入圈子 -- 构成1个圈子
    剩下2没有纳入圈子，但是2原本就在其位置上
    
    故例子中只有1个圈子，圈子里有4个数，圈子中包括0，故至少需交换3次

例2:3 5 7 2 6 4 9 0 8 1
    从位置0开始，将3纳入圈子；位置3的2纳入圈子；位置2的7纳入圈子；位置7的0纳入圈子 -- 构成1个圈子
    从位置1开始，将5纳入圈子；位置5的4纳入圈子；位置4的6纳入圈子；位置6的9纳入圈子；位置9的1纳入圈子 -- 构成1个圈子
    剩下8在原位
    
    故例子中有2个圈子，1个圈子包含0,4个数，至少交换3次；1个圈子不包含0,5个数，至少交换6次；
        故总至少交换9次
"""
##########################################

# n = int(input())
line = list(map(int, input().split()))
line.pop(0)
n = len(line)
mark = [0] * n
res = 0
for i in range(n):
    x = line[i]
    if x == i:
        mark[x] = 1
    elif mark[x] == 0:
        while mark[x] == 0:
            if x == 0:
                res -= 2
            mark[x] = 1
            x = line[x]
            res += 1
        res += 1
print(res)
