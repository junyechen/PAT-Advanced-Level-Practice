"""
Weibo is known as the Chinese version of Twitter. One user on Weibo may have many followers, and may follow many other users as well. Hence a social network is formed with followers relations. When a user makes a post on Weibo, all his/her followers can view and forward his/her post, which can then be forwarded again by their followers. Now given a social network, you are supposed to calculate the maximum potential amount of forwards for any specific user, assuming that only L levels of indirect followers are counted.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers: N (≤1000), the number of users; and L (≤6), the number of levels of indirect followers that are counted. Hence it is assumed that all the users are numbered from 1 to N. Then N lines follow, each in the format:

M[i] user_list[i]

where M[i] (≤100) is the total number of people that user[i] follows; and user_list[i] is a list of the M[i] users that followed by user[i]. It is guaranteed that no one can follow oneself. All the numbers are separated by a space.

Then finally a positive K is given, followed by K UserID's for query.
Output Specification:

For each UserID, you are supposed to print in one line the maximum potential amount of forwards this user can trigger, assuming that everyone who can view the initial post will forward it once, and that only L levels of indirect followers are counted.
Sample Input:

7 3
3 2 3 4
0
2 5 6
2 3 1
2 3 4
1 4
1 5
2 2 6

Sample Output:

4
5
"""

############################################
"""
本题题目较为简单，但是python仍有一个点超时

可采取广度优先搜索遍历

但我采用的是深度优先搜索遍历，对于访问过的节点不加摘选，统一放入访问池中，最后对访问池进行集合化去重操作
因为有可能会重新访问到根节点，根节点自身不能作为计数成员，故在最后排除
"""
############################################


def bfs(root, level):
    global N, L, relation, res
    if level == L:
        return
    else:
        for ii in range(1, N+1):
            if relation[root][ii] == 1:
                res.append(ii)
                bfs(ii, level+1)


N, L = map(int, input().split())
relation = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    if len(data) == 1:
        continue
    else:
        for j in data[1:]:
            relation[j][i] = 1
request = list(map(int, input().split()))
for i in request[1:]:
    res = []
    bfs(i, 0)
    res = set(res)
    if i in res:
        print(len(res)-1)
    else:
        print(len(res))
