"""
Behind the scenes in the computer's memory, color is always talked about as a series of 24 bits of information for each pixel. In an image, the color with the largest proportional area is called the dominant color. A strictly dominant color takes more than half of the total area. Now given an image of resolution M by N (for example, 800×600), you are supposed to point out the strictly dominant color.
Input Specification:

Each input file contains one test case. For each case, the first line contains 2 positive numbers: M (≤800) and N (≤600) which are the resolutions of the image. Then N lines follow, each contains M digital colors in the range [0,2​24​​). It is guaranteed that the strictly dominant color exists for each input image. All the numbers in a line are separated by a space.
Output Specification:

For each test case, simply print the dominant color in a line.
Sample Input:

5 3
0 0 255 16777215 24
24 24 0 0 24
24 0 24 24 24

Sample Output:

24
"""

##################################
"""
本题非常简单，本以为可能又败在python的处理速度上，但实际均通过了
方法一是最原始的想法，建一个字典，然后利用try-except异常机制，往字典里填数据，最后求最大值的键即可
方法二是利用题目中给出众数必定唯一存在，且众数数量必定大于一半，则可利用“摩尔投票法”：
    核心就是对拼消耗。玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。最后还有人活下来的国家就是胜利。那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。最后能剩下的必定是自己人。
但在实际运行中，两者运算速度差别不是很大，分析一下，时间复杂度都是O(n)，但是空间复杂度是“摩尔投票法”省，因为只需要一个键-值空间，而方法一需要完整地键-值空间
"""
##################################

##################################
"""
方法二
"""
##################################
m, n = map(int, input().split())
key, value = -1, 1
for _ in range(n):
    for c in input().split():
        if key == -1:
            key = c
        else:
            if key == c:
                value += 1
            else:
                value -= 1
                if value == 0:
                    key, value = -1, 1
print(key)
####################################

"""
m, n = map(int, input().split())
mode = [-1, 1]
flag = True
for _ in range(n):
    for c in input().split():
        if mode[0] == -1:
            mode[0] = c
        else:
            if mode[0] == c:
                mode[1] += 1
            else:
                mode[1] -= 1
                if mode[1] == 0:
                    mode = [-1, 1]
print(mode[0])
"""

##################################
"""
方法一
"""
##################################
"""
m, n = map(int, input().split())
color = {}
for _ in range(n):
    for c in input().split():
        try:
            color[c] += 1
        except:
            color[c] = 0
max_k, max_v = c, color[c]
for key, value in color.items():
    if value > max_v:
        max_v = value
        max_k = key
print(max_k)
"""