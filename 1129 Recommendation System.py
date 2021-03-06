"""
Recommendation system predicts the preference that a user would give to an item. Now you are asked to program a very simple recommendation system that rates the user's preference by the number of times that an item has been accessed by this user.
Input Specification:

Each input file contains one test case. For each test case, the first line contains two positive integers: N (≤ 50,000), the total number of queries, and K (≤ 10), the maximum number of recommendations the system must show to the user. Then given in the second line are the indices of items that the user is accessing -- for the sake of simplicity, all the items are indexed from 1 to N. All the numbers in a line are separated by a space.
Output Specification:

For each case, process the queries one by one. Output the recommendations for each query in a line in the format:

query: rec[1] rec[2] ... rec[K]

where query is the item that the user is accessing, and rec[i] (i=1, ... K) is the i-th item that the system recommends to the user. The first K items that have been accessed most frequently are supposed to be recommended in non-increasing order of their frequencies. If there is a tie, the items will be ordered by their indices in increasing order.

Note: there is no output for the first item since it is impossible to give any recommendation at the time. It is guaranteed to have the output for at least one query.
Sample Input:

12 3
3 5 7 5 5 3 2 1 8 3 8 12

Sample Output:

5: 3
7: 3 5
5: 3 5 7
5: 5 3 7
3: 5 3 7
2: 5 3 7
1: 5 3 2
8: 5 3 1
3: 5 3 1
8: 3 5 1
12: 3 5 8
"""

#########################################################################
"""
题目
    输入第一行用户数n以及最多推荐的个数k
    输入第二行为产品查询次序
    
    每当输入一个产品查询时，推荐之前查询过产品最多的k个产品，若出现查询次数相同的情况，输出最小的查询号产品
    
最暴力的做法就是将每个产品的次数依次叠加，然后排序，按输出要求输出即可，但会超时，因此不对所有产品进行排序，而是对推荐的个数进行排序，这样有助于减少排序上的时间开支
但是这个版本勉勉强强，接近时间上限通过
"""
#########################################################################

if __name__ == '__main__':
    n, k = map(int, input().split())
    queries = list(map(int, input().split()))
    rec_full = [0] * (n + 1)
    rec_full[queries[0]] = 1
    rec_no = [queries[0]]
    for i in range(1, n):
        print('%d: %s' % (queries[i], ' '.join(map(str, rec_no))))
        rec_full[queries[i]] += 1
        if queries[i] in rec_no:
            rec_no.sort(key=lambda x: (rec_full[x], -x), reverse=True)
        else:
            rec_no.append(queries[i])
            rec_no.sort(key=lambda x: (rec_full[x], -x), reverse=True)
        if len(rec_no) > k:
            rec_no = rec_no[:k]
