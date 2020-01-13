"""
According to Wikipedia:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. Each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

Merge sort works as follows: Divide the unsorted list into N sublists, each containing 1 element (a list of 1 element is considered sorted). Then repeatedly merge two adjacent sublists to produce new sorted sublists until there is only 1 sublist remaining.

Now given the initial sequence of integers, together with a sequence which is a result of several iterations of some sorting method, can you tell which sorting method we are using?
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤100). Then in the next line, N integers are given as the initial sequence. The last line contains the partially sorted sequence of the N numbers. It is assumed that the target sequence is always ascending. All the numbers in a line are separated by a space.
Output Specification:

For each test case, print in the first line either "Insertion Sort" or "Merge Sort" to indicate the method used to obtain the partial result. Then run this method for one more iteration and output in the second line the resuling sequence. It is guaranteed that the answer is unique for each test case. All the numbers in a line must be separated by a space, and there must be no extra space at the end of the line.
Sample Input 1:
10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

Sample Output 1:
Insertion Sort
1 2 3 5 7 8 9 4 6 0

Sample Input 2:
10
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6

Sample Output 2:
Merge Sort
1 2 3 8 4 5 7 9 0 6
"""

################################################
"""
不需要重新实现算法，只要知道原理，用系统的sort解决就可以
对于插入排序，只要满足前m个数字是从小到大排列，后面的数字与原序列相同，则表明为插入排序，反之为归并排序
归并排序为2、4、8、16，2倍数分组下去，注意排在后面未成满组的，仍需进行排序
"""
################################################

n = int(input())
first = list(map(int, input().split()))
last = list(map(int, input().split()))
i = 1
while last[i-1] <= last[i] and i < len(last):
    i += 1
if sorted(first[0:i]) == last[0:i] and first[i:] == last[i:]:
    print("Insertion Sort")
    print(' '.join(map(str, sorted(last[0:i+1])+first[i+1:])))
else:
    print("Merge Sort")
    i = 2
    flag = False
    while True:
        for j in range(i-1, len(last), i):
            first[j-i+1:j+1] = sorted(first[j-i+1:j+1])
        if j != len(last) - 1:
            first[j + 1:] = sorted(first[j + 1:])
        if flag:
            break
        if first == last:
            flag = True
        i = i * 2
    print(' '.join(map(str, first)))


'''
n = int(input())
first = list(map(int, input().split()))
last = list(map(int, input().split()))
i = 1
while last[i-1] <= last[i] and i < len(last):
    i += 1
if sorted(first[0:i]) == last[0:i] and first[i:] == last[i:]:
    print("Insertion Sort")
    print(' '.join(map(str, sorted(last[0:i+1])+first[i+1:])))
else:
    print("Merge Sort")
    i = 2
    flag = False
    while i*2 <= len(last):
        for j in range(i-1, len(last), i):
            first[j-i+1:j+1] = sorted(first[j-i+1:j+1])
        if j != len(last) - 1:
            first[j + 1:] = sorted(first[j + 1:])
        if flag:
            break
        if first == last:
            flag = True
        i = i * 2
    print(' '.join(map(str, first)))
'''

'''
n = int(input())
first = list(map(int, input().split()))
last = list(map(int, input().split()))
i = 1
while last[i-1] <= last[i] and i < len(last):
    i += 1
if sorted(first[0:i]) == last[0:i] and first[i:] == last[i:]:
    print("Insertion Sort")
    print(' '.join(map(str, sorted(last[0:i+1])+first[i+1:])))
else:
    print("Merge Sort")
    i = 2
    flag = False
    while i*2 <= len(last):
        for j in range(i-1, len(last), i):
            temp = []
            temp1 = first[j-i+1:j-i//2+1]
            temp2 = first[j-i//2+1:j+1]
            p, q = 0, 0
            while p != i//2 or q != i//2:
                if p == i//2:
                    temp.append(temp2[q])
                    q += 1
                elif q == i//2:
                    temp.append(temp1[p])
                    p += 1
                else:
                    if temp1[p] < temp2[q]:
                        temp.append(temp1[p])
                        p += 1
                    else:
                        temp.append(temp2[q])
                        q += 1
            first[j-i+1:j+1] = temp
        if j != len(last)-1:
            first[j+1:] = sorted(first[j+1:])
        if flag:
            break
        if first == last:
            flag = True
        i = i * 2
    print(' '.join(map(str, first)))
'''
