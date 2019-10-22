"""
Given a string, you are supposed to output the length of the longest symmetric sub-string. For example, given Is PAT&TAP symmetric?, the longest symmetric sub-string is s PAT&TAP s, hence you must output 11.

Input Specification:

Each input file contains one test case which gives a non-empty string of length no more than 1000.

Output Specification:

For each test case, simply print the maximum length in a line.

Sample Input:

Is PAT&TAP symmetric?
Sample Output:

11
"""

############################################################################################
"""
本题一开始觉得很难，后来想到先定下中点，然后由中间向两侧遍历比较是否回文即可
但是本题第一次没有通过，要注意回文可以分奇回文和偶回文，我只考虑了奇回文，造成有答案没能通过

后面学习"马拉车"算法，再次尝试，时间果然有明显提升，因为马拉车时间复杂度为O(n)，而前一个暴力遍历时间复杂度为O(n^2)，所以该算法所有案例运行时间均相近，为20ms左右，而暴力遍历最长有265ms。
    马拉车核心算法是基于回文字节的特殊性，同时利用往各个字节填充相同特殊符号"#"以排除奇回文和偶回文的影响。
        如 abacd 转化为 #a#b#a#c#d#
    另设置一队记录每个中心的回文半径长度，若半径为1，则表明该中心仅其自身"构成回文"
    从左往右依次遍历
        每一个中心均可得到对应的回文半径长度r，该中心的右边界r_boundary，也可以得知
        当遍历下一个中心时，判断该中心是否在边界内：
            1. 若该中心不在边界里，则无法利用回文数对称性质，故需要从该中心向两侧检测回文，从而得到该中心的回文半径长度r与该中心的右边界r_boundary，因该边界必定大于上一个中心的右边界，将其设置为当前遍历点的最大右边界
            2. 若该中心在边界里，则利用回文数对称性质，该中心的字母与该边界对应中心的对称点的字母相同
                1. 若对称点的左边界在当前最大左边界的右边，则依据回文对称性，该中心的右边界必定在当前最大右边界的左边，该中心的半径即为对称点的半径
                2. 若对称点的左边界在当前最大左边界的左边，则依据回文对称性，该中心右边界将超过当前最大右边界，但尚不清楚落在右边界何处，故需要从最大右边界开始，以该中心的为中心，向两侧检测回文，得到该中心的回文半径长度r与该中心的右边界r_boundary，并将该右边界作为最大右边界
"""
############################################################################################


string = input()
string_ = ""
for _ in string:
    string_ += '*' + _
string_ += '*'
r = [1] * len(string_)
r_max_index = 0
boundary_centre = 0
r_boundary = 0
for i in range(len(string_)):
    if i >= r_boundary:
        j = 1
        while i - j >= 0 and i + j <= len(string_) - 1 and string_[i - j] == string_[i + j]:
            j += 1
        r[i] = j
        if r[i] > r[r_max_index]:
            r_max_index = i
        if i + j - 1 > r_boundary:
            r_boundary = i + j - 1
            boundary_centre = i
    else:
        if r[boundary_centre * 2 - i] < r_boundary - i:
            r[i] = r[boundary_centre * 2 - i]
        else:
            j = r_boundary - i + 1
            while i - j >= 0 and i + j <= len(string_) - 1 and string_[i - j] == string_[i + j]:
                j += 1
            r[i] = j
            if r[i] > r[r_max_index]:
                r_max_index = i
            if i + j - 1 > r_boundary:
                r_boundary = i + j - 1
                boundary_centre = i
    if r_boundary == len(string_) - 1:
        break
print(r[r_max_index] - 1)

############################################################################################

string = input()
maximum = 1
for i in range(len(string)):
    j = 1
    while i - j >= 0 and i + j <= len(string) - 1 and string[i - j] == string[i + j]:
        j += 1
    if (j - 1) * 2 + 1 > maximum:
        maximum = (j - 1) * 2 + 1
    j = 0
    while i - j >= 0 and i + 1 + j <= len(string) - 1 and string[i - j] == string[i + 1 + j]:
        j += 1
    if (j - 1) * 2 + 2 > maximum:
        maximum = (j - 1) * 2 + 2
print(maximum)


#####################################################
"""
string = input()
maximum = 1
for i in range(1, len(string) - 1):
    j = 1
    while i - j >= 0 and i + j <= len(string) - 1:
        if string[i - j] == string[i + j]:
            j += 1
        else:
            break
    if 1 + (j - 1) * 2 > maximum:
        maximum = 1 + (j - 1) * 2
print(maximum)
"""
#####################################################
