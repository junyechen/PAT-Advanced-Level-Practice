"""
A traveler's map gives the distances between cities along the highways, together with the cost of each highway. Now you are supposed to write a program to help a traveler to decide the shortest path between his/her starting city and the destination. If such a shortest path is not unique, you are supposed to output the one with the minimum cost, which is guaranteed to be unique.

Input Specification:

Each input file contains one test case. Each case starts with a line containing 4 positive integers N, M, S, and D, where N (≤500) is the number of cities (and hence the cities are numbered from 0 to N−1); M is the number of highways; S and D are the starting and the destination cities, respectively. Then M lines follow, each provides the information of a highway, in the format:

City1 City2 Distance Cost
where the numbers are all integers no more than 500, and are separated by a space.

Output Specification:

For each test case, print in one line the cities along the shortest path from the starting point to the destination, followed by the total distance and the total cost of the path. The numbers must be separated by a space and there must be no extra space at the end of output.

Sample Input:

4 5 0 3
0 1 1 20
1 3 2 30
0 3 4 10
0 2 2 20
2 3 1 20
Sample Output:

0 2 3 3 40
"""


##################################################################
"""
本题相对简单，本次尝试直接使用dfs遍历所有路径。
主要卡在python的函数参数传递问题，若在函数中对list整个赋值，会造成递归回溯时，list新值丢失，只能通过引用的方法对list更新
    例：若原shortest = [1]
        在递归函数中 shortest = [0] 则在回溯时shortest != [0], shortest仍为[1]
        必须得使用shortest[0] = 0, 则在回溯时shortest = [0]
    始终记得，python中，函数传递时，list是传递首字节地址，若对整个list更改，则会造成地址变更，在回溯时只会找到原地址，因此改变的值无法保留
    同样注意python中list2 = list1这样赋值时，是传递list1首字节地址，若改变list1值，则list2也会相应改变，可使用list2 = list1.copy()只传递值
"""
##################################################################


def dfs(start, des, city, routine, shortest, cheapest, s_routine):
    if start == des:
        short, cheap = 0, 0
        for j in range(len(routine) - 1):
            short += dis_cos[routine[j]][routine[j + 1]][0]
            cheap += dis_cos[routine[j]][routine[j + 1]][1]
        if short < shortest[0]:
            shortest[0] = short
            cheapest[0] = cheap
            s_routine.pop()
            s_routine.append(routine.copy())
        elif short == shortest[0]:
            if cheap < cheapest[0]:
                cheapest[0] = cheap
                s_routine.pop()
                s_routine.append(routine.copy())
    else:
        for i in range(num_city):
            if dis_cos[start][i] != -1:
                if city[i] != 0:
                    city[i] = 0
                    routine.append(i)
                    dfs(i, des, city, routine, shortest, cheapest, s_routine)
                    city[i] = 1
                    routine.pop()


num_city, num_road, city_st, city_des = [int(_) for _ in input().split()]
dis_cos = [[-1 for _ in range(num_city)] for _ in range(num_city)]
for _ in range(num_road):
    temp = [int(_) for _ in input().split()]
    dis_cos[temp[0]][temp[1]] = dis_cos[temp[1]][temp[0]] = temp[2:4]
r = [city_st]
s = [city_des]
city = [1] * num_city
city[city_st] = 0
shortest, cheapest = [65536], [65536]
dfs(city_st, city_des, city, r, shortest, cheapest, s)
print(' '.join(list(map(str, s[0]))), shortest[0], cheapest[0])
