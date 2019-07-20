"""
At the beginning of every day, the first person who signs in the computer room will unlock the door, and the last one who signs out will lock the door. Given the records of signing in's and out's, you are supposed to find the ones who have unlocked and locked the door on that day.
Input Specification:

Each input file contains one test case. Each case contains the records for one day. The case starts with a positive integer M, which is the total number of records, followed by M lines, each in the format:

ID_number Sign_in_time Sign_out_time

where times are given in the format HH:MM:SS, and ID_number is a string with no more than 15 characters.
Output Specification:

For each test case, output in one line the ID numbers of the persons who have unlocked and locked the door on that day. The two ID numbers must be separated by one space.

Note: It is guaranteed that the records are consistent. That is, the sign in time must be earlier than the sign out time for each person, and there are no two persons sign in or out at the same moment.
Sample Input:

3
CS301111 15:30:28 17:00:10
SC3021234 08:00:00 11:25:25
CS301133 21:45:00 21:58:40

Sample Output:

SC3021234 CS301133
"""

#################################
"""
非常简单，一次通过
参看他人思路，发现可以直接用字符串大小进行比较，而不需按时位进行
"""
#################################

M = int(input())
s_in = "23:59:59"
s_out = "00:00:00"
for _ in range(M):
    temp = input().split()
    if s_in > temp[1]:
        s_in = temp[1]
        sin = temp[0]
    if temp[2] > s_out:
        s_out = temp[2]
        sout = temp[0]
print(sin,sout)

#################################
"""
def timecom(t1, t2):
    if t1[:2]>t2[:2]:
        return 1
    elif t1[:2]<t2[:2]:
        return 0
    else:
        if t1[3:5]>t2[3:5]:
            return 1
        elif t1[3:5]>t2[3:5]:
            return 0
        else:
            if t1[6:8]>t2[6:8]:
                return 1
            else:
                return 0

M = int(input())
s_in = "23:59:59"
s_out = "00:00:00"
for _ in range(M):
    temp = input().split()
    if timecom(s_in,temp[1]):
        s_in = temp[1]
        sin = temp[0]
    if timecom(temp[2],s_out):
        s_out = temp[2]
        sout = temp[0]
print(sin,sout)
"""
##################################