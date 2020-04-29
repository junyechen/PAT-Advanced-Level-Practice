"""
The "travelling salesman problem" asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science. (Quoted from "https://en.wikipedia.org/wiki/Travelling_salesman_problem".)

In this problem, you are supposed to find, from a given list of cycles, the one that is the closest to the solution of a travelling salesman problem.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive integers N (2<N≤200), the number of cities, and M, the number of edges in an undirected graph. Then M lines follow, each describes an edge in the format City1 City2 Dist, where the cities are numbered from 1 to N and the distance Dist is positive and is no more than 100. The next line gives a positive integer K which is the number of paths, followed by K lines of paths, each in the format:

n C​1​​ C​2​​ ... C​n​​

where n is the number of cities in the list, and C​i​​'s are the cities on a path.
Output Specification:

For each path, print in a line Path X: TotalDist (Description) where X is the index (starting from 1) of that path, TotalDist its total distance (if this distance does not exist, output NA instead), and Description is one of the following:

    TS simple cycle if it is a simple cycle that visits every city;
    TS cycle if it is a cycle that visits every city, but not a simple cycle;
    Not a TS cycle if it is NOT a cycle that visits every city.

Finally print in a line Shortest Dist(X) = TotalDist where X is the index of the cycle that is the closest to the solution of a travelling salesman problem, and TotalDist is its total distance. It is guaranteed that such a solution is unique.
Sample Input:

6 10
6 2 1
3 4 1
1 5 1
2 5 1
3 1 8
4 1 6
1 6 1
6 3 1
1 2 1
4 5 1
7
7 5 1 4 3 6 2 5
7 6 1 3 4 5 2 6
6 5 1 4 3 6 2
9 6 2 1 6 3 4 5 2 6
4 1 2 5 1
7 6 1 2 5 4 3 1
7 6 3 2 5 4 1 6

Sample Output:

Path 1: 11 (TS simple cycle)
Path 2: 13 (TS simple cycle)
Path 3: 10 (Not a TS cycle)
Path 4: 8 (TS cycle)
Path 5: 3 (Not a TS cycle)
Path 6: 13 (Not a TS cycle)
Path 7: NA (Not a TS cycle)
Shortest Dist(4) = 8
"""

###############################################################
"""
python超时无法解决

查看网上的两个python AC的解，提交他们的代码，也超时，可能题目的时间限制有修改
"""
###############################################################

n, m = map(int, input().split())
road = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, dis = map(int, input().split())
    road[a][b] = road[b][a] = dis
small_dis = 100000000
small_dis_index = 0
for i in range(int(input())):
    routine = list(map(int, input().split()))
    city_num = routine[0]
    routine = routine[1:]
    dis = 0
    for j in range(city_num-1):
        dis_temp = road[routine[j]][routine[j+1]]
        if dis_temp == 0:
            print('Path %d: NA (Not a TS cycle)' % (i+1))
            break
        else:
            dis += dis_temp
    else:
        if len(set(routine)) == n:
            if routine[0] == routine[-1]:
                if city_num == n + 1:
                    print('Path %d: %d (TS simple cycle)' % (i+1, dis))
                else:
                    print('Path %d: %d (TS cycle)' % (i+1, dis))
                if dis < small_dis:
                    small_dis = dis
                    small_dis_index = i+1
            else:
                print('Path %d: %d (Not a TS cycle)' % (i + 1, dis))
        else:
            print('Path %d: %d (Not a TS cycle)' % (i+1, dis))
print('Shortest Dist(%d) = %d' % (small_dis_index, small_dis))
