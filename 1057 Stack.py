"""
Stack is one of the most fundamental data structures, which is based on the principle of Last In First Out (LIFO). The basic operations include Push (inserting an element onto the top position) and Pop (deleting the top element). Now you are supposed to implement a stack with an extra operation: PeekMedian -- return the median value of all the elements in the stack. With N elements, the median value is defined to be the (N/2)-th smallest element if N is even, or ((N+1)/2)-th if N is odd.
Input Specification:

Each input file contains one test case. For each case, the first line contains a positive integer N (≤10​5​​). Then N lines follow, each contains a command in one of the following 3 formats:

Push key
Pop
PeekMedian

where key is a positive integer no more than 10​5​​.
Output Specification:

For each Push command, insert key into the stack and output nothing. For each Pop or PeekMedian command, print in a line the corresponding returned value. If the command is invalid, print Invalid instead.
Sample Input:

17
Pop
PeekMedian
Push 3
PeekMedian
Push 2
PeekMedian
Push 1
PeekMedian
Pop
Pop
Push 5
Push 4
PeekMedian
Pop
Pop
Pop
Pop

Sample Output:

Invalid
Invalid
3
2
2
1
2
4
4
5
3
Invalid
"""

######################################################
"""
这题超出了我的基本能力，树状数组或者线段树什么的压根不清楚，看起来也是一头雾水，暂时先放弃了= =。。。
"""
######################################################

######################################################
"""
stack = []
for i in range(int(input())):
    command = input()
    if command == "Pop":
        if stack:
            print(stack.pop())
        else:
            print("Invalid")
    elif command == "PeekMedian":
        if stack:
            stack_ = stack.copy()
            stack_.sort()
            if len(stack_) % 2 == 0:
                print(stack_[len(stack_)//2-1])
            else:
                print(stack_[(len(stack_)+1)//2-1])
        else:
            print("Invalid")
    else:
        stack.append(int(command.split()[1]))
"""
######################################################
