"""
In computer science, a heap is a specialized tree-based data structure that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C. A common implementation of a heap is the binary heap, in which the tree is a complete binary tree. (Quoted from Wikipedia at https://en.wikipedia.org/wiki/Heap_(data_structure))

Your job is to tell if a given complete binary tree is a heap.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers: M (≤ 100), the number of trees to be tested; and N (1 < N ≤ 1,000), the number of keys in each tree, respectively. Then M lines follow, each contains N distinct integer keys (all in the range of int), which gives the level order traversal sequence of a complete binary tree.
Output Specification:

For each given tree, print in a line Max Heap if it is a max heap, or Min Heap for a min heap, or Not Heap if it is not a heap at all. Then in the next line print the tree's postorder traversal sequence. All the numbers are separated by a space, and there must no extra space at the beginning or the end of the line.
Sample Input:

3 8
98 72 86 60 65 12 23 50
8 38 25 58 52 82 70 60
10 28 15 12 34 9 8 56

Sample Output:

Max Heap
50 60 65 72 12 23 86 98
Min Heap
60 58 52 38 82 70 25 8
Not Heap
56 12 34 28 9 8 15 10
"""

#####################################################
"""
python存在超时，有几率通过

重新回顾堆的定义，利用数组与完全二叉树的性质，避免建树
"""
#####################################################


def get_post_order(root):
    global n, heap, post_order
    if root >= n:
        return
    else:
        get_post_order(root * 2 + 1)
        get_post_order(2 * (root + 1))
        post_order.append(heap[root])


m, n = map(int, input().split())
for _ in range(m):
    heap = list(map(int, input().split()))
    if heap[0] > heap[1]:
        heap_property = 1  # max_heap
    else:
        heap_property = -1  # min_heap
    for i in range(n):
        left = i * 2 + 1
        right = 2 * (i + 1)
        if left >= n:
            break
        else:
            if heap[i] > heap[left] and heap_property == 1 or heap[i] < heap[left] and heap_property == -1:
                pass
            else:
                heap_property = 0
                break
        if right >= n:
            break
        else:
            if heap[i] > heap[right] and heap_property == 1 or heap[i] < heap[right] and heap_property == -1:
                pass
            else:
                heap_property = 0
                break
    if heap_property == 0:
        print('Not Heap')
    elif heap_property == 1:
        print('Max Heap')
    else:
        print('Min Heap')
    post_order = []
    get_post_order(0)
    print(*post_order)
