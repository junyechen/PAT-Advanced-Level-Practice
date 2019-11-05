"""
Given a stack which can keep M numbers at most. Push N numbers in the order of 1, 2, 3, ..., N and pop randomly. You are supposed to tell if a given sequence of numbers is a possible pop sequence of the stack. For example, if M is 5 and N is 7, we can obtain 1, 2, 3, 4, 5, 6, 7 from the stack, but not 3, 2, 1, 7, 5, 6, 4.
Input Specification:

Each input file contains one test case. For each case, the first line contains 3 numbers (all no more than 1000): M (the maximum capacity of the stack), N (the length of push sequence), and K (the number of pop sequences to be checked). Then K lines follow, each contains a pop sequence of N numbers. All the numbers in a line are separated by a space.
Output Specification:

For each pop sequence, print in one line "YES" if it is indeed a possible pop sequence of the stack, or "NO" if not.
Sample Input:

5 7 5
1 2 3 4 5 6 7
3 2 1 7 5 6 4
7 6 5 4 3 2 1
5 6 4 3 7 2 1
1 7 6 5 4 3 2

Sample Output:

YES
NO
NO
YES
NO
"""
#######################################################
"""
一开始没搞清思路，导致做出的东西是错误的，后面重新更正了思路，本题考察模拟堆栈操作即可
从输出第一个数开始，分别为x，对于输出的每一个数，对应到队列出队数i
    若堆栈为空，则操作必定为将(i+1)~x压入堆栈，并将x弹出，队列出队数i=x
    若堆栈不为空
        若x>i，则操作必定为将(i+1)~x压入堆栈，并将x弹出，队列出队数i=x
        若x<i，则操作必定为将栈顶弹出，且弹出的栈顶应==x，否则不符合堆栈操作，报错
    
    突然发现上述堆栈为空与不空可以合并，不需要分开讨论，可以简化。
"""
#######################################################
m, n, k = map(int, input().split())
for _ in range(k):
    stack = []
    que = 0
    flag = True
    for ele in map(int, input().split()):
        if flag:
            if ele > que:
                stack += list(range(que + 1, ele))
                que = ele
            else:
                if stack.pop() != ele:
                    flag = False
            if len(stack) + 1 > m:
                flag = False
        else:
            break
    if flag:
        print("YES")
    else:
        print("NO")
#######################################################
"""
m, n, k = map(int, input().split())
for _ in range(k):
    stack = []
    que = 0
    flag = True
    for ele in map(int, input().split()):
        if flag:
            if stack:
                if ele > que:
                    stack += list(range(que + 1, ele))
                    que = ele
                else:
                    if stack.pop() != ele:
                        flag = False
                        break
            else:
                stack += list(range(que + 1, ele))
                que = ele
            if len(stack) + 1 > m:
                flag = False
                break
        else:
            break
    if flag:
        print("YES")
    else:
        print("NO")
"""
#######################################################
"""
m, n, k = map(int, input().split())
for _ in range(k):
    stack = []
    que = 0
    flag = True
    for ele in map(int, input().split()):
        if not flag:
            break
        if stack:
            while stack and ele > stack[-1]:
                if stack.pop() == que + 1:
                    que += 1
                else:
                    flag = False
                    break
        stack.append(ele)
        if len(stack) > m:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
"""
