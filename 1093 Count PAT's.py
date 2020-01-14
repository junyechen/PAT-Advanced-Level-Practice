"""
The string APPAPT contains two PAT's as substrings. The first one is formed by the 2nd, the 4th, and the 6th characters, and the second one is formed by the 3rd, the 4th, and the 6th characters.

Now given any string, you are supposed to tell the number of PAT's contained in the string.
Input Specification:

Each input file contains one test case. For each case, there is only one line giving a string of no more than 10​5​​ characters containing only P, A, or T.
Output Specification:

For each test case, print in one line the number of PAT's contained in the string. Since the result may be a huge number, you only have to output the result moded by 1000000007.

Sample Input:

APPAPT

Sample Output:

2
"""

##################################################
"""
本题一开始没想好方法，想的就是找到P，然后找到A，然后计数剩下的T进行相加，有两个测试点超时，这必定会花很长时间
后面想的是，可以直接找A，然后分别计数A之前的P和之后T，相乘后的结果累加，但三个测试点超时
那么费时的就是每个A的P、T重新计数时间，重新设计：
    找到有有效P的第一个A，得到该A的P计数p和T计数t，该A的结果为p*t
    此后遍历后面的字符序列，若为P，则p+1，若为T，则t-1，若为A，则累加p*t；若t=0，则退出计数
"""
##################################################

message = input()
ans = 0
for i in range(0, len(message)-2):
    if message[i] == 'P':
        for j in range(i+1, len(message)-1):
            if message[j] == 'A':
                p = message[:j].count('P')
                t = message[j + 1:].count('T')
                ans = p * t
                break
        # else:
        #       continue
        break
for i in range(j+1, len(message)-1):
    if message[i] == 'P':
        p += 1
    elif message[i] == 'T':
        t -= 1
    else:
        ans += p * t
    if t == 0:
        break
print(ans % 1000000007)

'''
message = input()
ans = 0
for i in range(1, len(message)-1):
    if message[i] == 'A':
        ans += message[:i].count('P') * message[i+1:].count('T')
print(ans)
'''

'''
import collections


def Count(s):
    res = 0
    for i in range(len(s) - 2):
        if string[i] == 'P':
            for j in range(i+1, len(string) - 1):
                if string[j] == 'A':
                    increment = collections.Counter(s[j+1:])
                    if 'T' in increment:
                        res += increment['T']
                    else:
                        return res
    return res


string = input()
count = Count(string)
print(count)
'''
