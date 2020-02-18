"""
When register on a social network, you are always asked to specify your hobbies in order to find some potential friends with the same hobbies. A social cluster is a set of people who have some of their hobbies in common. You are supposed to find all the clusters.
Input Specification:

Each input file contains one test case. For each test case, the first line contains a positive integer N (≤1000), the total number of people in a social network. Hence the people are numbered from 1 to N. Then N lines follow, each gives the hobby list of a person in the format:

K​i​​: h​i​​[1] h​i​​[2] ... h​i​​[K​i​​]

where K​i​​ (>0) is the number of hobbies, and h​i​​[j] is the index of the j-th hobby, which is an integer in [1, 1000].
Output Specification:

For each case, print in one line the total number of clusters in the network. Then in the second line, print the numbers of people in the clusters in non-increasing order. The numbers must be separated by exactly one space, and there must be no extra space at the end of the line.
Sample Input:

8
3: 2 7 10
1: 4
2: 5 3
1: 4
1: 3
1: 4
4: 6 8 1 5
1: 4

Sample Output:

3
4 3 1
"""


###################################################
"""
这题做的非常累，查阅之后属于并查集问题，但还是不会做，再仔细思考网上使用并查集的思路后，采用如下算法：
    1. 将输入的数据转换为“爱好-人”的字典集，这样符合每个爱好下面的人都是一群人
    2. 在初始化时，设定每个人的上级（father）都是自己，因此每个上级的集合都是1个人（child）
    3. 对应每个爱好，如果1个爱好下属的人数只有1个人，则不进行操作
        若下属超过1个人，表明通过该爱好，这个爱好下的人应组为1个集合
    4. 设定超过1个人的爱好里，第一个爱好的祖先为这个爱好的祖先，此后，对于该爱好下的其他人，判断他们的祖先是否是同一个祖先，如果不是同一个祖先，则将后祖先重新编入先祖先，并将后祖先所属的孩子全部划归先祖先，删除后祖先的孩子
        判断是否是祖先：自身编号与祖先一致即说明此为祖先本人

一开始始终有两个测试点不过，后来发现是回溯祖先时没有回溯到头造成了错代的数据问题
"""
###################################################


class Cluster:
    def __init__(self, index):
        self.father = index
        self.child = 1


n = int(input())
cluster = [Cluster(_) for _ in range(n)]
hobby = {}
for people in range(n):
    data = input().split()
    hobbies = list(map(int, data[1:]))
    for h in hobbies:
        if h in hobby:
            hobby[h].append(people)
        else:
            hobby[h] = [people]
for hobbies, people in hobby.items():
    if len(people) != 1:
        father = cluster[people[0]].father
        while cluster[father].father != father:
            father = cluster[father].father
        for person in people[1:]:
            if cluster[person].father != father:
                while cluster[person].father != person:
                    person = cluster[person].father
                cluster[person].father = father
                cluster[father].child += cluster[person].child
                cluster[person].child = 0
social_cluster = []
for c in cluster:
    if c.child != 0:
        social_cluster.append(c.child)
print(len(social_cluster))
print(' '.join(map(str, sorted(social_cluster, reverse=True))))


"""
class Cluster:
    def __init__(self, index):
        self.father = index
        self.mark = index
        self.child = 1


n = int(input())
cluster = [Cluster(_) for _ in range(n)]
hobby = {}
for people in range(n):
    data = input().split()
    hobbies = list(map(int, data[1:]))
    for h in hobbies:
        if h in hobby:
            hobby[h].append(people)
        else:
            hobby[h] = [people]
for hobbies, people in hobby.items():
    if len(people) != 1:
        father = cluster[people[0]].father
        for person in people[1:]:
            if cluster[person].father != father:
                origin_father = cluster[person].father
                cluster[person].father = father
                cluster[origin_father].father = father
social_cluster = {}
for person in cluster:
    while person.father != person.mark:
        person = cluster[person.father]
    if person in social_cluster:
        social_cluster[person] += 1
    else:
        social_cluster[person] = 1
print(len(social_cluster))
print(' '.join(map(str, sorted([value for key, value in social_cluster.items()], reverse=True))))
"""

"""
class Cluster:
    def __init__(self, index):
        self.father = index
        self.child = 1


n = int(input())
cluster = [Cluster(_) for _ in range(n)]
hobby = {}
for people in range(n):
    data = input().split()
    hobbies = list(map(int, data[1:]))
    for h in hobbies:
        if h in hobby:
            hobby[h].append(people)
        else:
            hobby[h] = [people]
for hobbies, people in hobby.items():
    if len(people) != 1:
        father = cluster[people[0]].father
        for person in people[1:]:
            if cluster[person].father != father:
                origin_father = cluster[person].father
                cluster[person].father = father
                cluster[origin_father].father = father
                cluster[father].child += cluster[origin_father].child
                cluster[person].child = 0
                cluster[origin_father].child = 0
social_cluster = []
for c in cluster:
    if c.child != 0:
        social_cluster.append(c.child)
print(len(social_cluster))
print(' '.join(map(str, sorted(social_cluster, reverse=True))))
"""
