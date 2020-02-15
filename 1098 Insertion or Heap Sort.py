"""
According to Wikipedia:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. Each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

Heap sort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region. it involves the use of a heap data structure rather than a linear-time search to find the maximum.

Now given the initial sequence of integers, together with a sequence which is a result of several iterations of some sorting method, can you tell which sorting method we are using?
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤100). Then in the next line, N integers are given as the initial sequence. The last line contains the partially sorted sequence of the N numbers. It is assumed that the target sequence is always ascending. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in the first line either "Insertion Sort" or "Heap Sort" to indicate the method used to obtain the partial result. Then run this method for one more iteration and output in the second line the resulting sequence. It is guaranteed that the answer is unique for each test case. All the numbers in a line must be separated by a space, and there must be no extra space at the end of the line.
Sample Input 1:

10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

Sample Output 1:

Insertion Sort
1 2 3 5 7 8 9 4 6 0

Sample Input 2:

10
3 1 2 8 7 5 9 4 6 0
6 4 5 1 0 3 2 7 8 9

Sample Output 2:

Heap Sort
5 4 3 1 0 2 6 7 8 9
"""

##############################################
"""
本题主要考查堆排序(heap sort)的原理

对于前面的插入排序，根据算法，前a个为从小到大的有序数列，之后的序列应与原序列一致；
    故下一级算法序列，只需将前a个有序数列扩增1个数后进行排序，连接后面的序列(n-a-1)即可
对于后面的堆排序，根据算法，后b个为从小到大的有序数列，前面的序列为大堆顶，且堆顶的数为前序列的最大值
    故下一级算法序列为，将第一个数与后b个有序数列的前一个数交换，并再次对前面的序列(n-b-1)作大堆顶操作即可
"""
##############################################


def swap(r, a, b):
    temp = r[a]
    r[a] = r[b]
    r[b] = temp


n = int(input())
origin = list(map(int, input().split()))
sort = list(map(int, input().split()))
for i in range(n-1):
    if sort[i] > sort[i+1]:
        break
if origin[i+1:] == sort[i+1:]:
    print("Insertion Sort")
    res = sorted(sort[:i+2]) + sort[i+2:]
    print(' '.join(map(str, res)))
else:
    print("Heap Sort")
    for i in range(n-1,0,-1):
        if sort[0] > sort[i]:
            break
    res = sort.copy()
    swap(res, 0, i)
    last_parent = (i-2)//2
    p = i-1
    for i in range(last_parent+1):
        left_child = i*2+1
        right_child = left_child+1
        if right_child > p:
            if res[i]<res[left_child]:
                swap(res, i, left_child)
        else:
            max_index = i
            if res[left_child] > res[max_index]:
                max_index = left_child
            if res[right_child] > res[max_index]:
                max_index = right_child
            if max_index != i:
                swap(res, i, max_index)
    print(' '.join(map(str, res)))


"""
    heap = origin.copy()
    flag = False
    while True:
        last_parent = ((n-1)-1)//2
        for i in range(last_parent, -1, -1):
            if i*2+2 == n:
                left_child = i*2+1
                if heap[left_child] > heap[i]:
                    temp = heap[left_child]
                    heap[left_child] = heap[i]
                    heap[i] = temp
            else:
                left_child = i*2+1
                right_child = i*2+2
                max_index = i
                if heap[left_child]>heap[max_index]:
                    max_index = left_child
                if heap[right_child]>heap[max_index]:
                    max_index = right_child
                if max_index != i:
                    temp = heap[max_index]
                    heap[max_index] = heap[i]
                    heap[i] = temp
        tmep = heap[0]
        heap[0] = heap[n-1]
        heap[n-1] = temp
        if flag:
            break
        if heap == sort:
            flag = True
        n -= 1
    print(' '.join(map(str, heap)))
"""
