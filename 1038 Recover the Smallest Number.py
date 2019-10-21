"""
Given a collection of number segments, you are supposed to recover the smallest number from them. For example, given { 32, 321, 3214, 0229, 87 }, we can recover many numbers such like 32-321-3214-0229-87 or 0229-32-87-321-3214 with respect to different orders of combinations of these segments, and the smallest number is 0229-321-3214-32-87.

Input Specification:

Each input file contains one test case. Each case gives a positive integer N (≤10
​4
​​ ) followed by N number segments. Each segment contains a non-negative integer of no more than 8 digits. All the numbers in a line are separated by a space.

Output Specification:

For each test case, print the smallest number in one line. Notice that the first digit must not be zero.

Sample Input:

5 32 321 3214 0229 87
Sample Output:

22932132143287
"""


#############################################
"""
本以为这道题很简单，字符串排序就可以，但马上发现32-3214不如3214-32小，而32是＜3214
一开始设想是补充数位，末尾补9，但是出现答案错误，思考一下发现32-3234，按照补9，则顺序为3234-32，但实际上应为32-3234
思考后发觉对于不同数位的字符，按照长短可分别设为A, B-C，使得B与A的数位相同，C可以为''
    对于排列顺序则有A-B-C或者B-C-A两种
        若A>B，则B-C-A
        若A<B，则A-B-C
        要讨论的只有A=B的情况，即A-A-C和A-C-A的比较，注意数位不齐的问题
************* 好吧，数学不行，分析讨论不下去了：
    为什么重复补充A的数字至补齐数位，然后按照字符串大小排序即可以得到答案？
    例 32-3234 32(323232)-3234(32343234)，结果为32-3234

经过这样的思考发现，对于原数列就是冒泡排序：
    即A+(B-C)与(B-C)+A的字符串大小比较，若前者小，则将A置于前一位，若前者大，则将A置于后一位。
    从第一位到最后依次两两比较，则最大的会在最后
    此后再从第一位到倒数第二两两比较
    这也和网上的大部分解题算法一致
"""
#############################################


seg = input().split()
seg.pop(0)
sup = [0] * len(seg)
for i in range(len(seg)):
    sup[i] = 8 - len(seg[i])
    seg[i] = seg[i] * 9
    seg[i] = seg[i][:9]
merge = [[a, b] for a, b in zip(seg, sup)]
merge.sort(key=lambda x: x[0])
string = ''
for i in range(len(merge)):
    string += merge[i][0][:8-merge[i][1]]
try:
    while string[0] == '0':
        string = string[1:]
except:
    string = '0'
print(string)

###########################################
"""
seg = input().split()
seg.pop(0)
sup = [0] * len(seg)
for i in range(len(seg)):
    sup[i] = 8 - len(seg[i])
    seg[i] += '9' * sup[i]
merge = [[a, b] for a, b in zip(seg, sup)]
merge.sort(key=lambda x: x[0])
string = ''
for i in range(len(merge)):
    string += merge[i][0][:8-merge[i][1]]
try:
    while string[0] == '0':
        string = string[1:]
except:
    string = '0'
print(string)
"""
###########################################
