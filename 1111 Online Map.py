"""
Input our current position and a destination, an online map can recommend several paths. Now your job is to recommend two paths to your user: one is the shortest, and the other is the fastest. It is guaranteed that a path exists for any request.
Input Specification:

Each input file contains one test case. For each case, the first line gives two positive integers N (2≤N≤500), and M, being the total number of streets intersections on a map, and the number of streets, respectively. Then M lines follow, each describes a street in the format:

V1 V2 one-way length time

where V1 and V2 are the indices (from 0 to N−1) of the two ends of the street; one-way is 1 if the street is one-way from V1 to V2, or 0 if not; length is the length of the street; and time is the time taken to pass the street.

Finally a pair of source and destination is given.
Output Specification:

For each case, first print the shortest path from the source to the destination with distance D in the format:

Distance = D: source -> v1 -> ... -> destination


Then in the next line print the fastest path with total time T:

Time = T: source -> w1 -> ... -> destination

In case the shortest path is not unique, output the fastest one among the shortest paths, which is guaranteed to be unique. In case the fastest path is not unique, output the one that passes through the fewest intersections, which is guaranteed to be unique.

In case the shortest and the fastest paths are identical, print them in one line in the format:

Distance = D; Time = T: source -> u1 -> ... -> destination

Sample Input 1:

10 15
0 1 0 1 1
8 0 0 1 1
4 8 1 1 1
3 4 0 3 2
3 9 1 4 1
0 6 0 1 1
7 5 1 2 1
8 5 1 2 1
2 3 0 2 2
2 1 1 1 1
1 3 0 3 1
1 4 0 1 1
9 7 1 3 1
5 1 0 5 2
6 5 1 1 2
3 5

Sample Output 1:

Distance = 6: 3 -> 4 -> 8 -> 5
Time = 3: 3 -> 1 -> 5

Sample Input 2:

7 9
0 4 1 1 1
1 6 1 1 3
2 6 1 1 1
2 5 1 2 2
3 0 0 1 1
3 1 1 1 3
3 2 1 1 2
4 5 0 2 2
6 5 1 1 2
3 5

Sample Output 2:

Distance = 3; Time = 4: 3 -> 2 -> 5
"""


#################################################################################
"""
一段时间没用dijkstra算法，又生疏了许多，花了比较长的时间！不熟练啊！
python超时无法解决
"""
#################################################################################


def dijkstra(maps, start, end):
    global N
    unvisited = list(range(N))
    unvisited.remove(start)
    now_station = start
    per_value = [float('inf') for _ in range(N)]
    per_value[now_station] = 0
    routine_back = [[] for _ in range(N)]
    while unvisited:
        for next_station in unvisited:
            temp = maps[now_station][next_station]
            if temp != -1:
                if per_value[next_station] > per_value[now_station] + temp:
                    per_value[next_station] = temp + per_value[now_station]
                    routine_back[next_station] = [now_station]
                elif per_value[next_station] == per_value[now_station] + temp:
                    routine_back[next_station].append(now_station)
        min_value = float('inf')
        min_station = -1
        for next_station in unvisited:
            if per_value[next_station] < min_value:
                min_value = per_value[next_station]
                min_station = next_station
        unvisited.remove(min_station)
        now_station = min_station
    return routine_back, per_value[end]


def find_fast(routine_back, start, end, r):
    global shortest_routine_with_fastest_time, time
    if end != start:
        for before in routine_back[end]:
            find_fast(routine_back, start, before, [before] + r)
    else:
        total_time = 0
        for i in range(len(r)-1):
            total_time += time[r[i]][r[i+1]]
        if total_time < shortest_routine_with_fastest_time[1]:
            shortest_routine_with_fastest_time = [r, total_time]


def find_short(routine_back, start, end, r):
    global fastest_time_with_shortest_routine
    if end != start:
        for before in routine_back[end]:
            find_short(routine_back,  start, before, [before] + r)
    else:
        if len(r) < fastest_time_with_shortest_routine[1]:
            fastest_time_with_shortest_routine = [r, len(r)]


N, M = map(int, input().split())
length = [[-1 for _ in range(N)] for _ in range(N)]
time = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    data = list(map(int, input().split()))
    length[data[0]][data[1]] = data[3]
    time[data[0]][data[1]] = data[4]
    if data[2] == 0:
        length[data[1]][data[0]] = data[3]
        time[data[1]][data[0]] = data[4]
source, destination = map(int, input().split())
routine, shortest_routine_length = dijkstra(length, source, destination)
shortest_routine_with_fastest_time = [0, float('inf')]
r_temp = [destination]
find_fast(routine, source, destination, r_temp)
routine, fastest_routine_time = dijkstra(time, source, destination)
fastest_time_with_shortest_routine = [0, float('inf')]
r_temp = [destination]
find_short(routine, source, destination, r_temp)
if shortest_routine_with_fastest_time[0] == fastest_time_with_shortest_routine[0]:
    print("Distance = %d; Time = %d: %s" % (shortest_routine_length, fastest_routine_time, ' -> '.join(map(str, shortest_routine_with_fastest_time[0]))))
else:
    print("Distance = %d: %s" % (shortest_routine_length, ' -> '.join(map(str, shortest_routine_with_fastest_time[0]))))
    print("Time = %d: %s" % (fastest_routine_time, ' -> '.join(map(str, fastest_time_with_shortest_routine[0]))))
