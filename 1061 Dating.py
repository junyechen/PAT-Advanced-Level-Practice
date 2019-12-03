"""
Sherlock Holmes received a note with some strange strings: Let's date! 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm. It took him only a minute to figure out that those strange strings are actually referring to the coded time Thursday 14:04 -- since the first common capital English letter (case sensitive) shared by the first two strings is the 4th capital letter D, representing the 4th day in a week; the second common character is the 5th capital letter E, representing the 14th hour (hence the hours from 0 to 23 in a day are represented by the numbers from 0 to 9 and the capital letters from A to N, respectively); and the English letter shared by the last two strings is s at the 4th position, representing the 4th minute. Now given two pairs of strings, you are supposed to help Sherlock decode the dating time.
Input Specification:

Each input file contains one test case. Each case gives 4 non-empty strings of no more than 60 characters without white space in 4 lines.
Output Specification:

For each test case, print the decoded time in one line, in the format DAY HH:MM, where DAY is a 3-character abbreviation for the days in a week -- that is, MON for Monday, TUE for Tuesday, WED for Wednesday, THU for Thursday, FRI for Friday, SAT for Saturday, and SUN for Sunday. It is guaranteed that the result is unique for each case.
Sample Input:

3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm

Sample Output:

THU 14:04
"""

########################################################
"""
题目简单，理解题意花了点时间
"""
########################################################

line1 = input()
line2 = input()
line3 = input()
line4 = input()
DAY = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
flag = True
for i in range(min(len(line1), len(line2))):
    if line1[i] == line2[i] and flag:
        if 'A' <= line1[i] <= 'G':
            day = DAY[ord(line1[i]) - 65]
            flag = False
    elif line1[i] == line2[i] and not flag:
        if '0' <= line1[i] <= '9':
            hh = int(line1[i])
            break
        elif 'A' <= line1[i] <= 'N':
            hh = ord(line1[i]) - 65 + 10
            break
for i in range(min(len(line3), len(line4))):
    if line3[i] == line4[i] and ('a' <= line3[i] <= 'z' or 'A' <= line3[i] <= 'Z'):
        mm = i
        break
print(day, '%02d:%02d' % (hh, mm))
