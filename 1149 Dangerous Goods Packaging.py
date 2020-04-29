"""
When shipping goods with containers, we have to be careful not to pack some incompatible goods into the same container, or we might get ourselves in serious trouble. For example, oxidizing agent （氧化剂） must not be packed with flammable liquid （易燃液体）, or it can cause explosion.

Now you are given a long list of incompatible goods, and several lists of goods to be shipped. You are supposed to tell if all the goods in a list can be packed into the same container.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers: N (≤10​4​​), the number of pairs of incompatible goods, and M (≤100), the number of lists of goods to be shipped.

Then two blocks follow. The first block contains N pairs of incompatible goods, each pair occupies a line; and the second one contains M lists of goods to be shipped, each list occupies a line in the following format:

K G[1] G[2] ... G[K]

where K (≤1,000) is the number of goods and G[i]'s are the IDs of the goods. To make it simple, each good is represented by a 5-digit ID number. All the numbers in a line are separated by spaces.
Output Specification:

For each shipping list, print in a line Yes if there are no incompatible goods in the list, or No if not.
Sample Input:

6 3
20001 20002
20003 20004
20005 20006
20003 20001
20005 20004
20004 20006
4 00001 20004 00002 20003
5 98823 20002 20003 20006 10010
3 12345 67890 23333

Sample Output:

No
Yes
Yes
"""

###################################################
"""
和别人思路不一样，导致时间过长而未过
我的思路是将比对清单一一与货物清单进行比较，是否为货物清单的子集，如果是，则表明有问题，但这样超时
别人的思路是，遍历货物清单，对每个货物的不相容货物检索判定是否在货物清单里
"""
###################################################

n, m = map(int, input().split())
incompatible = [set() for _ in range(100000)]
for _ in range(n):
    a, b = map(int, input().split())
    incompatible[a].add(b)
    incompatible[b].add(a)
for _ in range(m):
    goods = list(map(int, input().split()))[1:]
    for a in goods:
        for b in incompatible[a]:
            if b in goods:
                print('No')
                break
        else:
            continue
        break
    else:
        print('Yes')

    # for i in range(len(goods)-1):
    #     for j in range(i, len(goods)):
    #         if goods[i] in incompatible[goods[j]]:
    #             print('No')
    #             break
    #     else:
    #         continue
    #     break
    # else:
    #     print('Yes')

#####################################################################
"""
n, m = map(int, input().split())
incompatible = []
for _ in range(n):
    incompatible.append(set(list(map(int, input().split()))))
for _ in range(m):
    goods = set(list(map(int, input().split()))[1:])
    for i in range(n):
        if incompatible[i].issubset(goods):
            print('No')
            break
    else:
        print('Yes')
"""
#####################################################################
