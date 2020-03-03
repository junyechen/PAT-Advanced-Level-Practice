"""
"Damn Single (单身狗)" is the Chinese nickname for someone who is being single. You are supposed to find those who are alone in a big party, so they can be taken care of.
Input Specification:

Each input file contains one test case. For each case, the first line gives a positive integer N (≤ 50,000), the total number of couples. Then N lines of the couples follow, each gives a couple of ID's which are 5-digit numbers (i.e. from 00000 to 99999). After the list of couples, there is a positive integer M (≤ 10,000) followed by M ID's of the party guests. The numbers are separated by spaces. It is guaranteed that nobody is having bigamous marriage (重婚) or dangling with more than one companion.
Output Specification:

First print in a line the total number of lonely guests. Then in the next line, print their ID's in increasing order. The numbers must be separated by exactly 1 space, and there must be no extra space at the end of the line.
Sample Input:

3
11111 22222
33333 44444
55555 66666
7
55555 44444 10000 88888 22222 11111 23333

Sample Output:

5
10000 23333 44444 55555 88888
"""


###################################################################
"""
相对来说简单，建立夫妻关系表，建立宾客登记表，然后匹配宾客登记里另一个是否登记，没有登记则表明该为单身狗。

python运行速度不稳定，可能最后2个测试点不能通过，但多试几次有时候又可以！
"""
###################################################################


def main():
    couple = [-1] * 100000
    for _ in range(int(input())):
        a, b = map(int, input().split())
        couple[a] = b
        couple[b] = a
    input()
    guests = list(map(int, input().split()))
    guest_reg = [0] * 100000
    damn_single = []
    for guest in guests:
        guest_reg[guest] = 1
    for guest in guests:
        if couple[guest] == -1:
            damn_single.append(guest)
        elif guest_reg[couple[guest]] != 1:
            damn_single.append(guest)
    damn_single.sort()
    print(len(damn_single))
    if len(damn_single) > 0:
        print(' '.join(['%05d' % x for x in damn_single]))


if __name__ == '__main__':
    main()
